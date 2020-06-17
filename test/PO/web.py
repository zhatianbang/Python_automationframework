# coding:utf8

from selenium.webdriver import *
import time,os,random,datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from common.logger import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback,re

# 用类封装打开浏览器的方法
class BasePage():

    def __init__(self,writer):
        # 保存打开的浏览器
        self.writer = writer
        self.driver = None
        self.text = '' # 断言时会用到
        self.title = ''
        self.jsres = '' # 执行js后的返回值
        self.param ={} # 用于保存参数

    #定义打开浏览器的函数
    def openbrowser(self,browserType='gc',dir=None):

        if browserType == 'gc' or browserType=='chrome' or browserType == '' or browserType == None:
            if dir is None or dir == '':
                dir = './lib/chromedriver'
            option = ChromeOptions()  # 创建一个用来配置chrome属性的变量
            option.add_argument('disable-infobars')  # 去掉提示条

            # #是否启用无界面模式
            # option.add_argument("--headless")
            # option.add_argument("--no-sandbox")  # 解决DevToolsActivePort文件不存在的报错
            # option.add_argument("window-size=1936x1056") # 设置浏览器分辨率
            # option.add_argument("--disable-gpu")   # 谷歌文档提到需要加上这个属性来规避bug
            # option.add_argument("--hide-scrollbars")  #隐藏滚动条，应对一些特殊页面
            # option.add_argument("blink-settings=imagesEnabled=false")


            # 获取用户目录，提升加载速度
            # userdir = os.environ['USERPROFILE'] + "\\AppData\\Local\\Google\\Chrome\\User Data"
            # option.add_argument(r'--user-data-dir=' + userdir)
            self.driver = Chrome(executable_path=dir, options=option)
            self.driver.maximize_window()
            logger.info("成功打开chrome浏览器")
            self.driver.implicitly_wait(10)
            self.writer.write(self.writer.row, 7, 'PASS')
            return True
        elif browserType == 'ie':
            if dir is None or dir == '':
                dir = './lib/IEDriver.exe'
            self.driver = Ie(executable_path=dir)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.writer.write(self.writer.row, 7, 'PASS')
            return True
        elif browserType=='ff':
            if dir is None or dir == '':
                dir = './lib/geckodriver.exe'
            self.driver = Firefox(executable_path=dir)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.writer.write(self.writer.row, 7, 'PASS')
            return True
        else:
            print('暂未实现该浏览器')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, '暂未实现该浏览器')
            return False

    # 访问网站
    def get(self,url):
        try:
            self.driver.get(url)
            logger.info("成功访问url【" + url + "】")
            self.writer.write(self.writer.row, 7, 'PASS')
            return True
            # self.writer.write(self.writer.row, 8, 'url')
        except Exception as e:
            logger.error("访问url失败【"+url  + "】" )
            logger.error(traceback.format_exc())
            self.savepng()
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, e)
            return False

    def click(self,xpath):
        path = self.__replaceparam(xpath)
        try:
            self.__waitelementtobeclickable(path)
            self.driver.find_element_by_xpath(path).click()
            logger.info("点击成功【"+path  + "】")
            self.writer.write(self.writer.row, 7, 'PASS')
            # self.writer.write(self.writer.row, 8, 'xpath')
            return True
        except Exception as e:
            logger.error("点击失败】" + path  + "】")
            logger.error(traceback.format_exc())
            self.savepng()
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, e)
            return False


    def clear(self,xpath):
        try:
            ele = self.__find_element(xpath)
            ele.clear()
            logger.info("清除成功【" + xpath + "】")
            self.writer.write(self.writer.row, 7, 'PASS')
            return True
        except Exception as e:
            logger.error("清除失败【" + xpath + "】")
            logger.error(traceback.format_exc())
            self.savepng()
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, e)
            return False

    def input(self,xpath,value):
        valuep = self.__userandom(value)
        valuep = self.__replaceparam(valuep)
        path = self.__replaceparam(xpath)
        try:
            self.__waitelementtobeclickable(path)
            ele = self.driver.find_element_by_xpath(path)
            ele.clear()
            ele.send_keys(valuep)
            logger.info("向【" + path + "】输入【" + valuep +"】成功" )
            self.writer.write(self.writer.row, 7, 'PASS')
            return True
        except Exception as e:
            logger.error("向【" + path + "】输入【：" + valuep + "】失败！")
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, e)
            return False

    def inputcirculate(self,xpath,text):
        self.__waitelementtobeclickable(xpath)
        try:
            self.driver.find_element_by_xpath(xpath).clear()
            for i in text:
                self.driver.find_element_by_xpath(xpath).send_keys(i)
            logger.info("向【" + xpath +"】循环输入【"+ text + "】成功" )
            self.writer.write(self.writer.row, 7, 'PASS')
            return True
        except Exception as e:
            logger.info("向【" + xpath + "】循环输入【" + text + "】失败")
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.savepng()
            self.writer.write(self.writer.row,8,traceback.format_exc())
            return False

    # 关闭浏览器当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭浏览器tab成功")
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row,8, e)

    def sleep(self,t=3):
        try:
            time.sleep(int(float(t)))
            logger.info("等待成功：" + str(float(t)) + "秒！")
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            logger.error("等待失败：" + str(float(t)) + "秒！")
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row,8, e)

    def gettext(self,xpath):
        self.text = self.__find_element(xpath).text

    def intoiframe(self,xpath):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(xpath))

    def outiframe(self):
        self.driver.switch_to.default_content()

    def gettitle(self):
        self.title = self.driver.title


    def switchwindow(self,index=0):
        """切换到指定下标的窗口"""
        print(self.driver.window_handles)
        h = self.driver.window_handles
        self.driver.switch_to.window(h[int(index)])

    def assertequals(self,act,value):
        try:
            act = act.replace('{text}',self.text)
            act = act.replace('{jsres}',self.jsres)
            act = act.replace('{title}',self.title)
            if str(act) == value:
                logger.info("断言成功，实际值【"+act + "】，期望值【" + value  + "】")
                self.writer.write(self.writer.row, 7, 'PASS')
            else:
                logger.error("断言失败，实际值【" + act + "】,期望值【" + value  + "】")
                self.writer.write(self.writer.row, 7, 'FAIL')
                self.writer.write(self.writer.row, 8, str(act))
        except Exception as e:
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(e))

    # 断言元素消失，如元素被删除
    def assertinvisibility(self,xpath):
        '''断言元素消失，如元素被删除'''
        try:
            ele = self.driver.find_elements_by_xpath(xpath)
            if len(ele) == 0:
                self.writer.write(self.writer.row, 7, 'PASS')
                return True
            #　移除的概念不好理解啊
            elif (WebDriverWait(self.driver, 10, 0.5).until(EC.staleness_of(self.driver.find_element_by_xpath(xpath)))):
                self.writer.write(self.writer.row, 7, 'PASS')
                return True
        except Exception as e:
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(e))
            return False



    # 键盘下
    def pressdown(self,xpath):
        '''
        发送键盘按钮
        :param xpath: 元素定位表达式
        :return:
        '''
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(Keys.DOWN)
            self.writer.write(self.writer.row, 7, 'PASS')
            logger.info("键盘DOWN键成功" + xpath +"】")
            return True
        except Exception as e:
            logger.error("键盘DOWN键失败【" + xpath +"】" )
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(e))
            return False

    #　键盘下
    def pressenter(self,xpath):
        '''
        发送键盘按钮
        :param xpath: 元素定位表达式
        :return:
        '''
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(Keys.ENTER)
            self.writer.write(self.writer.row, 7, 'PASS')
            logger.info("键盘ENTER键成功" + xpath + "】")
            return True
        except Exception as e:
            logger.error("键盘ENTER键失败【" + xpath + "】")
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(e))
            return False

    def closebrowser(self):
        """退出驱动关闭所有窗口"""
        time.sleep(3)
        try:
            self.driver.quit()
            logger.info("关闭所有窗口，关闭所有驱动成功！")
            self.writer.write(self.writer.row, 7, 'PASS')
            return True
        except Exception as e:
            logger.error("关闭所有窗口，关闭所有驱动失败")
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(e))
            return False

    def closecurrentwindow(self):
        # 关闭selenium当前定位的窗口
        self.driver.close()

    # 滚动到指定元素（适合元素可见可定位，否则使用js滚动）
    def moveto(self,xpath):
        actions = ActionChains(self.driver)
        ele = self.__find_element(xpath)
        actions.move_to_element(ele).perform()

    def executejs(self,js):
        self.driver.execute_script(js)

    def elementisdisplay(self, element):
        flag = element.is_displayed()
        if flag == True:
            return element
        else:
            return False

    def forward(self):
        """浏览器前进按钮"""
        self.driver.forward()

    def back(self):
        """浏览器后退按钮"""
        self.driver.back()

    def refreshf5(self):
        '''强制刷新'''
        try:
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()
            logger.info("强制刷新浏览器成功")
            self.writer.write(self.writer.row, 7, 'PASS')
            return True
        except Exception as e:
            logger.info("强制刷新浏览器失败")
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(e))
            return False

    # def find_element(self,xpath):
    #     logger.info("测试")
    #     self.find_element(xpath)
    def savepng(self):
        """保存到项目根目录下的Screenshots下"""
        try:
            file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
            # now_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
            now_time = datetime.datetime.now().strftime('%Y%m%d_%H_%M_%S_%f')  # 含微秒的日期时间，来源 比特量化
            screen_name = file_path + now_time + '.png'
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("截图成功，文件名：" + now_time + ".png" )
        except Exception as e:
            logger.error("截图失败！")
            logger.error(traceback.format_exc())

    def runjsclick(self,xpath):
        path = self.__replaceparam(xpath)
        try:
            self.__waitelementtobeclickable(path)
            button = self.driver.find_element_by_xpath(path)
            self.driver.execute_script("$(arguments[0]).click()", button)
            logger.info("js点击成功：" + path)
            self.writer.write(self.writer.row, 7, 'PASS')
            return True
        except Exception as e:
            logger.error("执行js点击失败: ",path)
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(e))
            return False

    # ID = "id"
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"
    #
    # def jsscroll(self,loctype,loc):
    #     if loctype== 'CLASS_NAME':
    #         js = 'document.getElementsByClassName("'+ loc +'")[0].scrollTop=100'
    #
    #     driver.execute_script(js)

    # 滚动到目标元素
    def scrolltotarget(self,xpath):
        '''
        滚动至目标元素，这里元素要先定位到才可以
        :param xpath:  目标元素的xpath定位表达式
        :return:
        '''
        try:
            target = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            logger.info("成功滚动到目标元素：" + xpath)
            self.writer.write(self.writer.row, 7, 'PASS')
            return True
        except Exception as e:
            logger.error("滚动到目标元素：" + xpath + "失败！")
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(e))
            return False

    # 滚动条滚动到最上面
    def scrolltotop(self,id):
        '''
        滚动掉滚动到最顶部
        :param id: 滚动条元素id，也可以是className等属性
        :return:
        '''
        try:
            js =js = "document.getElementById(\'" + id + "\').scrollIntoView()"
            self.driver.execute_script(js)
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(e))
            return False

    def __find_element(self,xpath):
        try:
            element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.XPATH, xpath))
            return element
        except Exception as e:
            logger.error("查找元素失败：" + xpath)
            logger.exception(str(traceback.format_exc()))

    def __waitelementtobeclickable(self,xpath):
        """等待元素可点击"""
        try:
            time.sleep(1)
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,xpath)))
        except Exception as e:
            logger.error("等待元素：" + str(xpath) + "可点击失败！")
            logger.error(traceback.format_exc())

    def __userandom(self,s):
        """最多6位随机数"""
        if ("{" in s) & ("}" in s):
            return s
        else:
            try:
                res = s
                if s.find('useRandom') != -1:
                    res = s.replace('useRandom', str(random.randint(1, 999999)))
                    self.param[s] = str(res)
                return res
            except Exception as e:
                logger.error("替换成随机数失败：" , s)
                logger.error(traceback.format_exc())

    def __replaceparam(self,p):
        '''
        替换参数，如果参数中含有{}，则遍历list，把参数中{param}部分替换成list[param]对应的值，返回替换后的值，如无返回原参数值
        :param p: 需要进行替换的参数
        :return: 返回替换后的或者原始的p
        '''
        res = p
        try:
            reg = ".*\\{.*\\}.*"
            if re.match(reg, p):
                for key in self.param:
                    res = res.replace("{" + key + "}", self.param[key])
        except Exception as e:
            logger.error("替换参数", p ,"失败")
            logger.error(traceback.format_exc())
        return res

if __name__ == '__main__':
    file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
    print(file_path)


