# _*_ coding:utf-8 _*_
# author:chenxc
# datetime:2019/7/12 23:17
# function:
import time
import sys

'''
    生成器（是一个返回迭代器的返回），只能用于迭代操作，只有运行next时才会真正执行一次迭代
'''


def gen_demo():
    print("before any yield")
    yield "first yield"
    print("between yield")
    yield "second yield"
    print("no yield anymore")


gen = gen_demo()
# sys.exit(0)

while True:
    try:
        tip = next(gen)
        print("-----:{0}".format(tip))
        time.sleep(5)
    except StopIteration as ex:
        print(str(ex))
        break
