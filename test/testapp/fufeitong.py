#coding:utf8
from appium  import webdriver
import time




caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "6.0.1"
caps["deviceName"] = "127.0.0.1:7555"
caps["appPackage"] = "com.neusoft.ebpp"
caps["appActivity"] = "com.shfft.ebpp.launcher.LoginActivityV3"
caps["noReset"] = "true"
caps["unicodeKeyboard"] = "true"
caps["resetKeyboard"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(20)


# 登陆
# try:
#     driver.find_element_by_xpath("//*[@text='登 录']").click()
#
#     time.sleep(1)
# except:
#     pass

##---------------------------密码登陆 上-----------------------------------
# ele = driver.find_element_by_id('com.neusoft.ebpp:id/edt_username')
# ele.clear()
#
# ele.send_keys("13236138473")
# time.sleep(1)
#
# driver.find_element_by_id('com.neusoft.ebpp:id/edtEnPwd').send_keys("dkjdkj1990")
# time.sleep(1)
# ##---------------------------密码登陆 下------------------------------------
# driver.find_element_by_xpath("//*[@text='登 录']").click()

# 扫一扫
driver.find_element_by_xpath("//*[@text='扫一扫']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@text='确定']").click()
time.sleep(1)

# 我要付款
driver.find_element_by_xpath("//*[@text='我要付款']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@content-desc='转到上一层级']").click()

# # 添加vip
# driver.find_element_by_xpath("//*[@text='添加VIP卡']").click()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@text='请输入18位卡号']").send_keys("123456789012345678")
# driver.find_element_by_xpath("//*[@text='请输入6位卡密码']").send_keys("123456")
# driver.find_element_by_xpath("//*[@content-desc='转到上一层级']").click()
#
# # 付费宝
# driver.find_element_by_xpath("//*[@text='实名激活付费宝']").click()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@text='身份证信息认证']").click()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@content-desc='转到上一层级']").click()
# time.sleep(1)
#
# driver.find_element_by_xpath("//*[@text='绑定银行卡']").click()
# time.sleep(1)
# driver.find_element_by_accessibility_id("转到上一层级").click()
# time.sleep(1)
# driver.find_element_by_accessibility_id("转到上一层级").click()
# time.sleep(1)
# driver.find_element_by_accessibility_id("转到上一层级").click()
# time.sleep(1)


# 水费
driver.find_element_by_xpath("//*[contains(@text,'水费')]").click()
time.sleep(1)
driver.find_element_by_xpath('//*[contains(@text,"上海市松江自来水有限公司")]').click()

time.sleep(1)
driver.find_element_by_xpath("//*[@text='8位数字']").send_keys("123456789")
time.sleep(1)
driver.find_element_by_xpath("//*[@text='查询']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@text='确认']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@content-desc='转到上一层级']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@content-desc='转到上一层级']").click()
time.sleep(1)

# 农场
driver.find_element_by_id("com.neusoft.ebpp:id/viewAdv").click()
time.sleep(1)
driver.find_element_by_accessibility_id("活动细则").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@content-desc='坚果农场']").click()
time.sleep(1)
try:
    """这里定位有问题"""
    driver.find_element_by_xpath("//*[@content-desc'坚果农场']/android.view.View[2]/android.view.View[1]").click()  #　关闭活动细则
    time.sleep(1)
except:
    pass
# driver.find_element_by_xpath('//*[@content-desc="坚果农场"]/android.view.View/android.view.View[3]/android.view.View[13]').click() # 能量助手
# time.sleep(1)
# driver.find_element_by_xpath('//*[@content-desc="能量收取提醒"]/following-sibling::android.widget.Button').click()    # 能量开关
# time.sleep(1)
# driver.find_element_by_accessibility_id("我要关闭").click()
time.sleep(1)
# driver.find_element_by_xpath('//*[@content-desc="坚果农场"]/android.view.View[4]/android.widget.Button').click()    # 开启能量提醒
time.sleep(1)
driver.find_element_by_accessibility_id('转到上一层级').click()
time.sleep(1)
# driver.find_element_by_accessibility_id("//*[@text='我要离开']").click()
time.sleep(1)
print(driver.find_element_by_id('com.neusoft.ebpp:id/im').get_attribute('elementId'))

aa='ad382de7-86f5-4648-9168-c61b6d4d131e'







