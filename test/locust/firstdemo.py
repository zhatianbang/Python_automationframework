from locust import HttpLocust, TaskSet, task, HttpUser,between, SequentialTaskSet

# 定义用户行为
class UserBehavior(SequentialTaskSet):

    # 进行初始化的工作，每个Locust用户开始做的第一件事
    def on_start(self):
        print("start")

    @task(1)
    def bky_index(self):
        self.client.get("/api/auth/login")

    @task(2)
    def blogs(self):
        self.client.get("/api/device")

    # 进行清理的工作，每个Locust用户做的最后一件事
    def on_stop(self):
        """"""
        print("pass")

# 定义一个运行类 继承HttpUser类， 所以要从locust中引入 HttpUser类
class RunnUserBehavior(HttpUser):
    host = "https://test-cc.chintcloud.net"
    task_set = [UserBehavior] # 类熟悉task_set必须为列表或者字典
    # min_wait = 1500
    # max_wait = 5000
    wait_time = between(0.1, 3)



if __name__ == '__main__':
    import os
    os.system("locust -f second.py --host=https://test-cc.chintcloud.net")