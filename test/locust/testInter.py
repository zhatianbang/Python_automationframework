# coding:utf-8

import requests
import json


session = requests.session()

#
url = "https://test-cc.chintcloud.net/api/auth/login"
data = '{"username":"duankj@chint.com","password":"a123456@"}'
res = session.post(url=url,json=json.loads(data))
print("登录返回："+res.text)
res = json.loads(res.text)
print()
import random

print(random.randint(1,999999999999999))

sn = str(random.randint(1,999999999999999))
device_name = str(random.randint(1,999999999999999))

url = 'https://test-cc.chintcloud.net/api/device'  # 接口请求的URL地址
data = '{"additionalInfo":{"description":"","gateway":true},"projectName":"","name":"locust名称' + device_name + '","type":"新增产品名字3113889","productCategoryName":"ronnie专用误删","productCode":"cLUNXkaBVi","sn":"' + sn + '"}'
print(data)
import json
print(json.loads(data))