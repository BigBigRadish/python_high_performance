# -*- coding: utf-8 -*-
'''
Created on 2019年4月12日 下午6:16:27
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#numy数组的创建和操作实例
#创建数组
import numpy as np
a=np.array([10,1,2])
print(a.dtype)
'''
int64
'''
#转为float,两种方式
a=np.array([10,1,2],dtype='float32')
a.astype('float32')
#创建二维数组
a=np.array([[10,1,2],[3,4,5]])
print(a)
print(a.shape)#输出轴
'''
[[10  1  2]
 [ 3  4  5]]
(2, 3)
'''
a=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(a.shape)
#(16,)
b=a.reshape(4,4)#等价于a.shape=(4,4)
print(b)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
'''
#numpy提供了一些便利的函数，可用于创建使用0或1填充的数组以及没有初始值的数组
np.zeros((3,3))
np.empty((3,3))
np.ones((3,3), dtype='float32')
np.random.rand(3,3)#生成一个随机数组
np.zeros_like(a)#初始化一个与其他形状数组相同的数组


##访问数组
#对于numpy数组，可使用整数索引来访问其元素，还可使用for元素进行迭代
A=np.array([0,1,2,3,4,5,6,7,8])
print(A[0])
'''
0
'''
print([a for a in A])
#[0, 1, 2, 3, 4, 5, 6, 7, 8]
#在numpy中，可在下标运算符[]中使用多个用逗号分割的索引来访问数组元素和子数组，如果访问一个（3,3）的数组，访问索引为0的元素，得到的将是第一行
A=np.array([[1,2,3],[1,2,3],[1,2,3]])
print(A[0])
#[1 2 3]
#要访问第一行第二个元素
print(A[0,1])#实际上是A[（0,1）]，换而言之，索引其实是一个元组
#2
#对数组进行切片
print(A[0:2])#在第一维上切片
print(A[0:2,0:2])#同时也在第二维上切片
'''
[[1 2 3]
 [1 2 3]]
[[1 2]
 [1 2]]
'''
#要更新数组上的值，可使用数字索引，也可使用切片
A[0,1]=7
A[0:2,0:2]=[[0,0],[0,0]]
#使用切片语法访问数组的速度非常快，这是因为不会创建副本，只会返回一个内存区域的视图。如果我们获取原始数组的切片，修改其中，则原始数组的值也会被修改
a=np.array([1,1,1,1])
a_view=a[0:2]
a_view[0]=2
print(a)#[2 1 1 1]
#修改numpy数组时必须十分小心。因为数据在视图之间共享。为避免副作用，可将标志a.flags.writable设置为False，这将避免无意间修改数组或者视图
#花式索引
a=np.array([0,1,2,3,4,5,6,7,8])
idx=np.array([0,2,3])
print(a[idx])
'''
[0 2 3]
'''
#可使用花式索引访问多维数组，方法是为每一维指定一个数组，就必须把每一个轴的索引放在一个数组。
A=np.array([[1,2,3],[1,2,3],[1,2,3]])
#要访问索引为(0,1),(1,2)
idx1=np.array([0,1])
idx2=np.array([1,2])
print(A[idx1,idx2])#[2 3]
#索引数组为布尔类型时，布尔数组犹如掩码
a=np.array([0,1,2,3,4,5])
mask=np.array([True,False,True,True,False,True])
print(a[mask])
'''
[0 2 3 5]
'''
#在numpy中索引操作的速度非常快，可使用速度更快的函数numpy.take和numpy.compress来进一步提高性能
#take的第一个参数是要操作的数组，第二个参数是要提取的元素的索引组成的列表，第三个是轴
print(np.take(a,[0,1,2,3],axis=0))
#[0 1 2 3]
                     