#coding:utf8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  #WebDriverWait注意大小写
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,chardet
import logging
#具体chromedriver的位置
driver = webdriver.Chrome(executable_path='../../lib/chromedriver')
driver.get("http://test-cc.chintcloud.net")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element_by_xpath("//input[@id='username-input']").send_keys(u"xmfang@chint.com")
# driver.find_element_by_xpath("//input[@id='password-input']").send_keys(u"xmfang1@")
# driver.find_element_by_xpath("//button[@type='submit']").click()
# # element = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'xu11']")))
# element = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,".tb-user-display-name ng-binding xh-highlight")))
sss  =".tb-user-display-name ng-binding xh-highlight"
print(type(sss))
print(chardet.detect(sss))
print(sss)

# username = driver.find_element_by_xpath("//*[contains(text(),'xu11']").text
# if(username == "xu11"):
#     print("登录成功")
# else:
#     print("登录失败")
#
# EC.presence_of_element_located
#
#
# #name = driver.find_element_by_xpath("//span[@class='tb-user-display-name ng-binding']").text
# # if(name == "xu11"):
# # #     print("登录成功")
# # # else:
# # #     print("登录失败")
# time.sleep(2)
