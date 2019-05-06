# -*- coding: utf-8 -*-
'''
Created on 2019年5月6日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#theano使用openmp
import theano as th
th.config.openmp=True#启用openmp支持
th.config.openmp_elemwise_minsize=1000#当数组长度超过1000.才对基于元素的操作进行并行化
th.config.OMP_NUM_THREADS=4
#要控制分配给OpenMP执行的线程数，可在执行代码前设置环境变量OMP_NUM_THREADS
#一个基准程序，演示如何使用openMP
import numpy as np
import timeit
import theano.tensor as T
x=T.vector('x')
y=T.vector('y')
hit_test=x**2+y**2<=1
hits=hit_test.astype('int32').sum()
misses=x.shape[0]
pi_est=4*hits/misses

calculate_pi=th.function([x,y],pi_est,profile=True)
x_val=np.random.uniform(-1,1,30000)
y_val=np.random.uniform(-1,1,30000)
res=timeit.timeit('calculate_pi(x_val,y_val)','from __main__ import x_val,y_val,calculate_pi',number=100000)
print(res)
calculate_pi.profile.summary()#打印剖析摘要
#使用两个线程，性能小幅度提升，但是再增加线程，性能急速下降。这说明就输入规模而言，使用两个以上线程没有任何好处，因为启动新线程和同步其共享数据的代价比并行计算带来的好处大