# coding:utf8
from appium import webdriver
from common import logger
import traceback, time, os, threading
from appium.webdriver.common.touch_action import TouchAction

class APP():
    """
    这是APP自动化的关键字
    """

    def __init__(self, writer):
        self.driver = None
        self.t = 20
        self.port = '4723'
        self.writer = writer

    # 执行cmd命令
    def runcmd(self,cmd,t=""):
        try:
            if t == "":
                t = 10

            def run(cmd):
                try:
                    os.popen(cmd).read()
                except Exception as e:
                    logger.error(traceback.format_exc())
            th = threading.Thread(target=run, args=(cmd,))
            th.start()
            time.sleep(int(float(t)))
            logger.info("执行cmd " + cmd + " 成功")
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            logger.error("执行cmd " + cmd + " 失败")
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    # 根据端口号kill掉对用进程
    def kill_port(self,port):
        '''
        根据端口号杀死对应进程，循环10次
        :param port:
        :return:
        '''
        for i in range(10):
            find_port = 'netstat -aon | findstr :%s' % port
            result = os.popen(find_port)
            text = result.read()
            pid = text[-5:-1]
            if len(pid) > 0 & len(pid) <= 6:
                # print("pid是: %s"%pid)
                find_kill = 'taskkill -f -pid %s' % pid
                result = os.popen(find_kill)
                logger.info(result.read())

    # cmd kill应用程序
    def cmdkill(self,pro_name):
        """
        cmd通过进程名字杀进程
        :param pro_name:  进程名
        :return:
        """
        cmd = "taskkill /F /IM %s" %pro_name
        try:
            os.popen('%s' %cmd)
            logger.info("执行cmd " + cmd + " 成功")
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            logger.error("执行cmd " + cmd + " 失败")
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def runappium(self, path='', port='', t=''):
        '''
        启动appium服务
        :param path: 桌面版appium的安装路径,如C:\\Users\\Administrator\\AppData\\Local\\Programs\\Appium
        :param port: appium服务的启动端口
        :param t: appium启动等待时间
        :return:
        '''
        logger.info(path)
        try:
            if path == '':
                cmd = 'node D:\\installation\\node-v12.15.0-win-x64\\node_modules\\appium\\build\\lib\\main.js'
            else:
                cmd = 'node ' + path + '\\resources\\app\\node_modules\\appium\\build\\lib\\main.js'
                logger.info(cmd)
            if port == '':
                cmd += ' -p ' + self.port
            else:
                self.port = port
                cmd += ' -p ' + self.port
            if t == '':
                t = 5

            self.kill_port(self.port) # 杀死被占用端口

            # 启动appium服务
            def run(cmd):
                try:
                    os.popen(cmd).read()
                except Exception as e:
                    pass

            th = threading.Thread(target=run, args=(cmd,))
            th.start()
            time.sleep(int(float(t)))
            logger.info("启动appium成功 %s"%cmd )
            self.writer.write(self.writer.row, 7, "PASS")
            self.writer.write(self.writer.row, 8, "")
        except Exception as e:
            logger.error("启动appium失败 %s"%cmd)
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def runapp(self, caps, t=''):
        """
        连接appium服务器，并根据conf配置，启用待测试app
        :param conf: APP的启动配置，格式尽量为json格式字符串（尽量所有的值都用字符串，少用布尔值等其他格式）
        :return:
        """
        try:
            caps = eval(caps)
            if t == '':
                t = 20
            else:
                t = int(t)
            self.driver = webdriver.Remote("http://localhost:" + self.port + "/wd/hub", caps)
            self.driver.implicitly_wait(t)
            logger.info("启动APP成功 %s"%caps)
            self.writer.write(self.writer.row, 7, "PASS")
            self.writer.write(self.writer.row, 8, "")
        except Exception as e:
            logger.error("启动APP失败 %s"%caps)
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))




    def __findele(self, path):
        """
        定位元素
        :param path:元素的定位路径，支持id,xpath, accessibility_id
        :return: 找到的元素，如未找到就返回None
        """
        ele = None
        try:
            if path.startswith("/"):
                # xpath定位
                ele = self.driver.find_element_by_xpath(path)
            # elif path.find(":id/")>0:  # 这种特殊情况下会有误判的可能
            else:
                try:
                    # 优先accessibility_id定位
                    self.driver.implicitly_wait(5)
                    ele = self.driver.find_element_by_accessibility_id(path)
                except:
                    # 其次id定位
                    # logger.error(str(traceback.format_exc()))
                    self.driver.implicitly_wait(self.t)
                    ele = self.driver.find_element_by_id(path)
        except Exception as e:
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
        return ele

    def click(self, path):
        ele = self.__findele(path)
        if ele is None:
            logger.error("No such element:" + path)
            self.writer.write(self.writer.row, 7, "FAIL")
        else:
            try:
                ele.click()
                logger.info("点击元素【" + path + "】成功")
                self.writer.write(self.writer.row, 7, "PASS")
            except Exception as e:
                logger.error("点击元素【" + path + "】失败")
                logger.error(traceback.format_exc())
                self.writer.write(self.writer.row, 7, "FAIL")
                self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def clear(self, path):
        ele = self.__findele(path)
        if ele is None:
            logger.error("No such element:" + path)
        else:
            try:
                ele.clear()
                logger.info("清除【" + path + "】成功")
                self.writer.write(self.writer.row, 7, "PASS")
            except Exception as e:
                logger.error("点击【" + path + "】失败")
                logger.error(traceback.format_exc())
                self.writer.write(self.writer.row, 7, "FAIL")
                self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def input(self, path, text):
        ele = self.__findele(path)
        if ele is None:
            logger.error("No such element:" + path)
        else:
            try:
                ele.clear()
                ele.send_keys(text)
                logger.info("向【" + path + "】"+"输入【" + text + "】成功")
                self.writer.write(self.writer.row, 7, "PASS")
            except Exception as e:
                logger.error("向【" + path + "】"+"输入【" + text + "】失败")
                logger.error(traceback.format_exc())
                self.writer.write(self.writer.row, 7, "FAIL")
                self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def send_keys(self, xpath, index, text):
        try:
            ele = self.__findele(xpath)[index]
            ele.clear()
            ele.send_keys(text)
            time.sleep(1)
            logger.info("向【" + xpath + "】" + "输入【" + text + "】成功")
            self.writer.write(self.writer.row, 7, "PASS")
        except AttributeError:
            logger.error("向【" + xpath + "】" + "输入【" + text + "】失败")
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))


    def closeappium(self):
        try:
            s = os.system('taskkill /F /IM node.exe')
            time.sleep(3)
            logger.info("执行关闭appium：taskkill /F /IM node.exe 成功 %s"%s)
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            logger.error("执行关闭appium：taskkill /F /IM node.exe 失败")
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def sleep(self,t=3):
        try:
            tim = int(float(t))
            time.sleep(tim)
            logger.info("等待【" + str(t) + "】秒成功" )
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            logger.info("等待【" + str(t) + "】秒失败" )
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    # 关闭页面退出驱动（driver生命结束），关闭页面是关闭页面在前台显示，手动打开app，可能还处在操作界面
    def quit(self):
        '''关闭页面退出驱动，结束driver的生命'''
        try:
            self.driver.quit()
            logger.info("关闭页面退出驱动成功")
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            logger.info("关闭页面退出驱动失败")
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def getsize(self):
        self.driver.get_window_size()

    def swipeup(self, n=1):
        '''定义向上滑动'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = width * 0.5
        y1 = height * 0.8
        y2 = height * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2)

    def swipedown(self, n=1):
        '''定义向下滑动'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = width * 0.5
        y1 = height * 0.25
        y2 = height * 0.9
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2)

    def swipeleft(self, n=1):
        '''定义向左滑动'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = width * 0.8
        x2 = width * 0.2
        y1 = height * 0.5
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1)

    def swiperight(self, n=1):
        '''定义向右滑动'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = width * 0.2
        x2 = width * 0.8
        y1 = height * 0.5
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1)

    """TouchAction封装、暂时发现对部分元素容易出问题（如对微信，虽然实现了滑动，但是同时出现了长按导致出现【标记未读、置顶聊天、删除该聊天】这个小弹窗的问题，而swipe则较少出现这个问题）"""

    def touchdown(self):
        """向下滑动"""
        try:
            size = self.driver.get_window_size()
            width = size['width'] * 0.5
            height = size['height']
            TouchAction(self.driver).press(x=width, y=height * 0.2).move_to(x=width, y=height * 0.8).release().perform()
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def touchup(self):
        """向上滑动"""
        try:
            size = self.driver.get_window_size()
            width = size['width'] * 0.5
            height = size['height']
            TouchAction(self.driver).press(x=width, y=height * 0.8).move_to(x=width, y=height * 0.2).release().perform()
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def touchleft(self):
        """向左滑动"""
        try:
            size = self.driver.get_window_size()
            width = size['width']
            height = size['height'] * 0.5
            TouchAction(self.driver).press(x=width * 0.8, y=height).move_to(x=width * 0.2, y=height).release().perform()
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def touchright(self):
        """向右滑动一次"""
        try:
            size = self.driver.get_window_size()
            width = size['width']
            height = size['height'] * 0.5
            TouchAction(self.driver).press(x=width * 0.2, y=height).move_to(x=width * 0.8, y=height).release().perform()
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    # 解锁九宫格，需要传递解锁需要的几个点，根据具体用例封装
    def unloccell(self,path):
        """解锁九宫格"""
        ele = self.__findele(path)
        x = ele.location.get('x')  # 九宫格左上角点的x轴坐标
        y = ele.location.get('y')  # 九宫格左上角点的y轴坐标
        width = ele.size.get('width')   # 九宫格的宽度
        height = ele.size.get('height') # 九宫格的高度
        offset = width / 6  # 偏移量，每次移动的距离

        # 九宫格9个元素的坐标
        p11 = int(x + width / 6), int(y + height / 6)
        p12 = int(x + width / 2), int(y + height / 6)
        p13 = int(x + width - offset), int(y + height / 6)
        p21 = int(x + width / 6), int(y + height / 2)
        p22 = int(x + width / 2), int(y + height / 2)
        p23 = int(x + width - offset), int(y + height / 2)
        p31 = int(x + width / 6), int(y + height - offset)
        p32 = int(x + width / 2), int(y + height - offset)
        p33 = int(x + width - offset), int(y + height - offset)
        TouchAction(self.driver).press(x=p11[0],y=p11[1]).wait(10)\
        .move_to(x=p12[0],y=p12[1]).wait(10)\
        .move_to(x=p13[0],y=p13[1]).wait(10)\
        .move_to(x=p22[0],y=p22[1]).wait(10)\
        .move_to(x=p32[0],y=p32[1]).wait(10)\
        .move_to(x=p21[0],y=p21[1]).wait(10).release().perform()
        """未完，后续根据具体用例具体补充"""

    # 启动其他app
    def startactivity(self,app_package,app_activity):
        """
        启动某个app
        :param app_package:  待启动app的app_package
        :param app_activity: 待启动app的app_activity
        :return:
        """
        try:
            # 两种方式启动app
            try:
                self.driver.start_activity(app_package, app_activity)
                self.writer.write(self.writer.row, 7, "PASS")
            except :
                code = "adb shell am start –n %s/%s"%(app_package, app_activity)
                os.system(code)
                self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))


    # adb按键事件
    def adbkeycode(self,keycode):
        """
        adb 按键码事件
        :param keycode: 按键码
        :return:
        """
        code = "adb shell input keyevent %s"%keycode
        os.system(code)

    # adb输入不支持中文
    def adbinput(self,text):
        code = "adb shell input text %s"%text
        os.system(code)

    # adb 的tap
    def adbtap(self,x,y):
        """
        adb的tap事件
        :param x: x轴坐标int型
        :param y: y轴坐标int型
        :return:
        """
        x1 = int(float(x))
        y1 = int(float(y))
        code = "adb shell input tap %s %s"%(x1,y1)
        os.system(code)

    # adb 的swipe
    def adbswipe(self,x1,y1,x2,y2):
        """adb 滑动"""
        code = "adb shell input "
        """未写完，后续补充"""


    # 发送按键码（安卓仅有），按键码可以上网址中找到
    def  presskeycode(self,key):
        """
        发送按键码
        :param key: 按键码，1、2、3...
        :return:
        """
        try:
            try:
                self.driver.press_keycode(key)
                self.writer.write(self.writer.row, 7, "PASS")
            except:
                # 两者好像效果一样
                self.driver.keyevent(key)
                self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            logger.error("执行按键码失败! %s"%key)
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    #  切换输入法
    def resetinput(self,engine):
        """切换输入法
        :param engine 待切换的输入
        """
        try:
            if engine =="" or engine is None:
                # 如果未传输入法，切换到下面默认的输入法
                engine = "com.baidu.input_huawei/.ImeService"
                self.driver.activate_ime_engine(engine)
                self.writer.write(self.writer.row, 7, "PASS")
                logger.info("切换输入法成功 %s"%engine)
            else:
                self.driver.activate_ime_engine(engine)
                self.writer.write(self.writer.row, 7, "PASS")
                logger.info("切换输入法成功 %s" % engine)
        except Exception as e:
            logger.error("切换输入法失败！ %s"%engine)
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    # 后台运行app指定时间
    def background_app(self,time):
        """
        后台运行app time秒，time秒后自动切回
        :param time: 单位秒
        :return:
        """
        try:
            self.driver.background_app(time)
            self.writer.write(self.writer.row, 7, "PASS")
            logger.info("后台运行app %s 秒成功！"%time)
        except Exception as e:
            logger.error("后台运行 %s 秒失败!"%time)
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    # 返回上一页
    def back(self):
        """返回上一页"""
        try:
            self.driver.back()
            self.writer.write(self.writer.row, 7, "PASS")
            logger.info("返回上一页成功")
        except Exception as e:
            logger.error("返回上一页失败！")
            logger.error(traceback.format_exc())
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    # 等待activity出现，超时时间5s，循环查询时间1秒
    def wait_activity(self,activity,time=5,interv=1):
        """
        等待activity出现，超时时间5s，循环查询时间1秒
        :param time: 超时时间
        :param interv: 循环查询时间
        :return:
        """
        if time == "" or time is None:
            timeout = 5
        else:
            timeout = int(float(time))
        if interv == "" or interv is None:
            interval = 1
        else:
            interval = int(float(interv))
        try:
            self.driver.wait_activity(activity,timeout,interval)
            self.writer.write(self.writer.row, 7, "PASS")
            logger.info("等待activity成功！ %s"%activity)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.error("等待activity失败！ %s"%activity)
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))


    # 保存源码到本地
    def savepagesource(self):
        p = self.driver.page_source
        with open("ppp.html", "wb") as f:
            f.write(p.encode('utf-8'))
    # def resetinput(self):
    #     '''重置手机输入法'''
    #     try:
    #         def swipe_up(n=1):
    #             '''定义向上滑动'''
    #             size = driver.get_window_size()
    #             width = size['width']
    #             height = size['height']
    #             x1 = width * 0.5
    #             y1 = height * 0.9
    #             y2 = height * 0.25
    #             for i in range(n):
    #                 driver.swipe(x1, y1, x1, y2)
    #
    #         caps = {}
    #         caps["platformName"] = "Android"
    #         caps["platformVersion"] = "8.0.0"
    #         caps["deviceName"] = "KWG5T16C29081222"
    #         caps["appPackage"] = "com.android.settings"
    #         caps["appActivity"] = ".HWSettings"
    #         caps["noReset"] = "true"
    #         # caps["unicodeKeyboard"] = "true"
    #         # caps["resetKeyboard"] = "true"
    #         driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    #         driver.implicitly_wait(10)
    #         swipe_up()
    #         try:
    #             driver.find_element_by_xpath('//*[contains(@text,"系统导航、系统更新、关于手机、语言和输入法")]').click()
    #         except:
    #             swipe_up()
    #             driver.find_element_by_xpath('//*[contains(@text,"系统导航、系统更新、关于手机、语言和输入法")]').click()
    #         time.sleep(1)
    #         driver.find_element_by_xpath('//*[contains(@text,"语言和输入法")]').click()
    #         time.sleep(1)
    #         driver.find_element_by_xpath('//*[contains(@text,"默认")]').click()
    #         time.sleep(1)
    #         driver.find_element_by_xpath('//*[contains(@text,"百度输入法华为版")]').click()
    #         time.sleep(1)
    #         driver.quit()
    #         self.writer.write(self.writer.row, 7, "PASS")
    #     except Exception as e:
    #         self.writer.write(self.writer.row, 7, "FAIL")
    #         self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
