# coding:utf-8
import re


# 匹配不成功就返回None，匹配成功返回的不知道是什么对象
s =re.match("(.+)是(.*)人","他说我是那美克星人")
print(s)


# re.search 扫描整个字符串并返回第一个成功的匹配。匹配成功re.search方法返回一个匹配的对象，否则返回None。
s = re.search("我是.*人","他说我是那美克星人")
print(s)


s1 ={"token":"eyJhbGciOiJIUzUxMiJ9.-sjEf4LKtYvPKA","refreshToken":"eyJhbGciOiJIUzUxMiJ9._9ZCN8WuuLmbNaXa57cjeo--RzSQtNuy7269-LNOeW9z0NlI3mS3gQ"}
s2 = str(s1)
#
# if re.match("{\"token(.*)refreshToken\"(.*)\"}",s2):
if re.match("(.*)token(.*)refreshToken(.*)",s2):
    print("返回成功")
else:
    print("匹配失败")
