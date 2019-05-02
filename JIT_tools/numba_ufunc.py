# -*- coding: utf-8 -*-
'''
Created on 2019年5月2日 下午6:48:53
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#numba通用函数
import numpy as np
import numba as nb
import timeit
@np.vectorize#使用vectorize添加广播功能
def cantor(a,b):#cantor配对函数，将两个自然数编码成一个自然数
    return int(0.5*(a+b)*(a+b+1)+b)
print(cantor(np.array([1,2]),2))#[ 8 12]
@nb.vectorize#使用vectorize添加广播功能
def cantor1(a,b):#cantor配对函数，将两个自然数编码成一个自然数
    return int(0.5*(a+b)*(a+b+1)+b)
print(timeit.timeit("cantor1(np.array([1,2]),2)",setup="import numpy as np;from __main__ import cantor1",number=100000))
print(timeit.timeit("cantor(np.array([1,2]),2)",setup="import numpy as np;from __main__ import cantor",number=100000))
'''
0.236509084702
1.30804300308
numba领先numpy
'''
#numba能够进行类型推导，通用函数另一个特点是能够并行执行，向装饰器nb.vectorize传递关键字参数target='cpu' or'gpu'