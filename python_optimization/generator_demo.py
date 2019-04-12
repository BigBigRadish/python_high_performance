# -*- coding: utf-8 -*-
'''
Created on 2019年4月12日 下午4:44:31
Zhukun Luo
Jiangxi University of Finance and Economics
'''
import time 
from memory_profiler import profile
def cal_time(func): 
    def call_func(): 
        print("开始运行") 
        start_time = time.time() 
        # print(start_time) 
        func() 
        end_time = time.time() 
        # print(end_time) 
        print(end_time-start_time,'seconds') 
    return call_func

@cal_time
def loop():
    res=[]
    for i in range(100000):
        res.append(i*i)
    return sum(res)
@cal_time
def comprehension():
    return sum([i*i for i in range(100000)])
@cal_time
def generator():
    return sum(i*i for i in range(100000))
loop()
comprehension()
generator()
#与列表一样使用字典推导来生成字典，效率会高一些
def loop_dict():
    res={}
    for i in range(100000):
        res[i]=i
def comprehension_dict():
    return {i:i for i in range(100000)}
#要实现高效的循环，可结合使用迭代器和filter，map等函数
#map函数接收两个参数-一个函数和一个迭代器，并返回一个生成器，该生成qi,该生成器将函数应用于集合中的每一个元素。这种操作是在迭代期间进行的，动态计算你节省内存
@profile
def map_normal(numbers):
    a=map(lambda n :n*2,numbers)
    b=map(lambda n:n**2, a)
    c=map(lambda n:n**0.33, b)
    return max(c)
numbers=range(100000)
map_normal(numbers)
'''
   45                             def map_normal(numbers):
    46     33.9 MiB      0.6 MiB       a=map(lambda n :n*2,numbers)
    47     37.0 MiB      0.8 MiB       b=map(lambda n:n**2, a)
    48     40.1 MiB      0.8 MiB       c=map(lambda n:n**0.33, b)
    49     40.1 MiB      0.0 MiB       return max(c)
'''
