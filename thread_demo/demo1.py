# -*- coding:utf-8 -*-
# Author: chenxc
# Date: 2019/7/11 17:53
# Func: 

import threading
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, 1, self.counter)
        print("退出线程：" + self.name)


def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            thread_name.exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = MyThread(1, "Thread-1", 3)
thread2 = MyThread(2, "Thread-2", 4)

# 开启新线程
thread1.start()
thread2.start()
# thread1.join()
# thread2.join()
print("退出主线程")
