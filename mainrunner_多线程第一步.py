#coding:utf-8
from interface.inter import HTTP
from app.App import APP
from common.Excel import *
import inspect,time
from common.excelresult import Res
from common import config
from common.mail import Mail

# def runcase(line):
#     if line[3]== 'post':
#         http.postJson(line[4],line[5],line[6])
#         return
#
#     if line[3] == 'assert':
#         http.assertequals(line[4],line[5])
#         return




# #**************************************
# func = getattr(http,'postJson')
# func("http://www.testingedu.com.cn/inter/HTTP/auth")
# args = inspect.getfullargspec(func).__str__()
# print(args)
#
# args = args[args.find("args=")+5:args.rfind(', varargs=None')]
# print(args)
#
# args = eval(args)
# args.remove('self')
# print(args)
# #**************************************


# #*********** 反射调用关键字 ***************************



def main(case_name="多线程APP1"):
    def runcase(line):
        # 分组信息不用执行
        if len(line[0]) > 0 or len(line[1]) > 0:
            return
        # 反射获取关键字函数
        func = getattr(http, line[3])
        # 获取参数列表
        args = inspect.getfullargspec(func).__str__()
        args = args[args.find('args=') + 5:args.rfind(', varargs')]
        args = eval(args)
        args.remove('self')
        # 根据参数调用
        # print(len(args))
        if len(args) == 0:
            func()
            return

        if len(args) == 1:
            func(line[4])
            return

        if len(args) == 2:
            func(line[4], line[5])
            return

        if len(args) == 3:
            func(line[4], line[5], line[6])
            return
        print('warning:目前只支持三个关键字调用')
    case_name =case_name

    case_path = './data/cases/'+ case_name +'.xls'
    resultcase_path = './outputs/resultcases/result-'+ case_name +'.xls'

    reader = Reader()
    reader.open_excel(case_path)
    sheetname = reader.get_sheets()
    writer = Writer()
    writer.copy_open(case_path,resultcase_path)

    # 根据情况实例化app、web、接口对象
    # http = HTTP(writer)
    http = APP(writer)


    # 测试开始时间
    writer.set_sheet(sheetname[0])
    startTime = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    writer.write(1,3,str(startTime))
    for sheet in sheetname:
        # 设置当前读取的sheet页面
        reader.set_sheet(sheet)
        # 设置写的sheet页，保持读和写是同一个sheet
        writer.set_sheet(sheet)
        for i in range(reader.rows):
            writer.row = i
            line = reader.readline()
            runcase(line)
    # 写入结束时间
    endTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    writer.write(1,4,str(endTime))
    writer.save_close()

        # 得到报告数据
    res = Res()
    r = res.get_res(resultcase_path)

    # 读取配置文件
    config.get_config('./conf/conf.properties')
    logger.info(config.config)
    logger.info(config.config['mail'])
    # 修改邮件数据
    html = config.config['mailtxt']     # 读取报告模板
    html = html.replace('title',r['title']) # 替换模板中的数据
    html = html.replace('runtype',r['runtype'])
    html = html.replace('passrate',r['passrate'])
    html = html.replace('status',r['status'])
    html = html.replace('casecount',r['casecount'])
    html = html.replace('starttime',r['starttime'])
    html = html.replace('endtime',r['endtime'])
    if r['status'] == 'Fail':
        html = html.replace('#00d800','red')

# mail = Mail()
# mail.send(html)

if __name__ == '__main__':
    # 多线程测试
    import threading
    cases_list = ["多线程APP1","多线程APP2"]
    t_list=[]
    for i in cases_list:
        t = threading.Thread(target=main,args=(i,))
        t_list.append(t)

    for j in t_list:
        j.start()

    for j in t_list:
        j.join()
    print("多线程结束")