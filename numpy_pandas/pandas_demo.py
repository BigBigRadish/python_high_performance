# -*- coding: utf-8 -*-
'''
Created on 2019年4月28日 下午9:45:37
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#pandas基础
'''
pandas的主要数据结构包括pandas.Series,pandas.Dataframe,pandas.panel.
pd.Series对象和np.array的主要不同在于，pd.Series对象将每个数组元素都关联到一个键。
'''
import pandas as pd
import numpy as np
patients=[0,1,2,3]
effective=[True,True,False,False]
effective_series=pd.Series(effective,index=patients)
print(effective_series)
'''
0     True
1     True
2    False
3    False
dtype: bool
'''
#在pandas中，键不仅是整数，还可以是字符串、浮点数，可散列的python对象
patients=['a','b','c','d']
effective=[True,True,False,False]
effective_series=pd.Series(effective,index=patients)
print(effective_series)
'''
a     True
b     True
c    False
d    False
dtype: bool
'''
#可将pd.series视为一种键值结构，就像python字典
#在pandas中，可将pd.Dataframe对象：多项数据关联到同一个键
patients=['a','b','c','d']
columns={
    'sys_initial':[120,126,130,135],
    'dia_initial':[75,85,90,86],
    'sys_final':[115,123,130,118],
    'dia_final':[70,82,92,87]
    }
df=pd.DataFrame(columns,index=patients)
print(df)
'''
   dia_final  dia_initial  sys_final  sys_initial
a         70           75        115          120
b         82           85        123          126
c         92           90        130          130
d         87           86        118          135
'''
#同样可使用pd.Panel来存储由pd.Dataframe组成的集合。
#访问Serieshe1Dataframe对象的内容，loc根据索引，iloc根据元素在底层数组中的位置访问
print(effective_series.loc['a'])#根据键访问
print(effective_series.iloc[0])#根据位置访问
'''
True
True
'''
#pandas中的索引与字典索引有些不同。字典中每个索引都是独一无二的，而pandas索引可以重复，在索引不是独一无二的情况下性能急速下降，其时间复杂度为O（N）
#,而不像字典为O（1），为了减轻这种影响，可使用二分查找对索引排序

#使用Pandas执行数据库操作
#在pandas中，索引操作的效率极高，因此可执行数据库操作，如计数，连接，分组和聚合
np.log(df.sys_initial)#pd.series是使用np.array来存储数据，计算series的对数
np.log(df)#计算dataframe的对数
#可像Numpy那样，对两个series执行元素运算，根据键而不是位置来匹配操作数
#pandas还可通过便利方法eval支持高效的numexpr式表达式
df.eval('sys_final-sys_initial')

