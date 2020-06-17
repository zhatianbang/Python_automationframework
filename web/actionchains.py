# coding:utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ActionChain:

    """模拟鼠标 和 模拟键盘方法"""

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    # 点击鼠标左键
    def click(self, ele):
        """
        单击鼠标左键
        :param ele: 元素对象
        :return:
        """
        self.action.move_to_element(ele).click().perform()

    # 点击鼠标右键
    def context_click(self, ele):
        """
        点击鼠标右键
        :param ele: 元素对象
        :return:
        """
        self.action.context_click(ele)

    # 点击鼠标左键，不松开
    def click_and_hold(self, ele):
        """
        单击鼠标左键，不松开
        :param ele: 元素对象
        :return:
        """
        self.action.click_and_hold(ele).perform()

    def double_click(self, ele):
        """
        双击鼠标左键
        :param ele: 元素对象
        :return:
        """
        self.action.double_click(ele).perform()

    # 悬停：鼠标移动到某个元素
    def move_to_elemet(self, ele):
        """
        悬停：鼠标移动到某个元素
        :param ele: 元素对象
        :return:
        """
        self.action.move_to_element(ele).perform()

    # 拖拽元素A到元素B的位置
    def drag_and_drop(self, source_ele, target_ele):
        """
        拖拽元素A到元素B的位置
        :param source_ele: 被拖拽的元素对象
        :param target_ele: 目标遗元素的对象
        :return:
        """
        self.action.drag_and_drop(source_ele, target_ele)

    # 拖拽元素A到元素B的位置,效果同上
    def drag_and_drop_a(self, source_ele, target_ele):
        """
        鼠标左键按住A元素移动B元素的位置后释放鼠标，并执行
        :param source_ele: 被拖拽的元素对象
        :param target_ele: 目标遗元素的对象
        :return:
        """
        self.action.click_and_hold(source_ele).move_to_element(target_ele).release().perform()

    #     # 拖拽元素A到元素B的位置,效果同上
    def drag_and_drop_b(self, source_ele, target_ele):
        """
        鼠标左键按住A元素在B元素处释放鼠标，并执行
        :param source_ele: 被拖拽的元素对象
        :param target_ele: 目标遗元素的对象
        :return:
        """
        self.action.click_and_hold(source_ele).release(target_ele).perform()

    # 移动元素到距离当前位置（x,y)的点
    def move_by_offset(self, x, y):
        """
        移动元素到距离当前位置（x,y)的点
        :param x:
        :param y:
        :return:
        """
        self.action.move_by_offset(int(x), int(y))

    # 移动元素到距离某元素（x,y)的点
    def move_to_element_with_offset(self, ele, x, y):
        """
        移动元素到距离当前位置（x,y)的点
        :param ele:
        :param x:
        :param y:
        :return:
        """
        self.action.move_to_element_with_offset(ele, int(x), int(y)).perform()

    # ctrl+指定字母
    def ctrl_letter(self, letter):
        """
        ctrl+指定字母组合键
        :param letter: 指定的字母，如a,c,x
        :return:
        """
        self.action.key_down(Keys.CONTROL).send_keys(letter).perform()

    # ctrl+v
    def ctrl_v(self, ele):
        """
        在ele元素处执行ctrl+v
        :param ele: 元素对象
        :return:
        """
        self.action.key_down(Keys.CONTROL, ele).send_keys('v').key_up(Keys.CONTROL).perform()

    def action_send_keys(self, text):
        """
        在当前焦点处输入内容
        :param text: 待输入的文本
        :return:
        """
        self.action.send_keys(text)

    @staticmethod
    def key_enter(ele):
        ele.send_keys(Keys.ENTER)

    @staticmethod
    def key_down(ele):
        ele.send_keys(Keys.DOWN)

    @staticmethod
    def key_ctrl_v(ele):
        ele.send_keys(Keys.CONTROL, "v")

    # 下面是一些常用的键盘事件：
    # Keys.BACK_SPACE：回退键（BackSpace）
    # Keys.TAB：制表键（Tab）
    # Keys.ENTER：回车键（Enter）
    # Keys.SHIFT：大小写转换键（Shift）
    # Keys.CONTROL：Control键（Ctrl）
    # Keys.ALT：ALT键（Alt）
    # Keys.ESCAPE：返回键（Esc）
    # Keys.SPACE：空格键（Space）
    # Keys.PAGE_UP：翻页键上（Page Up）
    # Keys.PAGE_DOWN：翻页键下（Page Down）
    # Keys.END：行尾键（End）
    # Keys.HOME：行首键（Home）
    # Keys.LEFT：方向键左（Left）
    # Keys.UP：方向键上（Up）
    # Keys.RIGHT：方向键右（Right）
    # Keys.DOWN：方向键下（Down）
    # Keys.INSERT：插入键（Insert）
    # DELETE：删除键（Delete）
    # NUMPAD0 ~ NUMPAD9：数字键1-9
    # F1 ~ F12：F1 - F12键
    # (Keys.CONTROL, ‘a’)：组合键Control+a，全选
    # (Keys.CONTROL, ‘c’)：组合键Control+c，复制
    # (Keys.CONTROL, ‘x’)：组合键Control+x，剪切
    # (Keys.CONTROL, ‘v’)：组合键Control+v，粘贴


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\Desktop\AutomationFramework\lib\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get('http://sahitest.com/demo/label.htm')

    input1 = driver.find_elements_by_tag_name('input')[3]
    input2 = driver.find_elements_by_tag_name('input')[4]

    action = ActionChains(driver)
    input1.click()
    action.send_keys('Test Keys').perform()
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()  # ctrl+a
    action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()  # ctrl+c

    action.key_down(Keys.CONTROL, input2).send_keys('v').key_up(Keys.CONTROL).perform()  # ctrl+v

    print(input1.get_attribute('value'))

    print(input2.get_attribute('value'))
