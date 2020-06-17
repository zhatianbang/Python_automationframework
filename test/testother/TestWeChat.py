# coding:utf8
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

caps = {"platformName": "Android",
        "platformVersion": "8.0.0",
        "deviceName": "KWG5T16C29081222",
        "appPackage": "com.tencent.mm",
        "appActivity": ".ui.LauncherUI",
        "noReset": "true",
        "unicodeKeyboard": "true",
        "resetKeyboard": "true",
        "chromeOptions": {"androidProcess": "com.tencent.mm:tools"}
        }


# caps["platformName"] = "Android"
# caps["platformVersion"] = "8.0.0"
# caps["deviceName"] = "KWG5T16C29081222"
# caps["appPackage"] = "com.tencent.mm"
# caps["appActivity"] = ".ui.LauncherUI"
# caps["noReset"] = "true"
# caps["unicodeKeyboard"] = "true"
# caps["resetKeyboard"] = "true"  #
# caps["chromeOptions"] ="{'androidProcess': 'com.tencent.mm:tools'}"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

# # 添加隐式等待
driver.implicitly_wait(10)
#
# # el1 = driver.find_element_by_accessibility_id("微信")
# # el1.click()
try:
    el2 = driver.find_element_by_id("com.tencent.mm:id/m6")
    el2.send_keys("12345")
    el3 = driver.find_element_by_id("com.tencent.mm:id/d0q")
    el3.click()
except:
    pass
# time.sleep(5)
print("等待5秒结束")
#
# # 我
# # driver.find_element_by_id("com.tencent.mm:id/djv").click()
driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/djv' and @text='我']").click()

#支付


driver.find_element_by_xpath("//*[@text='支付']").click()

#########------------------------- 九宫格解锁  开始-------------------------
# 定位九宫格元素
def unlock():
    lock_pattern = driver.find_element_by_id("com.tencent.mm:id/cs3")

    #获取九宫格的X，Y坐标
    x=lock_pattern.location.get('x')    # 九宫格左上角点的x轴坐标
    y=lock_pattern.location.get('y')    # 九宫格左上角点的y轴坐标

    # 获取View的宽度和高度
    width=lock_pattern.size.get('width')
    height=lock_pattern.size.get('height')

    #偏移量
    offset=width/6
    #计算每个点的位置
    p11=int(x+width/6),int(y+height/6)
    # print(p11)
    p12=int(x+width/2),int(y+height/6)
    p13=int(x+width-offset),int(y+height/6)
    p21=int(x+width/6),int(y+height/2)
    p22=int(x+width/2),int(y+height/2)
    p23=int(x+width-offset),int(y+height/2)
    p31=int(x+width/6),int(y+height-offset)
    p32=int(x+width/2),int(y+height-offset)
    p33=int(x+width-offset),int(y+height-offset)
    #这里需要两次绘制手势才能进行保存
    for i in range(1):
        TouchAction(driver).press(x=p11[0],y=p11[1]).wait(10)\
        .move_to(x=p12[0],y=p12[1]).wait(10)\
        .move_to(x=p13[0],y=p13[1]).wait(10)\
        .move_to(x=p22[0],y=p22[1]).wait(10)\
        .move_to(x=p32[0],y=p32[1]).wait(10)\
        .move_to(x=p21[0],y=p21[1]).wait(10).release().perform()
unlock()
#########------------------------- 九宫格解锁  结束-------------------------

# 支付（返回）
time.sleep(2)
# driver.find_element_by_xpath("//*[@content-desc='返回']").click()



#########------------------------- swipe滑动屏幕 开始-------------------------
print("开始滑动屏幕")
time.sleep(2)
size = driver.get_window_size()
x = size["width"]
y = size["height"]
for i in range(2):
    driver.swipe(x*0.5,y*0.8,x*0.5,y*0.2,duration=1000)
#
#########------------------------- swipe滑动开始 结束-------------------------

for i in range(8):
    driver.keyevent(24) # 增加音量
for i in range(5):
    driver.press_keycode(25) # 减小音量 同上
# # 后台运行app 2秒
print("后台运行app10秒")
driver.background_app(2)


# 点击美团外卖
print("当前上下文：%s"%(driver.current_context))
driver.find_element_by_xpath("//*[@text='美团外卖']").click()


#########------------------------- webview 切换  开始-------------------------
# time.sleep(5) # 等待切换到webview
# print("所有上下文:%s"%(driver.contexts))
#
# # 切换到"WEBVIEW_com.tencent.mm:tools"
#
# driver.switch_to.context("WEBVIEW_com.tencent.mm:tools")
# # 验证切换成功
# print("当前上下文：%s"%(driver.current_context))
#########------------------------- webview 切换  结束-------------------------
# 上面的webview切换完成，就可以任意selenium飞了

#########------------------------- 小程序不需要切换-------------------------

driver.find_element_by_xpath("//*[@text='美食']/..").click()
time.sleep(1)


driver.find_element_by_xpath("//*[@text='请输入商家或商品名称']").click()

# driver.find_element_by_xpath("//*[@text='请输入商家或商品名称']").send_keys("煲仔饭")
ele = driver.find_elements_by_xpath("//*[@text='请输入商家或商品名称']")
try:
    print("个数%s"%len(ele))
    ele[0].send_keys("煲仔饭")
except:
    ele[1].send_keys("水饺")


print("等待600s")
time.sleep(60)


# # # 设置
# # # driver.find_element_by_id("com.tencent.mm:id/dkm").click()
# # driver.find_element_by_xpath("//*[@resource-id='android:id/title' and @text='设置']").click()
# #
# # # 向上滑动
# # time.sleep(1)
# # size = driver.get_window_size()
# # x = size['width']
# # y = size['height']
# # print("屏幕尺寸", x, y)
# #
# # # 获取屏幕尺寸
# # x1 = int(x * 0.5)
# # y1 = int(y * 0.9)
# # y2 = int(x * 0.1)
# # driver.swipe(x1, y1, x1, y2, 500)
# #
# # # 点击 退出
# # driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/d8' and @text='退出']").click()
# #
# # # 点击 退出登录
# # # driver.find_element_by_id("com.tencent.mm:id/mf").click()
# # time.sleep(1)
# # driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/dc' and @text='退出登录']").click()
# #
# # # 确认 退出
# # driver.find_element_by_id("com.tencent.mm:id/b47").click()
# #
# # time.sleep(5)
# # # 退出app
# # driver.quit()

#########------------------------- 切换输入法 开始-------------------------
# # 获取当前可用输入
# s = driver.available_ime_engines
# print(s)
# # 切换回百度输入法华为版
# # driver.activate_ime_engine("io.appium.settings/.AppiumIME") # appium自带的输入法
driver.activate_ime_engine("com.baidu.input_huawei/.ImeService")  # 切换回百度输入法华为版
#########------------------------- 切换输入法 结束-------------------------


# 退出app及其关联的
driver.quit()