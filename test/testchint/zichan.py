#coding:utf8

from selenium import webdriver
import time,os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='../../lib/chromedriver')

driver.get('http://test-cc.chintcloud.net/#/login')
driver.maximize_window()
print(driver.get_window_size())



driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='username-input']").send_keys("common-api@chint.com")
driver.find_element_by_xpath("//input[@id='password-input']").send_keys("common-api")
driver.find_element_by_xpath("//*[@class='md-raised md-button md-tb-dark-theme md-ink-ripple']").click()

xpath ="//*[@class='md-raised md-button md-tb-dark-theme md-ink-ripple']"

ele = driver.find_elements_by_xpath(xpath)
try:
    if len(ele) == 0:
        print("0")
    elif (WebDriverWait(driver, 10, 0.5).until(EC.staleness_of(driver.find_element_by_xpath(xpath)))) :
        print("移除")
except Exception as e:
        print("错误")

driver.delete_all_cookies()
###-------------------------------------------------------新增资产----------------------------------------------------------- -----------
driver.find_element_by_xpath("//*[@section='section']/descendant::span[contains(text(),'资产')]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@aria-haspopup='true']/button").click()
time.sleep(1)
# driver.find_element_by_xpath("//ng-md-icon[@icon='insert_drive_file']").click()

button = driver.find_element_by_xpath("//ng-md-icon[@icon='insert_drive_file']")
driver.execute_script("$(arguments[0]).click()", button)


time.sleep(1)
driver.find_element_by_xpath("//*[@name='name' and @style='']").send_keys("资产12312")

time.sleep(1)
driver.find_element_by_xpath("//*[@aria-label='资产类型' and not(@disabled='disabled')]").send_keys("我是资产类型123")

time.sleep(1)
driver.find_element_by_xpath("//textarea[@name='description' and @rows='2']").send_keys("22222")

#点击添加
time.sleep(1)
driver.find_element_by_xpath("//span[contains(text(), '添加')] / parent::button[ @ type = 'submit']").click()

#点击公开
time.sleep(1)
driver.find_element_by_xpath("//*[contains(text(),'资产12312')]/ancestor::md-card/descendant::div[@aria-label='分享']").click()

#点击是
time.sleep(1)
driver.find_element_by_xpath("//*[contains(text(), '资产12312')] /../../ descendant::span[contains(text(), '是')]").click()
time.sleep(3)
driver.refresh()

#打开资产面板
time.sleep(1)
# driver.find_element_by_xpath("//span[contains(text(), '资产12312')]").click()


from selenium.webdriver import ActionChains
# element = driver.find_element_by_xpath("//span[contains(text(), '资产12312')]")
element=driver.find_element_by_xpath("//div[contains(text(), '我是资产类型123')]")
actions=ActionChains(driver)
actions.move_to_element(element).click().perform()
#资产属性tab
time.sleep(1)
driver.find_element_by_xpath("//*[@header-title='资产12312']/descendant::md-tab-item/span[contains(text(),'属性')]").click()


#添加属性
time.sleep(1)
driver.find_element_by_xpath("//span[contains(text(),'平台端属性')]/../button/md-icon[contains(text(),'add')]").click()


# 输入键
driver.find_element_by_xpath("//*[@name='key']").send_keys("abc")
driver.find_element_by_xpath("//*[@name='value']").send_keys("3333")
driver.find_element_by_xpath("//*[@type='submit']/span[contains(text(),'添加')]").click()


