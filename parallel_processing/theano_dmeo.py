# -*- coding: utf-8 -*-
'''
Created on 2019年5月5日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#theano代码示例
import theano.tensor as T
import theano as th
a=T.scalar('a')
a_sq=a**2
print(a_sq)#Elemwise{pow,no_inplace}.0
compute_square=th.function([a],a_sq)#返回一个可直接使用的pyhton函数
print(compute_square(2))#4.0,类型默认为float64
print(a.dtype)#float64
#相比于numba，theano不会编译通用的python代码，也不做任何类型推断，必须准确指定类型
#theano真正的威力在于它对于数组的支持。要定义一维向量，可使用函数T.vector,它返回的变量支持广播操作，就像numpy数组一样
a=T.vector('a')
b=T.vector('b')
ab_sq=a**2+b**2
compute_square1=th.function([a,b],ab_sq)
re=compute_square1([0,1,2],[3,4,5])
print(re)#[ 9. 17. 29.]
#将Theano API作为一种微型语言，用来合并各种numpy数组表达式，这样将生成高效的机器码

