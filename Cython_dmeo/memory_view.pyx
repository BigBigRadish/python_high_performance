# -*- coding: utf-8 -*-
'''
Created on 2019年5月1日 下午8:00:11
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#内存视图定义
cdef int[:] a#0维内存视图
cdef double [:,:] b#二维内存视图，类似切片
#这种语法也可以用于声明任何类型的变量和类属性，还可用于函数定义。任何暴露了缓冲区的接口对象都将自动绑定到内存视图。
import numpy as np
cdef int[:] arr
arr_np=np.zeros(10,dtype='int32')
arr=arr_np#将数组绑定到内存视图
#内存视图并不拥有与之绑定的数据，只是提供一种访问修改的途径
arr[2]=1
print(arr_np)
#对于内存视图，也可使用标准的numpy语法来执行切片操作
cdef int[:,:,:] a 
arr[0,:,:]#二维内存视图
arr[0,0,:]#一维内存视图
arr[0,0,0]#一个int值
#可以在内存视图之间复制数据
