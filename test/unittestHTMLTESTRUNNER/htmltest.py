# coding:utf-8
import unittest
import os,time
from lib.HTMLTestRunner_cn import HTMLTestRunner

# python2.7要是报编码问题，就加这三行，python3不用加
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

cur_path = os.path.dirname(os.path.realpath(__file__))#获取当前脚本的工程目录
case_path = os.path.join(cur_path, "unittestHTMLTESTRUNNER")        # 测试用例的路径
report_path = os.path.join(cur_path, "report")  # 报告存放路径

if __name__ == "__main__":
    print(cur_path)
    """start_dir = 测试文件的路径
        Pattern = “test*.py” 匹配规则，*匹配多个字符，test*.py是unittest写的方法
        Top_level_dir = None、    None 表示该文件就是顶层目录（这个参数一般不用动"""
    discover = unittest.defaultTestLoader.discover(cur_path,"test*.py")
    print(discover)  # 打印
    html = cur_path +"\test.html"  # 生成的报告
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    fp =open(html, "wb")
    run = HTMLTestRunner(title="可以装逼的测试报告",
                                            description="测试用例参考description",
                                            stream=fp,
                                            retry=1)

    run.run(discover)
    fp.close()


    # """如果有多个discovery，可以利用测试套件
    # all = unittest.TestSuite()
    # all.addTests(discover)
    # 然后 run.run(all)即可"""
    # print(discover)
    # now = time.strftime("%Y-%m-%d_%H_%M_%S")
    # filename = report_path+"\\"+now+"result.html"
    # fp =open(filename, "wb")
    #
    # run = HTMLTestRunner_jpg.HTMLTestRunner(title="可以装逼的测试报告",
    #                                         description="测试用例参考description",
    #                                         stream=fp,
    #                                         retry=1)
    #
    # run.run(discover)
    # fp.close()