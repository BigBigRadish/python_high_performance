# -*- coding: utf-8 -*-
'''
Created on 2019年5月2日 下午7:06:04
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#泛化通用函数实例
import numpy as np
import numba as nb
a=np.random.rand(3,3)
b=np.random.rand(3,3)
c=np.matmul(a,b)
print(c.shape)#(3, 3)
#ufunc将操作广播到整个标量数组，广播到数组的数组。
a=np.random.rand(10,3,3)
b=np.random.rand(3,3)#广播到形状（10,3,3）
c=np.matmul(a,b)
print(c.shape)#(10, 3, 3)
#numba提供了装饰器nb.guvectorize，以支持高效的泛化通用函数实现
@nb.guvectorize(['float64[:],float64[:],float64[:]'],'(n),(n) -> ()')
def euclidean(a,b,out):
    N=a.shape[0]
    out[0]=0.0
    for i in range(N):
        out[0]+=(a[i]-b[i])**2
#numba将标量视为长度为1的数组
a=np.random.rand(2)
b=np.random.rand(2)
print(euclidean(a, b))#0.6357443722228958
a=np.random.rand(10,2)
b=np.random.rand(10,2)
print(euclidean(a, b))#[0.48912612 0.76901234 0.8372441  0.62800346 0.00434796 0.27041949  0.10514873 0.21790081 0.8208809  0.20753536]
#numba比numpy速度更快
