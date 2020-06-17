# coding=utf-8
from appium import webdriver
import time
import yaml
import os
from common.logger import logger

#　根据设备名字读取设备信息
def get_device_info(devicesName,yaml_name="qq.yaml"):
    logger.info("read_yaml中的参数：%s"%devicesName)
    '''
    从yaml读取desired_caps配置信息
    参数name:设备名称,如：夜神/雷电
    :return: desired_caps字典格式 和port
    '''

    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    yamlpath = os.path.join(os.path.join(path, "configs"),yaml_name)
    # print("配置地址：%s" % yamlpath)
    try:
        logger.info("配置地址：%s" % yamlpath)
        f = open(yamlpath, "r", encoding="utf-8")
        a = f.read()
        f.close()
        # 把yaml文件转字典
        d = yaml.load(a,Loader=yaml.FullLoader)
        for i in d:
            if devicesName in i["desc"]:
                logger.info(i)
                return i
    except FileNotFoundError:
        logger.error("找不到文件%s"%yamlpath)

if __name__ == '__main__':
    print(get_device_info())
    s =get_device_info()["desired_caps"]
    print(s)

    s = " {'platformName': 'Android', 'platformVersion': '7.1.2', 'deviceName': '127.0.0.1:21503', 'appPackage': 'com.tencent.mobileqq', 'appActivity': '.activity.LoginActivity', 'noReset': True, 'udid': '127.0.0.1:21503'}"
    print(type(s))
    ele =eval(s)
    print(type(ele))