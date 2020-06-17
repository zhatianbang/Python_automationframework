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
###-------------------------------------------------------上传自定义测点----------------------------------------------------------- -----------
driver.find_element_by_xpath("//*[contains(text(),'产品管理')]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[contains(text(),'新增产品名字453467')]/../descendant::md-icon[@aria-label='添加测点']").click()
time.sleep(1)
driver.find_element_by_xpath("//span[contains(text(),'自定义测点')]/parent::md-tab-item").click()
time.sleep(1)
driver.find_element_by_xpath("//span[contains(text(),'导入自定义测点文件')]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[contains(text(),'拖动或者单击以选择要导入的文件')]").click()
time.sleep(1)

os.system(r"D:\installation\pythonworkspace\AutomationFramework\lib\upload.exe %s"%(r"C:\Users\duankj\Desktop\11111.xlsx"))

time.sleep(1)
driver.find_element_by_xpath("//span[contains(text(),'导入')]").click()



# element = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'common-api')]")))


# driver.find_element_by_xpath("//*[contains(text(),'产品管理')]").click()
# driver.find_element_by_xpath("//*[@aria-haspopup='true']/button").click()
# time.sleep(1)
# # driver.find_element_by_xpath("//ng-md-icon[@icon='insert_drive_file']/..").click()
#
# button = driver.find_element_by_xpath("//ng-md-icon[@icon='insert_drive_file']/..")
# driver.execute_script("$(arguments[0]).click()", button)
#
# time.sleep(3)
# driver.find_element_by_xpath("//input[@name='title' and @ng-model='tenant.productName']").send_keys("信息化的那篇UseRandom")
#
# driver.find_element_by_xpath("//*[contains(text(),'所属产品分类')]").click()
#
#
#
# target = driver.find_element_by_xpath("//a[contains(text(),'ronnie专用误删')]")
# # print(len(target))
#
# driver.execute_script("arguments[0].scrollIntoView();", target)
# driver.find_element_by_xpath("//a[contains(text(),'ronnie专用误删')]").click()
#
# driver.find_element_by_xpath("//*[contains(text(),'产品型号')]/../input").send_keys("sn1231233")
# driver.find_element_by_xpath("//*[@aria-label='编码格式']").click()
# driver.find_element_by_xpath("//*[@value='GB2312']").click()
# driver.find_element_by_xpath("//*[@aria-label='接入协议']").click()
# driver.find_element_by_xpath("//*[@value='MQTT']").click()
# driver.find_element_by_xpath("//*[@value='一机一密']").click()
#
# targets = driver.find_elements_by_xpath("//*[contains(text(),'描述')]")
# print(len(targets))
#
# driver.execute_script("arguments[0].scrollIntoView();", targets[0])
#
#
# time.sleep(3)
# driver.find_element_by_xpath("//*[@class='ng-binding ng-scope' and contains(text(),'添加')]").click()




#　设备模块
# driver.find_element_by_xpath("//*[@section='section']/descendant::span[contains(text(),'设备')]").click()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@aria-haspopup='true']/button").click()
# time.sleep(1)
# path ="//ng-md-icon[@icon='insert_drive_file']"
# button = driver.find_element_by_xpath(path)
# driver.execute_script("$(arguments[0]).click()", button)
#
# time.sleep(1)
# driver.find_element_by_xpath("//*[@name='name' and @style='']").send_keys("新增直连设备寂寞")
# time.sleep(1)
# driver.find_element_by_xpath("//*[@aria-label='所属产品']").click()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@aria-label='所属产品']").send_keys("我_一型一密_直连非ss")
# time.sleep(3)
# ele =driver.find_elements_by_xpath("//*[@aria-label='所属产品']")
# print(len(ele))
# try:
#     driver.find_elements_by_xpath("//*[@aria-label='所属产品']")[0].click()
#     print("成功")
# except Exception as e:
#     print("失败了")
#     try:
#         driver.find_elements_by_xpath("//*[@aria-label='所属产品']")[1].click()
#         print("第二个成功了")
#     except Exception as e:
#         print("又事变了")
# time.sleep(3)
# driver.find_elements_by_xpath("//*[@aria-label='所属产品']")[0].send_keys(Keys.DOWN)
# time.sleep(3)
# driver.find_element_by_xpath("//*[@aria-label='所属产品']").send_keys(Keys.ENTER)
#
#
# time.sleep(3)
# driver.close()