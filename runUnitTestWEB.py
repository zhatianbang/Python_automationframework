# -*- coding: UTF-8 -*-
import unittest,sys,datetime,os
from BeautifulReport import BeautifulReport as bf
from utest import datadriven
from common import config
from common.mysql import Mysql
from common import logger
from common.excelresult import Res
from common.mail import Mail

# 运行的相对路径
path = '.'
# 用例路径
casepath = ''
resultpath = ''
# 结果文件的名字
result_name=""

if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(testWeb))
    # suite = unittest.defaultTestLoader.discover(".", pattern="baidu.py", top_level_dir=None)
    # # 生成执行用例的对象
    # runner = bf(suite)
    # runner.report(filename='./test.html', description='这个描述参数是必填的')
    logger.info("开始用例")
    try:
        casepath = sys.argv[1]
    except:
        casepath = ''
    #用例源文件的文件名
    casefile = "WEBbasic"


    # 为空，则使用默认的
    if casepath == '':
        casepath = path + '/data/cases/'+ casefile +'.xls'

        now_time = datetime.datetime.now().strftime('%Y%m%d_%H_%M_%S')  # 含微秒的日期时间，来源 比特量化

        # 用例的结果文件名
        result_name = 'chintweb结果-' + casefile + now_time + '.xls'

        # 结果文件路径及文件，用于结果文件的统计
        # resultpath = path + '/data/results/'+ result_name
        resultpath = path + '/outputs/resultcases/' + result_name
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
    datadriven.getparams(casepath,resultpath)
    # print(datadriven.alllist)

    suite = unittest.defaultTestLoader.discover("./utest/", pattern="WebTest.py", top_level_dir=None)
   # 生成执行用例的对象
    runner = bf(suite)
    runner.report(filename='./outputs/report/test'+ casefile + '.html', description=datadriven.title)

    # 记录结束时间，写入结果文件
    endtime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 用例结束时间
    datadriven.writer.set_sheet((datadriven.writer.get_sheets())[0])
    datadriven.writer.write(1, 4, endtime)  # 对结果文件第二行第四列写入开始时间

    # 保存结果文件
    datadriven.writer.save_close()

    # 得到报告数据
    res = Res()
    r = res.get_res(resultpath)


    # 读取配置文件
    config.get_config('./conf/conf.properties')
    config.config["mailtitle"] = r['title']


    # 修改邮件数据
    html = config.config['mailtxt']  # 读取报告模板
    html = html.replace('title', r['title'])  # 替换模板中的数据
    html = html.replace('runtype', r['runtype'])
    html = html.replace('passrate', r['passrate'])
    html = html.replace('status', r['status'])
    html = html.replace('casecount', r['casecount'])
    html = html.replace('starttime', r['starttime'])
    html = html.replace('endtime', r['endtime'])
    html = html.replace('successcount',r['passcount'])
    html = html.replace('failcount',r['failcount'])


    logger.info(r['status'])

    if r['status'] != 'Pass':
        html = html.replace('#00d800', 'red')

        #根据结果决定是否发送邮件
        logger.info("开始发送邮件")
        mail = Mail()
        mail.mail_info['filepaths'] = [resultpath]
        mail.mail_info['filenames'] = [result_name]
        # mail.send(html)

    logger.info("结束用例")


