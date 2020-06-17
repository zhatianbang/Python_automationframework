from APP_PO.runner.HTMLTestRunner_cn import HTMLTestRunner
import unittest
import os
import time


# cur_path = os.path.dirname(os.path.realpath(__file__))#获取当前脚本的工程目录
# case_path = os.path.join(cur_path, "case")        # 测试用例的路径
# report_path = os.path.join(cur_path, "report")  # 报告存放路径



cur_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) # 获取项目根目录
case_path = os.path.join(cur_path, "cases")        # 测试用例的路径
report_path = os.path.join(cur_path, "report")  # 报告存放路径


if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover(case_path,"cases*.py")
    """如果有多个discovery，可以利用测试套件
    all = unittest.TestSuite()
    all.addTests(discover)
    然后 run.run(all)即可"""
    #
    print(discover)
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = report_path+"\\"+now+"result.html"
    fp =open(filename, "wb")

    run = HTMLTestRunner(title="可以装逼的测试报告",
                                            description="测试用例参考description",
                                            stream=fp,
                                            retry=1)

    run.run(discover)
    fp.close()