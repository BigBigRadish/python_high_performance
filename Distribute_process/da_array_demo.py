# -*- coding: utf-8 -*-
'''
Created on 2019年5月6日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#dask数组实例
import os
os.environ["PATH"] += os.pathsep + 'E:/graphviz/bin'
import graphviz
import dask 
import numpy as np
import dask.array as da
a=np.random.rand(30)
a_da=da.from_array(a,chunks=10)
print(a_da)#dask.array<array, shape=(30,), dtype=float64, chunksize=(10,)>
#变量维护着一个Dask图，这个图可通过属性dask访问。
print(dict(a_da.dask))
'''
{('array-0be8fc5a17faf72eaef43e3102ddb8bc', 0): (<built-in function getitem>, 'a
rray-original-0be8fc5a17faf72eaef43e3102ddb8bc', (slice(0, 10, None),)), ('array
-0be8fc5a17faf72eaef43e3102ddb8bc', 1): (<built-in function getitem>, 'array-ori
ginal-0be8fc5a17faf72eaef43e3102ddb8bc', (slice(10, 20, None),)), ('array-0be8fc
5a17faf72eaef43e3102ddb8bc', 2): (<built-in function getitem>, 'array-original-0
be8fc5a17faf72eaef43e3102ddb8bc', (slice(20, 30, None),)), 'array-original-0be8f
c5a17faf72eaef43e3102ddb8bc': array([0.5993826 , 0.59125626, 0.61325017, 0.66146
495, 0.98397374,
       0.46435936, 0.17210742, 0.99033549, 0.26083166, 0.33333832,
       0.77390389, 0.04439243, 0.33185568, 0.19555444, 0.89698959,
       0.50299082, 0.6437859 , 0.62624128, 0.82580572, 0.46065807,
       0.51549077, 0.79074589, 0.22691995, 0.07017427, 0.73730723,
       0.0287668 , 0.64240203, 0.28444215, 0.45677881, 0.3114798 ])}
'''
#每个任务提取一个包含10个元素的切片
#对数组a_da执行操作，dask将生成更多操作快的子任务，这是并行的大门。
#dask与numpy的兼容
N=10000
chunksize=1000
x_data=np.random.uniform(-1,1,N)
y_data=np.random.uniform(-1,1,N)

x=da.from_array(x_data,chunks=chunksize)
y=da.from_array(y_data,chunks=chunksize)
hit_test=x**2+y**2<1
hits=hit_test.sum()
pi=4*hits/N
print(pi.compute())#3.1192
pi.visualize()#可视化dask图
# print(pi.compute(get=dask.get))
