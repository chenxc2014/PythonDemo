# _*_ coding:utf-8 _*_
# author:chenxc
# datetime:2019/7/11 23:24
# function:

"""
深复制
深复除了复制目标对象的最外层，还递归复制了所有的子对象
所以复制出来的对象与原对象完全不相关
"""
import copy

l1 = [[1], [2], [3], [4]]
l2 = copy.deepcopy(l1)
l3 = l2
print(id(l1))
print(id(l2))
print(id(l3))
l1.append([5])
l3[1][0] = 0
print(l1)
print(l2)
print(l3)
