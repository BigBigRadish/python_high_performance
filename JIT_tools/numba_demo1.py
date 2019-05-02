# -*- coding: utf-8 -*-
'''
Created on 2019年5月2日 下午4:12:36
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#numba入门
# def sum_sq(a):
#     result=0
#     N=len(a)
#     for i in range(N):
#         result+=a[i]
#     return result
import numba,timeit
import numpy as np
import numba as nb
@nb.jit
def sum_sq(a):
    result=0
    N=len(a)
    for i in range(N):
        result+=a[i]
    return result
#numba将检测输入参数a的类型，并编译出一个性能更高的特殊版本
#要测量numba编译器带来的性能提升，可对原是函数和特殊函数的执行时间进行比较。要访问未经装饰的原是函数，可使用py_func

print(timeit.timeit("sum_sq(x)",setup="import numpy as np;x=np.random.rand(10000);from __main__ import sum_sq",number=1000))
print(timeit.timeit("sum_sq.py_func(x)",setup="import numpy as np;x=np.random.rand(10000);from __main__ import sum_sq",number=1000))
'''
0.114336967468
1.59666919708
numba的速度更快
numba比列表推导式以及numpy还要快一些
'''
#类型特殊化
#numba可通过属性signatures暴露特殊版本
print(sum_sq.signatures)#[(array(float64, 1d, C),)]
x=np.random.rand(1000).astype('float32')
sum_sq(x)
print(sum_sq.signatures)#[(array(float64, 1d, C),), (array(float32, 1d, C),)]
#可显示的针对特定类型来编译这个函数，为此可向函数nb.jit传递一个签名
#要传递签名，可使用一个元组，其中包含可接受的类型。numba提供了大量的类型，这些类型可在模块nb.types和顶级命名空间nb中找到。
@nb.jit((nb.float64[:],))#float64作为唯一参数类型
def sum_sq1(a):
    result=0
    N=len(a)
    for i in range(N):
        result+=a[i]
    return result
#如果传入其他类型将会引入异常
# sum_sq1(x.astype('float32'))
'''
TypeError: No matching definition for argument type(s) array(float32, 1d, C)
'''
#也可传入多个签名
@nb.jit(["float64(float64[:])","float64(float32[:])"])
def sum_sq2(a):
    result=0
    N=len(a)
    for i in range(N):
        result+=a[i]
    return result
sum_sq2(x.astype('float32'))