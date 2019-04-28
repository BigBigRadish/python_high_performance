# -*- coding: utf-8 -*-
'''
Created on 2018年04月12日 下午1:12:39
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#numpy的广播机制
import numpy as np
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print(A*B)
'''
[[ 5 12]
 [21 32]]
'''
#如果两个操作数的形状不匹配，Numpy尝试使用广播规则让他们匹配
#如果其中一个操作数是标量，将会应用于数组的每一个元素
print(A*2)
'''
[[2 4]
 [6 8]]
'''
#如果两个操作数都是数组，NUmpy将尝试从最后一个轴让他们的形状匹配。例如如果要合并两个形状分别为（3,2）,和（,2）,将把第二个数组重复三次，生成一个（3,2）的数组。。换而言之，将沿一个维度广播这个数组，使与另一个匹配。
#如果形状不匹配，将会引发异常
#可通过添加长度为1的轴来调整数组的形状。通过将常量numpy.newaxis用作索引，可引入一个维度。
A=np.random.rand(5,10,2)
B=np.random.rand(5,2)
A*B[:,np.newaxis,:]

a=np.array([1,2,3])
b=np.array([1,2,3])
AB=a[:,np.newaxis]*b[np.newaxis,:]
print(AB)
'''
计算外积
[[1 2 3]
 [2 4 6]
 [3 6 9]]
'''