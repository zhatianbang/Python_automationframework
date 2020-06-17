import os

def pa():
    c = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) # 获取项目根目录
    print("不受调用影响，调用代码所在的上上层目录"+ c)
    return c