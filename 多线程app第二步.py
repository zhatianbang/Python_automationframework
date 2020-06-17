# -*- coding: UTF-8 -*-
import unittest,sys,datetime
from BeautifulReport import BeautifulReport as bf
from utest import datadriven
from common import config
from common.mysql import Mysql
from common import logger
from common.excelresult import Res
from common.mail import Mail
from lib.HTMLTestRunner_cn import HTMLTestRunner
import time




"""测试htmltestRunner报告的"""
# unittest.main()
# suite = unittest.TestSuite()
# suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(testWeb))
# suite = unittest.defaultTestLoader.discover(".", pattern="baidu.py", top_level_dir=None)
# # 生成执行用例的对象
# runner = bf(suite)
# runner.report(filename='./test.html', description='这个描述参数是必填的')


def run(casename="多线程APP1"):
    # 运行的相对路径

    path = '.'
    # 用例路径
    casepath = ''
    resultpath = ''



    logger.info("开始用例")
    try:
        casepath = sys.argv[1]
    except:
        casepath = ''
    casefile = casename
    # 为空，则使用默认的
    if casepath == '':
        casepath = path + '/data/cases/'+ casefile +'.xls'
        resultpath = path + '/outputs/resultcases/chint结果-'+casefile+'.xls'
    else:
        # 如果是绝对路径，就使用绝对路径
        if casepath.find(':') >= 0:
            # 获取用例文件名
            resultpath = path + '/outputs/resultcases/chint结果-' + casepath[casepath.rfind('\\') + 1:]
        else:
            logger.error('非法用例路径')

    config.get_config(path + '/conf/conf.properties')
    # logger.info(config.config)
    # mysql = Mysql()
    # mysql.init_mysql(path + '/lib/userinfo.sql')
    logger.info("传递的参数是：%s,%s"%(casepath,resultpath))
    datadriven.getparams(casepath,resultpath)
    # print(datadriven.alllist)

    ### 下面三行代码为BeautifulReport 报告
    # suite = unittest.defaultTestLoader.discover("./utest/", pattern="WebTest.py", top_level_dir=None)
    # # 生成执行用例的对象
    # runner = bf(suite)
    # runner.report(filename='./report/test'+ casefile + '.html', description=datadriven.title)

    ### 下面几行代码为HTMLTestRunner 报告
    suite = unittest.defaultTestLoader.discover("./utest/", pattern="WebTest.py", top_level_dir=None)
    # 生成执行用例的对象
    runner = bf(suite)
    runner.report(filename='./outputs/report/test' + casefile + '.html', description=datadriven.title)


    # 记录结束时间，写入结果文件
    endtime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 用例结束时间
    datadriven.writer.set_sheet((datadriven.writer.get_sheets())[0])
    datadriven.writer.write(1, 4, endtime)  # 对结果文件第二行第四列写入开始时间

    # 保存结果文件
    datadriven.writer.save_close()

    # # 得到报告数据
    res = Res()
    r = res.get_res(resultpath)

    # 读取配置文件
    config.get_config('./conf/conf.properties')
    # logger.info(config.config)
    # logger.info(config.config['mail'])
    # 修改邮件数据
    html = config.config['mailtxt']  # 读取报告模板
    html = html.replace('title', r['title'])  # 替换模板中的数据
    html = html.replace('runtype', r['runtype'])
    html = html.replace('passrate', r['passrate'])
    html = html.replace('status', r['status'])
    html = html.replace('casecount', r['casecount'])
    html = html.replace('starttime', r['starttime'])
    html = html.replace('endtime', r['endtime'])

    if r['status'] == 'Fail':
        html = html.replace('#00d800', 'red')

    # 根据结果决定是否发送邮件
    if r['status'] == 'Fail':
        logger.info("开始发送邮件")
        mail = Mail()
    #     mail.send(html)

    logger.info("结束用例")



    # from APP_PO.common.server import *
    #
    # devices_name = "逍遥"
    # yaml_name = "qq.yaml"
    #
    # device_info = get_device_info(devices_name, yaml_name)
    # # 启动设备
    # start_simulator()
    # adb_connect_device(device_name=device_info["desired_caps"]["deviceName"])
    # start_appium(port=device_info["port"], udid=device_info["desired_caps"]["udid"])
    # run_app(port=device_info["port"], desired_caps=device_info["desired_caps"])
if __name__ == '__main__':
    # run()
    import threading
    t1= threading.Thread(target=run,args=("多线程APP1",))
    t2= threading.Thread(target=run,args=("多线程APP2",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
