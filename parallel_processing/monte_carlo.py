# -*- coding: utf-8 -*-
'''
Created on 2019年5月5日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#使用monte carlo计算pi的近似值
#串行版本
import random
samples=1000000
hits=0
for i in range(samples):
    x=random.uniform(-1.0,1.0)#规整范围
    y=random.uniform(-1.0,1.0)
    if x**2+y**2<=1:
        hits+=1
pi=4.0*hits/samples
print(pi)#3.143
#parallel版本
import multiprocessing
def sample():
    x=random.uniform(-1.0,1.0)#规整范围
    y=random.uniform(-1.0,1.0)
    if x**2+y**2<=1:
        return 1
    else:
        return 0
def sample_multiple(sample_partial):
    return sum(sample() for i in range(sample_partial))
if __name__=='__main__':
    pool=multiprocessing.Pool()
    results_async=[pool.apply_async(sample) for i in range(samples)]
    hits=sum(r.get() for r in results_async)
    #降低通信开销
    n_tasks=10
    chunk_size=samples/n_tasks
    results_async1=[pool.apply_async(sample_multiple,chunk_size) for i in range(n_tasks)]
    hits=sum(r.get() for r in results_async1)
    
