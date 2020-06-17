#coding:utf8

from selenium import webdriver
import time,os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random

driver = webdriver.Chrome(executable_path='../../lib/chromedriver')

driver.get('http://test-cc.chintcloud.net/#/login')
driver.maximize_window()
print(driver.get_window_size())



driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='username-input']").send_keys("duankj@chint.com")
driver.find_element_by_xpath("//input[@id='password-input']").send_keys("a123456@")
driver.find_element_by_xpath("//*[@class='md-raised md-button md-tb-dark-theme md-ink-ripple']").click()




print("等待")
time.sleep(10)
try:
    driver.find_element_by_xpath("//*[@aria-label='编码格式']").click()

except:
    print("*************")
    button = driver.find_element_by_xpath("//*[@aria-label='编码格式']")
    driver.execute_script("$(arguments[0]).click()", button)


# 实现下拉框随机选择
# ele = driver.find_elements_by_xpath("//*[@role='presentation' and @aria-hidden='false']/md-select-menu/md-content/md-option")
# size = len(ele)
# print(size)
#
# ele[random.randint(0,size-1)].click()
#
# def rand_select(xpaths):
#     eles = driver.find_elements_by_xpath(xpaths)
#     eles[random.randint(0,len(eles)-1)].click()


from selenium.webdriver.support.select import Select
ele = driver.find_elements_by_xpath("//*[@role='presentation' and @aria-hidden='false']/md-select-menu/md-content")
s = Select(ele)

for select in s.options:
    print(select.text)
