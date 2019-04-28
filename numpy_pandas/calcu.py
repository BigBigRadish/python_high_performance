# -*- coding: utf-8 -*-
'''
Created on 2019年4月28日 下午4:12:21
Zhukun Luo
Jiangxi University of Finance and Economics
'''
import numpy as np
'''
numpy默认支持使用广播技术来执行最常见的数学运算，
这包括简单的代数运算，三角运算，取整和逻辑运算。例如，要对数组中的每个元素取平方根，可使用Numpy.sqrt()
'''
print(np.sqrt(np.array([4,9,16])))
#[2. 3. 4.]
#在根据条件筛选元素时，比较运算符很有用，。假设有一个由0-1的随机数组成的数组，而你要提取其中所有的大于0.5的数字，因此可使用>,这将得到一个布尔数组。
a=np.random.rand(5,3)
print(a>0.3)
'''
[[ True False  True]
 [ True  True False]
 [ True  True  True]
 [False  True  True]
 [ True  True  True]]
'''
#然后可使用这个布尔数组作为索引来获取大于0.5的元素
print(a[a>0.5])
#[0.72618883 0.87943884 0.64446662 0.53730454 0.8671388  0.82789113 0.52206837]
#numpy还实现了方法ndarray.sum，它计算特定轴所有元素的和。
a=np.random.rand(5,3)
print(a.sum(axis=0))
#[2.38298388 1.86257948 2.25944983]
print(a.sum(axis=1))#[1.13290309 1.41184008 1.51107743 1.29948387 2.2896167 ]
#若没有制定参数，将作用于扁平化后的数组上
print(a.sum())#6.879605832854221

#计算范数
r_i=np.random.rand(10,2)
norm=np.sqrt(r_i**2).sum(axis=1)
print(norm)
'''
[1.24937353 0.8710457  1.02543865 0.75561074 0.66681118 1.33895009
 1.18980122 1.82093902 1.02400528 1.77647091]
'''