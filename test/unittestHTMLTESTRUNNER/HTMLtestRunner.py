#encoding=utf-8
from selenium import webdriver
import unittest,time
from lib.HTMLTestRunner_cn import HTMLTestRunner
# print os.getcwd()
class baidu(unittest.TestCase):
    u"""百度搜索测试"""   #必须放在此处否则无效
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../../lib/chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.baidu.com'

    def test_baidu_search(self):
        u"""搜索关键字"""   #必须放在此处，否则无效
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').send_keys('HTMLTestRunner')
        driver.find_element_by_id('su').click()

    def test_aaa(self):
        u''''纯测试多个测试用例而已'''
        pass

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite() #弄个测试套件，用来装多个测试用例的
    testunit.addTest(baidu('test_baidu_search'))#把测试用例装进套件中
    testunit.addTest(baidu('test_aaa'))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 定义报告存放路径 D盘根目录下 名为 时间+result.html  的文件
    filename = 'D:\ ' + now + 'result.html'
    fp = open(filename, 'wb')   #创建一个文件，如有同名直接覆盖
#fp = open('D:/result.html','wb')  #存放在D盘下
    runner = HTMLTestRunner(stream=fp,title=u'百度搜索报告',description=u'用例执行情况')
    runner.run(testunit)#运行测试套件
    fp.close()
