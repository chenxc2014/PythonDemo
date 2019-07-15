# -*- coding:utf-8 -*-
# Author: chenxc
# Date: 2019/7/11 15:10
# Func: 

import sys

'''
 使用了yield的函数被称为生成器，生成器是一个返回迭代器的函数，只能用于迭代操作
 在调用生成器运行的过程中，每次遇到yield时函数会暂停并保持当前所有的运行信息，返回yield的值
 并在下一次执行next()方法时从当前位置继续运行。
'''


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        print("exit")
        sys.exit()
