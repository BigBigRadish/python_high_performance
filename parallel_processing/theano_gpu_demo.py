# -*- coding: utf-8 -*-
'''
Created on 2019年5月6日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#theano gpu编程
THEANO_FLAGS='floatX=float32,device=gpu0,lib.cnmem=1'
from theano import function, config
import theano.tensor as T
import numpy as np
import time
N=5000
A_data=np.random.rand(N,N).astype('float32')#明确指定类型
B_data=np.random.rand(N,N).astype('float32')

A=T.matrix('A')
B=T.matrix('B')
f=function([A,B], T.dot(A, B))
start=time.time()
f(A_data,B_data)
print('Matrix multiply ({}) took {} seconds'.format(N,time.time()-start))
print('Device used: ',config.device)