import time
import threading


def sing(param):
    for i in range(param):
        print("%s线程数：%s,时间:%s"%(param,param,time.time()))
        time.sleep(10)




t1= threading.Thread(target=sing,args=(100,))
t2= threading.Thread(target=sing,args=(50,))
t1.start()

t2.start()
t1.join()
t2.join()
print("结束")
