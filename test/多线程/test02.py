# coding:utf-8

import unittest
from selenium import webdriver
import time

class Testaa(unittest.TestCase):
    u'''测试用例a的集合'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")

    def setUp(self):
        self.driver.get("https://www.cnblogs.com/yoyoketang/")
        print("test")


    def test_01(self):
        u'''用例1：用例1的操作步骤'''
        t = self.driver.title
        print(t)
        self.assertIn("悠悠", t)


    def test_02(self):
        u'''用例2：用例2的操作步骤'''
        t = self.driver.title
        print(t)
        self.assertIn("悠悠", t)

    def test_03(self):
        u'''用例3：用例3的操作步骤'''
        t = self.driver.title
        print(t)
        self.assertIn("悠悠", t)

    # def tearDown(self) -> None:
    #     print("每个方法执行一次")
    #     self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()