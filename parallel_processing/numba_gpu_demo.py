# -*- coding: utf-8 -*-
'''
Created on 2019年5月6日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#使用numba进行并行编程
#cpu版示例程序
import numba as nb
import math
@nb.vectorize(target='cpu')
def expon_cpu(x,y):
    return math.exp(x)+math.exp(y)
print(expon_cpu(1, 2))
@nb.vectorize(['float32(float32,float32)'],target='cuda')
def expon_gpu(x,y):
    return math.exp(x)+math.exp(y)
import numpy as np
import time

N=1000000
niter=100
a=np.random.rand(N).astype('float32')
b=np.random.rand(N).astype('float32')
#促发编译
expon_cpu(a,b)
expon_gpu(a,b)
#测量时间
start=time.time()
for i in range(niter):
    expon_cpu(a, b)
print('cpu:',time.time()-start)

start=time.time()
for i in range(niter):
    expon_gpu(a, b)
print('gpu:',time.time()-start)
#数组非常大才会有优势
#对大型数据集来说，并行处理是一种改善性能的有效方式。