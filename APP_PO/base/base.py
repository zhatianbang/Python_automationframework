from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import time
from common.logger import logger
from APP_PO.common.swipe_method import Swipe_Method


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        # self.log = Log(self)
        # 获取当前手机屏幕大小X,Y
        # self.X = self.driver.get_window_size()['width']
        # self.Y = self.driver.get_window_size()['height']


    def find_element(self, *loc):
        try:
            # 元素可见时，返回查找到的元素；以下入参为元组的元素，需要加*
            WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            logger.warning('Can not find element: %s' % loc[1])
            logger.error('Can not find element: %s' % loc[1])
            raise
        except TimeoutException:
            logger.error('Can not find element: %s' % loc[1])
            raise

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 30).until(lambda driver: driver.find_elements(*loc))
            return self.driver.find_elements(*loc)
        except NoSuchElementException:
            logger.warning('Can not find element: %s' % loc[1])
            self.get_screenshot()
            raise

    def click(self, loc):
        logger.info('Click element by %s: %s...' % (loc[0], loc[1]))
        try:
            self.find_element(*loc).click()
            time.sleep(2)
        except AttributeError:
            raise

    def double_click(self, loc):
        logger.info('Click element by %s: %s...' % (loc[0], loc[1]))
        try:
            self.find_element(*loc).click()
            self.find_element(*loc).click()
        except AttributeError:
            raise

    def clicks(self, loc, index):
        logger.info('Click element by %s: %s...' % (loc[0], loc[1]))
        try:
            self.find_elements(*loc)[index].click()
            time.sleep(2)
        except AttributeError:
            raise

    def click_back_key(self):
        logger.info('Click device back key...')
        self.driver.keyevent(4)
        time.sleep(1)

    def send_key(self, loc, text):
        try:
            logger.info('Clear input-box: %s...' % loc[1])
            self.find_element(*loc).clear()
            time.sleep(1)
            logger.info('Input: %s' % text)
            self.find_element(*loc).send_keys(text)
            self.hide_keyboard()
            time.sleep(2)
        except TimeoutException:
            raise
        except Exception:
            pass

    def send_keys(self, loc, index, text):
        try:
            logger.info('Clear input-box: %s...' % loc[1])
            self.find_elements(*loc)[index].clear()
            time.sleep(1)

            logger.info('Input: %s' % text)
            self.find_elements(*loc)[index].send_keys(text)
            time.sleep(2)
        except AttributeError:
            raise

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def is_display(self, loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return True
        except:
            return False

    # 获取屏幕的高度和宽度
    def get_windowsize(self):
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        return height, width

    # 滑动屏幕
    def swipe_direction(self,direction,times):
        if times == "" or time is None:
            times = 2
        else:
            times = int(times) + 1
        for i in range(1,times):
            if direction == "left":
                Swipe_Method.swipe_left(self.driver)
            if direction == "right":
                Swipe_Method.swipe_right(self.driver)
            if direction == "down":
                Swipe_Method.swipe_down(self.driver)
            if direction == "up":
                Swipe_Method.swipe_up(self.driver)

    # 获取toast信息，报错
    # def find_toast(self, message):
    #     # mes = '//*[@text="请输入账号"]'
    #     elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, message))
    #     print elem

    #截图，并保存于指定目录
    def get_screenshot(self):
        dir_path = os.path.dirname(os.getcwd()) + "\\Report\\ScreenShot"
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        pic_name = 'screenshot_' + time.strftime('%Y%m%d%H%M%S') + '.png'
        pic_url = dir_path + pic_name

        try:
            self.driver.save_screenshot(pic_url)
            print ('screenshot_name:%s' % pic_name)
        except:
            raise

    # 获取当前activity的名称
    def get_current_activity_name(self):
        activity_name = self.driver.current_activity
        print ('Current activity name is: %s' % activity_name)
        return activity_name



    # adb
    def adbKeyEvent(self,keycode):
        cmd = "adb shell input %s "%keycode
        os.system(cmd)

    # adb input
    def adb_input(self,text):
        cmd = "adb shell input text %s"%text
        os.system(cmd)

    #

if __name__ == '__main__':
    pass

# class Log:
#
#     def __init__(self, element):
#         self.el = element
#
#     def myloggger(self, msg, flag=1):
#
#         log_path = os.path.dirname(os.getcwd()) + "\\Report\\log"
#         if not os.path.isdir(log_path):
#             os.makedirs(log_path)
#         log_name = 'nw_' + time.strftime('%Y%m%d%H%M%S') + '.log'
#         file_log = log_path + log_name
#
#         logging.basicConfig(level=logging.DEBUG,
#                             format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
#                             datefmt='%a, %d %b %Y %H:%M:%S',
#                             filename=file_log,
#                             filemode='w'
#                             )
#
#         if flag == 0:
#             logging.debug(msg)
#
#         elif flag == 1:
#             logging.info(msg)
#
#         elif flag == 2:
#             logging.warning(msg)
#             self.el.get_screenshot()
#
#         elif flag == -1:
#             logging.error(msg)
#             self.el.get_screenshot()
