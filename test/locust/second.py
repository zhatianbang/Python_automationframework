import random
from locust import HttpUser, task, between, SequentialTaskSet, tag
import json
import jsonpath
import re
import random

# 定义一个任务类，这个类名称自己随便定义，类继承SequentialTaskSet 或 TaskSet类，所以要从locust中，引入SequentialTaskSet或TaskSet
# 当类里面的任务请求有先后顺序时，继承SequentialTaskSet类， 没有先后顺序，可以使用继承TaskSet类
class MyTaskCase(SequentialTaskSet):
    # 初始化方法，相当于 setup
    def on_start(self):
        url = 'https://test-cc.chintcloud.net/api/auth/login'  # 接口请求的URL地址
        self.headers = {"Content-Type": "application/json"}  # 定义请求头为类变量，这样其他任务也可以调用该变量

        data = '{"username":"duankj@chint.com","password":"a123456@"}'

        # 使用self.client发起请求，请求的方法根据接口实际选,
        # catch_response 值为True 允许为失败 ， name 设置任务标签名称   -----可选参数
        with self.client.post(url, json=json.loads(data), headers=self.headers, catch_response=True) as rsp:

            # 断言结果
            if re.match("(.*)token(.*)refreshToken(.*)", rsp.text):
                # rsp.success("接口登陆成功！")
                result = json.loads(rsp.text)
                token_tmp = jsonpath.jsonpath(result, "$.token")
                token = "Bearer " + token_tmp[0]
                # 添加头域的token
                self.headers["x-authorization"] = token

            else:
                print(rsp.text)

    # @task python中的装饰器，告诉下面的方法是一个任务，任务就可以是一个接口请求，
    # 这个装饰器和下面的方法被复制多次，改动一下，就能写出多个接口
    # 装饰器后面带上(数字)代表在所有任务中，执行比例
    # 要用这个装饰器，需要头部引入 从locust中，引入 task
    # @task
    # # @tag("leave_1")
    # def login(self):  # 一个方法， 方法名称可以自己改
    #     url = 'https://test-cc.chintcloud.net/api/auth/login'  # 接口请求的URL地址
    #     self.headers = {"Content-Type": "application/json"}  # 定义请求头为类变量，这样其他任务也可以调用该变量
    #
    #     data = '{"username":"duankj@chint.com","password":"a123456@"}'
    #
    #     # 使用self.client发起请求，请求的方法根据接口实际选,
    #     # catch_response 值为True 允许为失败 ， name 设置任务标签名称   -----可选参数
    #     with self.client.post(url, json=json.loads(data), headers=self.headers,catch_response = True) as rsp:
    #
    #         # 断言结果
    #         if re.match("(.*)token(.*)refreshToken(.*)", rsp.text):
    #             # rsp.success("接口登陆成功！")
    #             result = json.loads(rsp.text)
    #             token_tmp = jsonpath.jsonpath(result, "$.token")
    #             token = "Bearer " + token_tmp[0]
    #             # 添加头域的token
    #             self.headers["x-authorization"] = token
    #
    #         else:
    #             print(rsp.text)
    #             # rsp.fail("接口登陆失败")
    #     # assert re.match("(.*)token(.*)refreshToken1(.*)", rsp.text)

    def randNum(self):
        return str(random.randint(1,999999999999999))


    @task  # 装饰器，说明下面是一个任务
    def login_(self):
        device_name = self.randNum()
        sn = self.randNum()
        url = 'https://test-cc.chintcloud.net/api/device'  # 接口请求的URL地址
        data ='{"additionalInfo":{"description":"","gateway":true},"projectName":"","name":"locust名称' + device_name + '","type":"新增产品名字3113889","productCategoryName":"ronnie专用误删","productCode":"cLUNXkaBVi","sn":"'+ sn +'"}'
        print(type(data))
        with self.client.post(url, json=json.loads(data), headers=self.headers) as rsp:
            print(rsp.text)



    # 结束方法， 相当于teardown
    def on_stop(self):
        pass


# 定义一个运行类 继承HttpUser类， 所以要从locust中引入 HttpUser类
class UserRun(HttpUser):
    tasks = [MyTaskCase]
    wait_time = between(0.1, 3)  # 设置运行过程中间隔时间 需要从locust中 引入 between

if __name__ == '__main__':
    import os
    os.system("locust -f second.py --host=https://test-cc.chintcloud.net")