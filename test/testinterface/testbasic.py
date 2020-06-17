#coding:utf8

import requests,jsonpath,json,traceback,random
session = requests.session()


url ="http://test-cc.chintcloud.net/api/auth/login"
data ='{"username":"common-api@chint.com","password":"common-api"}'
res = session.post(url=url,data=data)
print(res.text)

token = json.loads(res.text)
token = jsonpath.jsonpath(token,"$.token")[0]
print(token)
session.headers['x-authorization'] = 'Bearer ' + token


# 添加设备
url = "https://test-cc.chintcloud.net/api/device"
data = '{"additionalInfo":{"gateway":false},"productCode":"hKtxlJyCmz","productName":"接口测试专用","productCategoryName":"ronnie专用误删","name":"标签测试UseRandom","type":"接口测试专用","sn":"SNSNUseRandom"}'

# res = session.post(url,json=json.loads(data))
# print(res.text)

def userandom( s):
    """最多6位随机数"""
    try:
        res = s
        if s.find('UseRandom') != -1:
            res = res.replace('UseRandom', str(random.randint(1, 999999)))
            # self.params[s] = str(res)
        return res
    except Exception as e:
        print(traceback.format_exc())

res = session.post(url,json=json.loads(data))
print(res.text)

res = json.loads(res.text)
device_id = jsonpath.jsonpath(res,'$.id.id')[0]
print(device_id)


url = "https://test-cc.chintcloud.net/api/device/" + device_id
res = session.delete(url)
print("响应结果：%s"%res.content)
if res.text is None or res.text =="":
    print("空结果")

print(json.loads(res.text))