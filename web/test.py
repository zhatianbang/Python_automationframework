#!/usr/bin/env python
# -*- codinfg:utf-8 -*-
'''
@author: Jeff LEE
@file: chrome下载.py
@time: 2019-06-26 16:32
@desc:
'''
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(executable_path=r'D:\installation\pythonworkspace\AutomationFramework\lib\chromedriver.exe', options=options)
driver.get("https://test-cc.chintcloud.net/")

import traceback
time.sleep(20)
try:
    ele = driver.find_element_by_xpath("//*[contains(text(),'下载模板')]")

    driver.execute_script("$(arguments[0]).click()", ele)
except:
    print(traceback.format_exc())
    driver.find_element_by_xpath("//*[contains(text(),'下载模板')]/..").click()
    print("导入模板下载成功")


time.sleep(30)
driver.quit()