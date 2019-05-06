# -*- coding: utf-8 -*-
'''
Created on 2019年5月1日 下午7:14:43
Zhukun Luo
Jiangxi University of Finance and Economics
'''
cimport numpy as c_np
import timeit
#现在可以声明numpy数组。方法是在方括号制定类型和维数，这被称为缓冲区语法
#声明一个二维double数组
cdef c_np.ndarray[double,ndim=2] arr
#访问这个数组时，将直接操作底层的内存区域，从而极大提高速度
import numpy as np
@timeit
def numpy_bench_py():
    py_arr=np.random.rand(1000)
    cdef int i
    for i in range(1000):
        py_arr[i]+=1
@timeit
def numpy_bench_c():
    cdef c_np.ndarray[double,ndim=1] c_arr
    c_arr=np.random.rand(1000)
    cdef int i 
    for i in range(1000):
        c_arr[i]+1
