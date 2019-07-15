# _*_ coding:utf-8 _*_
# author:chenxc
# datetime:2019/7/13 22:11
# function:

"""
 queue 模块提供队列类，分别有三种类型的队列
       q = queue.Queue(N)  FIFO，即先进先出队列
       q = queue.LifoQueue(N)   LIFO，即后进先出队列
       q = queue.PriorityQueue(N)  优先级别队列

       q.empty() 判断当前队列是否已空
       q.qsize() 获取当前队列大小
       q.full() 判断当前队列是否已满
       q.put(xx) | p.put_nowait(xx) 入列操作
       q.get() | p.get_nowait() 出列操作
"""

import queue
import threading
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.q = q

    def run(self):
        print("开启线程：" + self.name)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)


def process_data(thread_name, q):
    while not exitFlag:
        queueLock.acquire()  # 读取队列时，先加锁
        if not q.empty():
            data = q.get()
            queueLock.release()  # 队列读出后，再解锁
            print("%s processing %s" % (thread_name, data))  # 打印是哪个线程读取的队列数据
        else:
            queueLock.release()

        time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
# FIFO队列，即：先进先出
# workQueue = queue.Queue(10)
# LIFO队列，即：后进先出
# workQueue = queue.LifoQueue(10)
# 优先级队列
workQueue = queue.PriorityQueue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = MyThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()  # 填充前先加锁
for word in nameList:
    workQueue.put(word)
queueLock.release()  # 填充后再解锁

# 等待队列清空
# index = 1
while not workQueue.empty():
    # print(index)
    # index += 1
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()

print("退出主线程")
