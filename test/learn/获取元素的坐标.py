#!/usr/bin/env python
# -*- codinfg:utf-8 -*-

from selenium import webdriver
import time

from PIL import Image

# options = webdriver.ChromeOptions()
#
# driver = webdriver.Chrome(executable_path=r'D:\installation\pythonworkspace\AutomationFramework\lib\chromedriver.exe', options=options)
# driver.get("https://www.baidu.com/")
# driver.maximize_window()
#
#
#
# # driver.quit()
# def save_ele_png(loc, filename):
#     baidu_img =driver.find_element_by_id(loc)
#     filePath = "../" + filename + ".png"
#     driver.save_screenshot(filePath)
#     left = baidu_img.location['x']
#     top = baidu_img.location['y']
#     right = baidu_img.location['x'] + baidu_img.size['width']
#     bottom = baidu_img.location['y'] + baidu_img.size['height']
#     im = Image.open(filePath)
#     im = im.crop((left, top, right, bottom))  # 对浏览器截图进行裁剪
#     im.save('../baidu.png')
#
# save_ele_png("su", "测试")

a ="2.png"
print(a[:-4])


if a.endswith('.png'):
    print("对")