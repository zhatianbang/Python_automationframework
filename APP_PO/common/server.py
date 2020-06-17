# coding:utf-8
import os
import time
from APP_PO.common.read_yaml import *
from common.logger import logger
import threading
import traceback
import os
import socket
import urllib.request
from urllib.error import URLError
from multiprocessing import Process
import time
import platform
import subprocess
import threading

def start_simulator(simulator_name="逍遥"):
    if simulator_name == "逍遥":
        path = r"D:\Program Files\Microvirt\MEmu\MEmu.exe"
        os.system("taskkill /f /im MEmuHeadless.exe")
        os.system("taskkill /f /im MEmuSVC.exe")
        os.system("taskkill /f /im MEmu.exe")
        os.system("taskkill /f /im MemuService.exe")
        run_cmd(path,t="20")
        return
    if simulator_name =="MuMu":
        path = r"C:\Program Files (x86)\MuMu\emulator\nemu\EmulatorShell\NemuPlayer.exe"
        os.system("taskkill /f /im NemuSVC.exe")
        os.system("taskkill /f /im NemuPlayer.exe")
        run_cmd(path,t="20")
        return
    else:
        logger.error("未找到对应设备%s"%simulator_name)



def start_appium(port='', udid='', t=''):
    '''
    启动appium服务
    :param path: 桌面版appium的安装路径,如C:\\Users\\Administrator\\AppData\\Local\\Programs\\Appium
    :param port: appium服务的启动端口
    :param t: appium启动等待时间
    :return:
    '''
    appium_log_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) +"/log/" +"appium_" + str(port) + ".log"

    if t=="" or t is None:
        t = 5
    cmd_appium = "appium -a 127.0.0.1 -p %s -U %s --log %s --no-reset" % (port, udid,appium_log_path)
    print(cmd_appium)
    try:
        kill_port(port)
        # 启动appium服务
        def run(cmd):
            try:
                os.popen(cmd).read()
            except Exception as e:
                pass
        th = threading.Thread(target=run, args=(cmd_appium,))
        th.start()
        time.sleep(int(float(t)))
        while True:
            print("--------开始启动appium-------------")
            if server_is_running("http://127.0.0.1:" + str(port) + "/wd/hub" + "/status"):
                print("--------appium服务 成功--------------")
                break
    except Exception as e:
        logger.error("启动appium失败 %s" % cmd_appium)
        logger.error(traceback.format_exc())

def run_app(port,desired_caps):
    """
    :param port:
    :param desired_caps:
    :return:
    """
    # 执行代码
    driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' % port, desired_caps)
    time.sleep(10)
    return driver

def stop_appium():
    result = os.popen("tasklist |findstr node")
    if len(result.readlines()) > 0:
        os.popen("taskkill /F /IM node.exe")
        logger.info("已执行taskkill /F /IM node.exe")




def adb_connect_device(device_name):
    """
    adb连接设备
    :param device_name: 如127.0.0.1:7555
    :return:
    """
    try:
        os.system("adb kill-server")
        os.system("adb start-server")
        os.system("adb devcies")
        time.sleep(2)
        result = os.popen("adb connect %s"%device_name)
        result = result.readlines()
        if len(result) > 0:
            for i in result:
                if "connected to " + device_name in i:
                    logger.info("adb连接设备成功")
                    return
        else:
            logger.error("adb连接设备失败")
            logger.error(result)
        print(result)
    except Exception:
        logger.error(traceback.format_exc())

def kill_port(port):
    """根据端口号杀死对应的进程"""
    # 根据端口号查询pid
    find_port = 'netstat -aon | findstr %s' % port
    # 执行cmd命令 返回对象
    result = os.popen(find_port)
    # 读取返回结果
    text = result.read()
    print(f'端口:{port}占用情况：')
    print(text)
    # 提取pid
    text = [i.split(' ') for i in text.split('\n') if i]
    pids = []
    for i in text:
        pid = [u for u in i if u]
        if str(port) in pid[1]:
            pids.append(pid[-1])
    pids = list(set(pids))
    # 杀死占用端口的pid
    for pid in pids:
        find_kill = 'taskkill -f -pid %s' % pid
        result = os.popen(find_kill)
        # print(result.read())
        logger.info(result.read())

def run_cmd(cmd_command, t=""):
    if t == "":
        t = 10
    try:
        def run(cmd_command):
            try:
                os.popen(cmd_command).read()
            except Exception:
                logger.error(traceback.format_exc())
        th = threading.Thread(target=run, args=(cmd_command,))
        th.start()
        time.sleep(int(float(t)))
        logger.info("已执行cmd " + cmd_command )
    except Exception:
        logger.error("执行cmd " + cmd_command + " 失败")


def server_is_running(url):
    """
    Determine whether server is running
    :param url: http://127.0.0.1:4724/wd/hub/status
    :return: True or False
    """
    response = None
    time.sleep(1)
    try:
        response = urllib.request.urlopen(url, timeout=5)
        if str(response.getcode()).startswith("2"):
            return True
        else:
            return False
    except URLError:
        return False
    except socket.timeout:
        return False
    finally:
        if response:
            response.close()


def set_up(device_name_desc,yaml_file):
    logger.info("参数是：%s %s"%(device_name_desc,yaml_file))

    device_info = get_device_info(devicesName=device_name_desc,yaml_name=yaml_file)    # 获取设备信息

    start_simulator(simulator_name=device_name_desc)    # 启动模拟器

    adb_connect_device(device_info["desired_caps"]["deviceName"])   # adb连接设备

    start_appium(port=device_info["port"],udid=device_info["desired_caps"]["udid"]) # 启动appium

    run_app(port=device_info["port"],desired_caps=device_info["desired_caps"])  # 运行app
    # driver.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()
    # driver.find_element_by_xpath('//*[@content-desc="请输入QQ号码或手机或邮箱"]').send_keys("120517972")
    # driver.find_element_by_xpath('//*[@content-desc="密码 安全"]').send_keys('123456')

    stop_appium()   # 停止appium

if __name__ == '__main__':
    # adb_connect_device("127.0.0.1:21503")
    # kill_port(4723)
    # start_simulator(simulator_name="逍遥")
    # adb_connect_device(get_device_info("逍遥")["desired_caps"]["deviceName"])
    # from common.basic_page import Basic_page
    # driver = set_up("逍遥")
    # b  = Basic_page(driver)
    # b.swipe_direction(direction="left",times=3)
    # list =['逍遥',""]
    # driver = set_up("逍遥",yaml_file="waiqin_caps.yaml")
    logger.info("开始")
    t1 = threading.Thread(target=set_up,args=("逍遥","qq.yaml"))
    t2 = threading.Thread(target=set_up,args=("MuMu","qq.yaml"))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    logger.info("结束")



    # # 测试启动appium
    # port ='4723'
    # udid = "127.0.0.1:21503"
    # adb_connect_device(udid)
    # kill_port(port)
    # start_appium(port=port,udid=udid)