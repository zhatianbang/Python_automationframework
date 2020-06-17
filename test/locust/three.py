import random
from locust import HttpUser, task, between, SequentialTaskSet, tag
import json
import jsonpath
import re
import random

# 定义一个任务类，这个类名称自己随便定义，类继承SequentialTaskSet 或 TaskSet类，所以要从locust中，引入SequentialTaskSet或TaskSet
# 当类里面的任务请求有先后顺序时，继承SequentialTaskSet类， 没有先后顺序，可以使用继承TaskSet类

class MyTaskCase(SequentialTaskSet):

    
    def set_up(self):
        print("111111111111111")


    # 初始化方法，相当于 setup
    def on_start(self):
        print("每个迭代时所有@task执行开始前执行")


    def randNum(self):
        return str(random.randint(1,999999999999999))

    @task  # 装饰器，说明下面是一个任务
    def login_(self):
        url = 'https://test-cc.chintcloud.net/api/auth/login'  # 接口请求的URL地址
        self.headers = {"Content-Type": "application/json"}  # 定义请求头为类变量，这样其他任务也可以调用该变量
        data = '{"username":"duankj@chint.com","password":"a123456@"}'

        # 使用self.client发起请求，请求的方法根据接口实际选,
        # catch_response 值为True 允许为失败 ， name 设置任务标签名称   -----可选参数
        with self.client.post(url, json=json.loads(data), headers=self.headers, catch_response=True) as rsp:
            print(rsp.text)

    @task
    def test2(self):
        print("测试方法2")


    # 结束方法， 相当于teardown
    def on_stop(self):
        print("每个迭代时，所有的@task执行结束后")


# 定义一个运行类 继承HttpUser类， 所以要从locust中引入 HttpUser类
class UserRun(HttpUser):
    tasks = [MyTaskCase]
    wait_time = between(0.1, 3)  # 设置运行过程中间隔时间 需要从locust中 引入 between

if __name__ == '__main__':
    import os
    os.system("locust -f three.py --host=https://test-cc.chintcloud.net")