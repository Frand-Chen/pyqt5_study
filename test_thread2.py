import threading
import time


class myThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始", self.name)
        print_time(self.name, self.counter, 1)
        print("结束", self.name)


def print_time(name, counter, delay):
    count = 0
    while count < counter:
        time.sleep(delay)
        print("%s:%s" % (name, time.ctime(time.time())))
        count += 1


thread1 = myThread(1, "thread1", 2)
thread2 = myThread(2, "thread2", 5)

# 开启线程
thread1.start()
thread2.start()
# join()功能是在程序指定位置，优先让该方法的调用者使用 CPU 资源
thread1.join()
thread2.join()
print("线程结束....")
