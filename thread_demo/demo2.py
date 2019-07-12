# -*- coding:utf-8 -*-
# Author: chenxc
# Date: 2019/7/12 10:05
# Func:

import threading
import time

'''
    多个线程修改同个共享数据时，需要通过加锁来处理并发
    通过threading.Lock()或是threading.RLock()来处理
    这两个对象下都会有acquire()和release()这两个方法，前者用于申请一个锁，后缀用于释放对应的锁
    
    Lock下，同一线程中不能多次acquire（会造成死锁）,acquire与release必须成对出现，即acquire后必须出现release
    RLock下，同一线程中允许出现多次acquire，即acquire后可以再出现acquire(中间没有release)，但acquired的次数与release的次数必须相等。
'''


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        threadLock.acquire()
        print_time(self.name, 1, self.counter)
        # 释放锁，开启下一个线程
        threadLock.release()
        threadLock.release()


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


# threadLock = threading.Lock()
threadLock = threading.RLock()
threads = []

# 创建新线程
thread1 = MyThread(1, "Thread-1", 3)
thread2 = MyThread(2, "Thread-2", 3)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
