# coding:utf-8

import requests, json, jsonpath,re,traceback,random
from common.Excel import *
from common.logger import logger
from urllib import parse
from suds.client import Client
from suds.xsd.doctor import  Import,ImportDoctor

class HTTP():
    '''说明：
    1、 postJson方法的参数两种形式，默认为第二种，如需传第一种，需修改postJson方法调用__get_data即可：
        1.d= "{'username':'ronnie','password':'123456'}"这种格式postJson需调用 __get_data 方法
        2. d='username=ronnie&password=123456' 这种格式，postJson需调用 __get_data2 方法
    2、savaJson(self,key,p):# key为 上个请求返回的json结果中存在的key、p为保存参数时的自定义的键
    3、addheader(self,key,value):key是下个请求头中key，value是保存参数中的key（即2中的'{p}'），如保存参数中的存入的键是 't',则这里的value必须是'{t}'
    '''

    def __init__(self, writer):
        requests.packages.urllib3.disable_warnings()
        self.session = requests.session()
        # self.session.headers['content-type'] = 'application/x-www-form-urlencoded'
        self.session.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

        self.result = ''  # 保存返回的结果（未经编码等格式处理），临时使用
        self.jsonresult = {}  # 返回上个请求的结果，json格式
        self.param = {}  # 保存参数，用于下个请求
        self.url = ''
        self.writer = writer
        self.status_code=''

    def seturl(self, urlHost):
        """
        设置请求的url的host信息
        :param urlHost: url的
        :return:
        """
        if urlHost.startswith('http') or urlHost.startswith('https'):
            self.url = urlHost
            print("设置url成功 %s" % urlHost)
            logger.info("设置url成功 %s" % urlHost)
            self.writer.write(self.writer.row, 7, 'PASS')
            return True
        else:
            logger.info('ERROR：url格式错误')
            # print('ERROR：url格式错误')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, 'url格式错误:' + urlHost)
            return False

    def postjson(self, url, d=None, j=None):
        """
        发送post请求
        :param url: 可以是url+路径，也可以单纯是路径（路径不需反斜杠）
        :param d: d='username=ronnie&password=123456'
        :param j: 传递json字符串
        :return: 无
        """
        self.status_code = '' # 响应码置为空字符串，否则这时的响应码可能为上个请求的
        # 判断url格式
        if not (url.startswith('http') or url.startswith('https')):
            url = self.url +  url
        if d is None or d == '':
            pass
        else:
            d = self.__get_param(d)  # 如果d中有关联如 d='id={userid}'，则需要替换为：d='id=12324345325',如无则不替换
            d = self.__userandom(d) # 如果有UseRandom则替换成随机数
        if j is None or j=='':
            pass
        else:
            j = self.__userandom(j)  # 如果有UseRandom则替换成随机数
            j = self.__get_param(j)  # 如果d中有关联如"id":{userid}，则需要替换为："id":"123",如无则不替换
            j = self.__get_data(j)  # json格式字符串转为json

        # 如果请求https请求，报ssl错误，就在下面添加verify=False参数
        res = self.session.post(url, d, j)  # 发包
        self.status_code = res.status_code  # 获取响应码
        self.result = res.content.decode("utf8")
        print("postjson响应结果：%s" % self.result[0:200])  # 打印的内容会在BeautifulReport中可以看到
        try:
            jsons = self.result
            jsons = jsons[jsons.find('{'):jsons.rfind('}') + 1]  # 尝试处理非标准格式的json
            self.jsonresult = json.loads(jsons)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.jsonresult))
            logger.info("postjson请求发送成功！ %s %s %s"%(url,d,j))
            return True
        except Exception as e:
            print("postjson响应结果：%s" % self.result[0:200])  # 打印的内容会在BeautifulReport中可以看到
            # 等于空，不然等于上一次请求保存的json结果
            self.jsonresult = {}
            logger.error("响应结果转json失败")
            logger.exception(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.result))
            return False

    def get(self, url, params=None):
        """
        发送get请求
        :param url:
        :param params:  textSearch=96800
        :return:
        """
        self.status_code = '' # 响应码置为空字符串，否则这时的响应码可能为上个请求的
        # 判断url格式
        if not (url.startswith('http') or url.startswith('https')):
            url = self.url + url + '?' + params
        else:
            url = url + '?' + params

        # 如果请求https请求，报ssl错误，就在下面添加verify=False参数
        res = self.session.get(url, verify=False)  # 发包
        self.status_code = res.status_code  # 响应码
        self.result = res.content.decode("utf8")
        print("get请求响应结果：%s" % self.result[0:200])  # 打印的内容会在BeautifulReport中可以看到
        try:
            jsons = self.result
            jsons = jsons[jsons.find('{'):jsons.rfind('}') + 1]  # 尝试处理非标准格式的json
            self.jsonresult = json.loads(jsons)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.jsonresult))
        except Exception as e:
            # 等于空，不然等于上一次请求保存的json结果
            self.jsonresult = {}
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.result))

    # 适合restful接口
    def delete(self, url, params=None):
        """
        发送delete请求
        :param url:
        :param params:  textSearch=96800
        :return:
        """
        self.status_code = '' # 响应码置为空字符串，否则这时的响应码可能为上个请求的
        # 判断url格式
        if not (url.startswith('http') or url.startswith('https')):
            url = self.url  + url + '?' + params
        else:
            url = url + '?' + params
        url = self.__get_param(url)
        # 如果请求https请求，报ssl错误，就在下面添加verify=False参数
        res = self.session.delete(url)  # 发包
        self.status_code = res.status_code  # 响应码
        self.result = res.content.decode("utf8")
        print("DELETE响应码：%s" % self.status_code) # 打印的内容会在BeautifulReport中可以看到
        if self.result is None or self.result == "":
            logger.info("DELETE请求执行成功")
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.jsonresult))
            return True
        else:
            try:
                jsons = self.result
                jsons = jsons[jsons.find('{'):jsons.rfind('}') + 1]  # 尝试处理非标准格式的json
                self.jsonresult = json.loads(jsons)
                self.writer.write(self.writer.row, 7, 'PASS')
                self.writer.write(self.writer.row, 8, str(self.jsonresult))
                logger.info("DELETE请求执行成功")
                return True
            except Exception as e:
                # 等于空，不然等于上一次请求保存的json结果
                self.jsonresult = {}
                logger.error("DELETE请求执行失败")
                logger.exception(traceback.format_exc())
                self.writer.write(self.writer.row, 7, 'FAIL')
                self.writer.write(self.writer.row, 8, str(self.result))
                return False

    def addheader(self, key, value):
        """
        添加一个键值对，支持关联
        :param key:  键
        :param value: 键的值
        :return: 无
        """
        # key是下个请求头中key，value是保存参数中的key，如保存参数中的存入的键是 't',则这里的value必须是'{t}'
        # 因为待会self.__get_param(value)是对已经保存的参数的键进行遍历，如果键中的键能满足{value}格式的则就进行替换成对应的键值
        try:
            value = self.__get_param(value)
            self.session.headers[key] = value
            print("头域添加成功！key：%s,值：%s"%(key,value[0:200]))  # 打印的内容会在BeautifulReport中可以看到
            logger.info("添加头域成功 %s" % (self.session.headers))
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            print("头域添加失败！key：%s,值：%s"%(key,value[0:200]))  # 打印的内容会在BeautifulReport中可以看到
            logger.error("添加头域失败 %s %s"%(key,value))
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 8, str(self.session.headers))

    def removeheader(self, key):
        """
        从头里删除一个键值对
        :param key:
        :return:
        """
        try:
            self.session.headers.pop(key)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.session.headers))
        except Exception as e:
            logger.error('没有' + key + '这个键的header存在')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.session.headers))

    def savejson(self, p,jpath):
        """
        # key为 上个请求返回的json结果中存在的key、value为保存参数时的自定义的键
        :param key: 需要保存json的键
        :param p:  保存后，调用参数的参数名字{p}
        :return: 无
        """
        res = str(self.result)   # 默认res为返回结果的字符串
        try:
            s = str(jsonpath.jsonpath(self.jsonresult,jpath)[0])
            self.param[p] = s
            print("保存的key：%s，值：%s" % (p, s[0:200]))  # 打印的内容会在BeautifulReport中可以看到
            logger.info("保存参数成功！")
            self.writer.write(self.writer.row, 7, 'PASS')
            # self.writer.write(self.writer.row, 8, str(self.param[p]))
            return True
        except Exception as e:
            print('保存参数失败！键：%s,值：%s'%(p,traceback.format_exc()))
            logger.error('保存参数失败！键：%s,值：%s'%(p,jsonpath))
            logger.exception(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, traceback.format_exc())
            return False

    def assertequals(self, jpath, value):
        """
        断言json结果中某个键的值和value相等
        :param key: json结果的键
        :param value: 预期值
        :return: 无
        """
        value = self.__get_param(value)
        res = str(self.result)  # 返回结果转为字符串
        # 尝试用jsonpath提取jpath表达式中获取到的值，如果失败，res = str(self.result)
        try:
            res = str(jsonpath.jsonpath(self.jsonresult,jpath)[0])
        except Exception as e:
            logger.exception(e)
            pass
        if res == str(value):
            logger.info('断言成功')
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(res))
        else:
            logger.error('断言失败')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, '实际：' + str(res))

    def assertresponsecode(self,response_code):
        '''
        响应码断言
        :param response_code: 响应码，
        :return:
        '''
        if self.status_code == int(float(response_code)):
            print("断言响应码成功！预期：%s，实际：%s"%(self.status_code,response_code))
            logger.info('断言成功')
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, self.status_code)
            return True
        else:
            print("断言响应码失败！预期：%s，实际：%s"%(self.status_code,response_code))
            logger.error('断言失败')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, '实际：' +str(self.status_code))
            return False

    def __get_param(self, s):
        # 替换关联的参数
        for key in self.param:
            # 遍历已经保存的参数，并将传入的字符串里面，满足{key}所有字符串用key对应的值来替换,如无，则不替换
            s = s.replace('{' + key + '}', self.param[key])
        return s

    def __get_data(self, str):
        global false, null, true
        false = null = true = ""
        # d= "{'username':'ronnie','password':'123456'}" 这种格式的字符串可以直接转为字典
        str = eval(str)
        return str

    def __get_data2(self, s):
        # 如传入的是 d='username=ronnie&password=123456' 这种格式
        flg = False # 用来判断是否是标准格
        param = {}
        p = s.split('&')  # 返回的是list ，['username=ronnie', 'password=123456']
        for pp in p:
            # 通过成员变量，分割每个成员 成为 键 和 值 的结果
            ppp = pp.split('=')  # 返回的是list ['username','ronnie'] 和 ['password','123456']
            try:
                param[ppp[0]] = self.__urlEncode(ppp[1])  # self.__url_encode 对ppp[1]中的中文进行url编码
            except Exception as e:
                flg= True
                logger.info('url参数格式不标准! %s'%s)
                logger.exception(e)
        if flg:
            return s
        else:
            return param

    def __userandom(self,s):
        """将参数中的1个或者多个UseRandom替换为最多6位的随机数"""
        res = s
        try:
            if s.find('UseRandom') != -1:
                res = res.replace('UseRandom', str(random.randint(1, 999999)))
                self.param[s] = str(res)
            return res
        except Exception as e:
            logger.error("替换成随机数失败：" , s)
            logger.error(traceback.format_exc())
        return res

    def __urlEncode(self, s):
        regex = re.compile(u'[\u4e00-\u9fa5]')
        encodeRes = str(s)
        match = regex.search(s)
        if match:
            encoderes = str(parse.quote(s))
        return encodeRes

