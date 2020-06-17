#coding:utf8
from lxml import etree
from common.mail import Mail

mail = Mail()

f = open("D:\\1.html","r",encoding="utf8") #读取文件
f = f.read()    #把文件内容转化为字符串
html = etree.HTML(f) #把字符串转化为可处理的格式

# 读取成功率（完全符合xpath语法）
result2 = html.xpath("//*[@class='details']/tr[2]/td[3]")
if result2[0].text == "100.00%":
    print("pass")
else:
    mail.mail_info['filepaths'] = ["D:"]
    mail.mail_info['filenames'] = ["D:\\1.html"]
    mail.send()