from appium import webdriver
import time


#pack='com.ss.android.article.news'
#activity='com.ss.android.article.news.activity.SplashActivity'
#PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:21503'
desired_caps['platformVersion']  = '7.1.2'
desired_caps['sessionOverride'] = True  #允许session被覆盖（冲突的话），默认是FALSE
#desired_caps['newCommandTimeout'] = 600    #一段时间不输入命令的话，app会退出，这个参数用来设置超时时间
#desired_caps['autoAcceptAlerts'] = True    #IOS的个人信息访问警告出现时，自动选择接受
desired_caps['appPackage'] = 'com.tencent.mobileqq'
desired_caps['appActivity'] = '.activity.LoginActivity'
desired_caps['noRest'] = True   #不要在会话前重置应用状态，默认flase
desired_caps['unicodekeyboard'] = True  #设置appium输入法后就不会弹出默认的系统输入法了
desired_caps['resetKeyboard'] = True    #重置系统输入法

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
time.sleep(10)

size = driver.get_window_size()
print(size)
print(size["height"])
print(size["width"])


print ('1')
driver.find_element_by_id("com.tencent.mobileqq:id/btn_login").click()

time.sleep(1)
# driver.find_element_by_xpath('//*[@content-desc="请输入QQ号码或手机或邮箱"]').send_keys("120517912")

from app_po.basic_page import Basic_page
b = Basic_page(driver)
loc =("xpath",'//*[@content-desc="请输入QQ号码或手机或邮箱"]')
# b.send_key(loc,"120517972")
b.driver.find_element_by_xpath('//*[@content-desc="请输入QQ号码或手机或邮箱"]').send_keys("120517912")


# driver.find_element_by_accessibility_id(u'热点').click()
# print ('2')
#
# driver.find_element_by_accessibility_id(u'上海').click()
# time.sleep(5)
# print ('3')
# driver.find_element_by_accessibility_id(u'娱乐').click()
# print ('4')
#
# driver.find_element_by_accessibility_id(u'推荐').click()
# time.sleep(5)
# print(driver.contexts) #获取当前所有可用上下文，不需要参数和()
# print(driver.current_context)  #获取当前可用的上下文，不需要（）和参数



# driver.find_element_by_id('com.ss.android.article.news:id/auh').click()
# time.sleep(5)
# driver.swipe(int(width*0.5),int(height*0.75),int(width*0.5),int(height*0.25),600) #向下滑动
# time.sleep(5)
# driver.swipe(int(width*0.5),int(height*0.25),int(width*0.5),int(height*0.75),600) #向上滑动
# driver.swipe(int(width*0.25),int(height*0.25),int(width*0.75),int(height*0.25),600)    #从左向右滑动
# time.sleep(5)
# driver.swipe(int(width*0.75),int(height*0.25),int(width*0.25),int(height*0.25),600) #从右向左滑动
# time.sleep(5)
# driver.remove_app('com.android.chrome')     #卸载app,如无app,不会报错
# print (u'5s后开始安装app')
# time.sleep(5)
#
# #driver.install_app('C:\Users\Ronnie\Desktop\appium\Chrome.apk')    #安装app
# print (driver.is_app_installed('com.zhaopin.social')) #检查app是否已经安装)
# driver.launch_app('com.zhaopin.social',)     #启动app
# time.sleep(5)
# driver.background_app('com.zhaopin.social') #将app置于后台
# time.sleep(5)
# driver.launch_app('com.zhaopin.social')     #将应用启动
# print ('5秒后将应用置于后台10')
# time.sleep(5)
# driver.background_app(10)
# time.sleep(5)
#
# driver.close_app()  #关闭当前打开的应用，不需要
#
#
#
# driver.open_notifications()
# time.sleep(5)