class SOAP:
    """
    这是webservice接口自动化的关键字库
    """
    def __init__(self,writer):
        # 定义wsdl描述文档的地址
        self.wsdl = ''
        self.client = None
        self.result = ''
        self.jsonres = {}
        self.writer = writer
        self.headers = {}
        self.params = {}
        self.doctor = None
    """
    @:param schema、xsd、namesapce
    """
    def adddoctor(self,schema=None,xsd=None,namespace=None):
        imp = Import(schema, location=xsd)
        # 指定命名空间
        imp.filter.add(namespace)
        self.doctor = ImportDoctor(imp)
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, str(self.wsdl))

    # 设置wsdl路径，并解析webservice服务
    def setwsdl(self,url):
        # 定义wsdl描述文档的地址
        self.wsdl = url
        self.client = Client(url=url,doctor = self.doctor)

    def callmethod(self,method,paramlist=None):
        # parmalist=None时会报错，所以做个判断传不传
        if paramlist == None or paramlist=='' :
            try:
                self.result = self.client.service.__getattr__(method)()
            except Exception as e:
                self.result=e.__str__()
                logger.exception(self.result)
                self.writer.write(self.writer.row, 7, 'FAIL')
                self.writer.write(self.writer.row, 8, str(self.result))
        else:
            paramlist = paramlist.split('、')
            for i in range(len(paramlist)):
                paramlist[i] = self.__get_param(paramlist[i])
                try:
                    self.result = self.client.service.__getattr__(method)(*paramlist)
                except Exception as e:
                    self.result = e.__str__()
                    logger.exception(e)
                    self.writer.write(self.writer.row, 7, 'FAIL')
                    self.writer.write(self.writer.row, 8, str(self.result))
        try:
            jsons = self.result
            jsons = jsons[jsons.find('{'):jsons.rfind('}')+1]
            self.jsonres = json.loads(jsons)
            logger.info('PASS')
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.jsonres))
        except Exception as e:
            self.jsonres ={}
            logger.info('FAIL')
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.result))

    # 添加头
    def addheader(self,key,value):
        try:
            value = self.__get_param(value)
            self.headers[key] =value
            self.client = Client(self.wsdl,headers =self.headers)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.jsonres))
            return True
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(traceback.format_exc())
            return False


    def removeheader(self,key,value):
        self.headers.pop(key)
        self.client = Client(self.wsdl,headers =self.headers)
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, str(self.jsonres))

    def savejson(self, jpath, p):
        """
        # key为 上个请求返回的json结果中存在的key、value为保存参数时的自定义的键
        :param key: 需要保存json的键
        :param p:  保存后，调用参数的参数名字{p}
        :return: 无
        """
        res = str(self.result)   # 默认res为返回结果的字符串
        try:
            self.params[p] = str(jsonpath.jsonpath(self.jsonresult,jpath)[0])
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.params[p]))
        except Exception as e:
            logger.error('保存参数失败！键：%s,值：%s'%(jsonpath,p))
            logger.exception(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.jsonres))



    def assertequals(self, jpath, value):
        """
        断言json结果中某个键的值和value相等
        :param key: json结果的键
        :param value: 预期值
        :return: 无
        """
        value = self.__get_param(value)
        status = False
        if value == 'None':
            value = None
        res = str(self.result)  # 返回结果转为字符串
        # 尝试用jsonpath提取jpath表达式中获取到的值，如果失败，res = str(self.result)
        try:
            res = str(jsonpath.jsonpath(self.jsonres,jpath)[0])
        except Exception as e:
            res = None
            logger.exception(e)
            pass
        if res == value:
            logger.info('断言成功')
            status = True
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(res))
        else:
            logger.info('断言失败')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, '实际：' + str(res))
            if res == None:
                res ='None'
            print("实际值：" + str(res))
        return status

    def __userandom(self,s):
        """把参数中的1个或者多个字符串UseRandom替换成最多6位的随机数"""
        try:
            res = s
            if s.find('UseRandom') != -1:
                res = res.replace('UseRandom', str(random.randint(1, 999999)))
                self.params[s] = str(res)
            return res
        except Exception as e:
            logger.error("替换成随机数失败：" , s)
            logger.error(traceback.format_exc())

    def __get_param(self, s):
        # 替换关联的参数
        for key in self.params:
            # 遍历已经保存的参数，并将传入的字符串里面，满足{key}所有字符串用key对应的值来替换,如无，则不替换
            s = s.replace('{' + key + '}', 'Bearer '+self.params[key])
        return s

if __name__ == '__main__':
    d = "{'username':'ronnie','password':'123456'}"  # 这种字符串可以直接解析成字典
    print(eval(d))
