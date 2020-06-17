# coding:utf8
import os,datetime
from selenium import webdriver
#
# def f(a=1,b=2,c=3):
#     return a+b+c
#
# list =['Sheet1', 'Sheet2']
# list2= [1]
# list = list2 + list
# print(list)
#
# driver = webdriver.Chrome(executable_path='../../lib/chromedriver')
# driver.get("http://www.baidu.com")
#
#
# file_path = os.path.dirname(os.path.abspath('..')) + '/screenshots/'
# print(file_path)
# # # now_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
# now_time = datetime.datetime.now().strftime('%Y%m%d_%H_%M_%S_%f')  # 含微秒的日期时间，来源 比特量化
now_time = datetime.datetime.now().strftime('%Y%m%d_%H_%M_%S')  # 含微秒的日期时间，来源 比特量化

# screen_name = file_path + now_time + '.png'
# driver.get_screenshot_as_file(screen_name)
print(now_time)

print(os.path.abspath("."))

t="1.0"
print(int(float(t)))