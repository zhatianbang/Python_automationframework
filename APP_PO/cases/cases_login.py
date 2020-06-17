# coding:utf-8

from APP_PO.base.base import Base
import unittest
from APP_PO.common.read_yaml import get_device_info
from APP_PO.common.server import *
from APP_PO.page.进入主页并登陆 import Login_page


class TestLogin(unittest.TestCase):



    @classmethod
    def setUpClass(cls) -> None:
        devices_name ="逍遥"
        yaml_name = "qq.yaml"

        device_info = get_device_info(devices_name,yaml_name)
        # 启动设备
        start_simulator()
        adb_connect_device(device_name=device_info["desired_caps"]["deviceName"])
        start_appium(port=device_info["port"],udid=device_info["desired_caps"]["udid"])
        cls.driver = run_app(port=device_info["port"],desired_caps=device_info["desired_caps"])
        time.sleep(10)

    def test_001(self):
        login = Login_page(self.driver)
        login.login_btn_click()
        login.user_input()
        login.password_input()



    def tearDown(self) -> None:
        pass