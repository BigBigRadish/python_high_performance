# -*- coding: utf-8 -*-
'''
Created on 2019年5月5日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#cython串行示例
import Cython
import numpy as np
def sqare_serial(double[:] inp):
    cdef int i,size
    cdef double[:] out
    size=inp.shape[0]
    out_np=np.empty(size,'double')
    out=out_np
    for i in range(size):
        out[i]=inp[i]*inp[i]
    return out_np
#cython并行示例
def sqare_serial1(double[:] inp):
    cdef int i,size
    cdef double[:] out
    size=inp.shape[0]
    out_np=np.empty(size,'double')
    out=out_np
    with nogil:#使用prange,必须确定循环体不使用解释器。避免解释器调用GIL
        for i in prange(size):#,nogil=True
            out[i]=inp[i]*inp[i]
    return out_np