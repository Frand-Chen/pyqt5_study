import _thread
import time


def print_time(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s:%s" % (name, time.ctime(time.time()),))


try:
    _thread.start_new_thread(print_time, ("thread1", 2))
    _thread.start_new_thread(print_time, ("thread2", 4))
except:
    print("无法启动线程")

print(_thread._count())
while 1: # 保持程序运行
    pass
