# -*- coding: utf-8 -*-
'''
Created on 2019年4月28日 下午9:06:28
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#使用numexpr最大限度优化性能
#处理复杂表达式时，Numpy将中间结果存储在内存中。numexpr可以动态地优化并编译数组表达式。还能优化缓存使用量，并利用多个处理器
import numpy as np
import numexpr as ne
a=np.random.rand(10000)
b=np.random.rand(10000)
c=np.random.rand(10000)
r=np.random.rand(10000,2)
r_i=r[:,np.newaxis]
print(r_i.shape)
r_j=r[np.newaxis,:]
print(r_j.shape)
# d_ij=r_j-r_i
d_ij=ne.evaluate('sum((r_j-r_i)**2,2)')
print(d_ij.shape)
#numexpr编译器不存储中间结果，以避免不必要的内存分配。还尽可能将运算分给多个处理器去执行
'''
(10000, 1, 2)
(1, 10000, 2)
(10000, 10000)
'''