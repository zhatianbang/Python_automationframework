# coding:utf-8
from selenium.webdriver.common.by import By
from APP_PO.base.base import Base

class Login_page(Base):

    # 首次页面的登陆
    登陆or注册 = (By.ID, "com.tencent.mobileqq:id/btn_login")
    def login_btn_click(self):
        self.click(self.登陆or注册)

    # 用户名
    用户名 = (By.XPATH, '//*[@content-desc="请输入QQ号码或手机或邮箱"]')
    def user_input(self,username="120517972"):
        self.send_key(self.用户名,username)

    # 密码
    密码 = (By.XPATH, '//*[@content-desc="密码 安全"]')
    def password_input(self,password="12345"):
        self.send_key(self.密码,password)


    def enter_home(self,username='120517972',password='123456'):
        self.login_btn_click()
        self.user_input(username)
        self.password_input(password)