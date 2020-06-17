# js = 'document.getElementById("end").scrollIntoView()'
import  datetime,os,time
# dt_ms = datetime.datetime.now().strftime('%Y%m%d_%H_%M_%S_%f') # 含微秒的日期时间，来源 比特量化
# file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
# screen_name = file_path + dt_ms + '.png'
# print(screen_name)
import threading

cmd =r"D:\installation\MuMu\emulator\nemu\EmulatorShell\NemuPlayer.exe"


def run(cmd):
    try:
        os.popen(cmd).read()

    except Exception as e:
        pass
        th = threading.Thread(target=run, args=(cmd,))
        th.start()
        time.sleep(10)


# run(cmd)
print("123")

a ={"a":124}
print("测试%s"%a)
