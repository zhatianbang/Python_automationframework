from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction


caps = {'platformName': 'Android', 'deviceName': '127.0.0.1:21503', 'platformVersion': '7.1.2', 'appPackage': 'com.chint.cloud.industry', 'appActivity': 'com.chint.plugin.userinfos.ui.activity.LoginActivity',
        'noReset': True, 'udid': '127.0.0.1:21503',
        "automationName":"appium",
        "autoGrantPermissions": True,  # 设置自动授权权限
        'unicodeKeyboard':True,  # 输入中文时要加，要不然输入不了中文
        'resetKeyboard':True  # 输入中文时要加，要不然输入不了中文
        }

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
el1 = driver.find_element_by_id("com.chint.cloud.industry:id/user_input")
el1.send_keys("1234567")
el2 = driver.find_element_by_id("com.chint.cloud.industry:id/password_input")
el2.send_keys("abc@123")
el3 = driver.find_element_by_id("com.chint.cloud.industry:id/login_btn")
el3.click()

def find_Toast2( message):  # 查找toast值
    '''
    method explain:查找toast的值,与find_Toast实现方法一样，只是不同的2种写法
    parameter explain：【text】查找的toast值
    Usage:
        device.find_Toast2('再按一次退出iBer')
    '''
    print("查找toast值---'%s'" % (message))
    try:
        message = "//*[contains(@text,'%s')]"%message
        print(message)
        WebDriverWait(driver,10, 0.5).until(EC.presence_of_element_located((By.XPATH, message)))
        print("查找到toast----%s" % message)
        return True
    except:
        print("未查找到toast----%s" % message)
        return False
find_Toast2("登陆")
import time
time.sleep(2)

el4 = driver.find_element_by_id("com.chint.cloud.industry:id/fast_billing")
el4.click()
el5 = driver.find_element_by_id("com.chint.cloud.industry:id/orderName")
el5.send_keys("公开的工单名称1")
el6 = driver.find_element_by_id("com.chint.cloud.industry:id/linkMan")
el6.send_keys("联系人姓名测试")
el7 = driver.find_element_by_id("com.chint.cloud.industry:id/mobile")
el7.send_keys("13000000000")
el8 = driver.find_element_by_id("com.chint.cloud.industry:id/addressProvince")
el8.click()
el9 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[10]/android.widget.LinearLayout")
el9.click()
el10 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[9]")
el10.click()
el11 = driver.find_element_by_id("com.chint.cloud.industry:id/maxAmount")
el11.click()
el12 = driver.find_element_by_id("com.chint.cloud.industry:id/address")
el12.send_keys("山西省大同市打通宵")
el13 = driver.find_element_by_id("com.chint.cloud.industry:id/content")
el13.send_keys("请输入服务描述的内容")
el14 = driver.find_element_by_id("com.chint.cloud.industry:id/tool")
el14.send_keys("工具名称测试呢容")

# 最低预算
el15 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[8]/android.widget.LinearLayout")
el15.click()
el16 = driver.find_element_by_id("com.chint.cloud.industry:id/minAmount")
el16.send_keys("1")

#　最高预算
el17 = driver.find_element_by_id("com.chint.cloud.industry:id/maxAmount")
el17.send_keys("10000")

el18 = driver.find_element_by_id("com.chint.cloud.industry:id/executeStartTime")
el18.click()
el19 = driver.find_element_by_id("com.chint.cloud.industry:id/tv_wheel_ok")
el19.click()
el20 = driver.find_element_by_id("com.chint.cloud.industry:id/executeEndTime")
el20.click()
TouchAction(driver).press(x=596, y=1162).move_to(x=596, y=940).release().perform()

el21 = driver.find_element_by_id("com.chint.cloud.industry:id/tv_wheel_ok")
el21.click()
el22 = driver.find_element_by_id("com.chint.cloud.industry:id/ll_serviceType")
el22.click()

time.sleep(3)
el23 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.TextView")
el23.click()
el24 = driver.find_element_by_id("com.chint.cloud.industry:id/tv_true")
el24.click()
TouchAction(driver).press(x=350, y=927).move_to(x=302, y=503).release().perform()

el25 = driver.find_element_by_id("com.chint.cloud.industry:id/product_brand")
el25.click()
el26 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[10]/android.view.View")
el26.click()
el27 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView")
el27.click()
el27.click()
el28 = driver.find_element_by_id("com.chint.cloud.industry:id/tv_true")
el28.click()
el29 = driver.find_element_by_id("com.chint.cloud.industry:id/btn")
el29.click()
el30 = driver.find_element_by_id("com.chint.cloud.industry:id/view1")
el30.click()
el31 = driver.find_element_by_id("com.chint.cloud.industry:id/tv_all")
el31.click()
el32 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView")
el32.click()
el32.click()
