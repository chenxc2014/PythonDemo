# _*_ coding:utf-8 _*_
# author:chenxc
# datetime:2019/7/11 23:14
# function:

"""
浅复制
浅复制只复制目标对象的最外层，不会复制内部的子对象
所以复制出来的对象并非与原对象毫不相关
"""
import copy
l1 = [[1], [2], [3], [4]]
l2 = l1.copy()
# 这里这两种复制，都是浅复制
l2_2 = copy.copy(l1)
l3 = l2
print(id(l1))
print(id(l2))
print(id(l2_2))
print(id(l3))
l1.append([5])
l3[1][0] = 0
print(l1)
print(l2)
print(l2_2)
print(l3)
