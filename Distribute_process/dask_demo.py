# -*- coding: utf-8 -*-
'''
Created on 2019年5月6日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#dask有向无环图示例
#定义计算图
dsk={'a':2,'b':2,}#每个变量相当于DAG中的一个节点
#添加一个任务，新增一个元组
dsk1={'a':2,'b':2,'result':(lambda x,y:x+y,'a','b')}
from operator import add
dsk2={'a':2,'b':2,'result':(add,'a','b')}
import dask
res=dask.get(dsk2,'result')#get函数为调度器，同步串行方式实现的
print(res)#4
