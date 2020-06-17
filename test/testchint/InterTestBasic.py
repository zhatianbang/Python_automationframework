#coding:utf8

import requests,jsonpath,json,random

def rand():
    s = random.randint(1,999999)
    return str(s)

randnum = rand()
deviceNameA = "机密直连ssl" + randnum
devidetypeA = "321" + randnum
shebeiA = "直接设备" +rand()
shebeiSN = "sn" + rand()
print("产品名字：" + deviceNameA + "  设备名字：" + shebeiA)

session  = requests.session()


url = "https://test-cc.chintcloud.net/api/auth/login"
data = '{"username":"duankj@chint.com","password":"a123456@"}'
res = session.post(url=url,json=json.loads(data))
print("登录返回："+res.text)
res = json.loads(res.text)

token = jsonpath.jsonpath(res,"$.token")[0]

# :
session.headers["x-authorization"] ="Bearer " + token
# 1、新增直连设备一机一密ssl
data = '{"published":"false","accessType":"direct","gateway":"direct","secretType":"一机一密","isShowGateway":true,"usedSsl":true,"authType":"ACCESS_TOKEN","productCategoryName":"a","productName":"'+ deviceNameA +'","productCategoryId":"0b0344a0-fb80-11e9-938d-8b0a5a95506a","productModel":"'+ devidetypeA +'","deviceEncode":"GB2312","accessProtocal":"MQTT"}'
url ='https://test-cc.chintcloud.net/api/capability'
res = session.post(url=url,json=json.loads(data))
print("新增设备返回："+res.text)
deviceida =  jsonpath.jsonpath(json.loads(res.text),"$.id.id")[0]
productCodea = jsonpath.jsonpath(json.loads(res.text),"$..productCode")[0]
productTokena  = jsonpath.jsonpath(json.loads(res.text),"$..productToken")[0]

# 2、增加测点
session.headers['content-type']='application/json;charset=UTF-8'
url ='https://test-cc.chintcloud.net/api/capability/'+deviceida+'/points'
data = '[{"entityType":"DEVICE_POINT","id":"0c22d0d0-2150-11ea-9412-43b05683a6e9"}]'
res = session.post(url=url,data=data)
print("添加测点返回：" + res.text)


# 3.发布
url ='https://test-cc.chintcloud.net/api/capability'
data ='{"id":{"entityType":"PRODUCT_CAPABILITY","id":"'+ deviceida +'"},"createdTime":1583323710465,"additionalInfo":null,"productCode":"'+productCodea+'","productToken":"'+ productTokena+'","productName":"'+ deviceNameA +'","published":true,"productCategoryId":"0b0344a0-fb80-11e9-938d-8b0a5a95506a","productFamily":null,"productModel":"'+ devidetypeA +'","manufacturer":null,"secretType":"一机一密","deviceEncode":"GB2312","accessType":"direct","accessProtocal":"MQTT","usedSsl":true,"authType":"ACCESS_TOKEN","description":null,"tenantId":{"entityType":"TENANT","id":"802a0ef0-1d84-11ea-ace0-dd1cdc1e9384"},"createTs":1583323710449,"modifyTs":1583323710517,"haveDevice":false,"name":"'+ devidetypeA +'"}'
res = session.post(url=url,json=json.loads(data))
print("发布产品返回："+ res.text)


# 4.新增设备
url ='https://test-cc.chintcloud.net/api/device'
data ='{"additionalInfo":{"gateway":false,"description":"'+ deviceNameA +'：对应的设备'+'"},"productCode":"cxeHAasrYW","productName":"'+ deviceNameA +'","productCategoryName":"a","name":"'+shebeiA+'","type":"机密直连ssl518937","sn":"'+shebeiSN+'"}'
res = session.post(url=url,json=json.loads(data))
print("新增设备返回："+ res.text)
