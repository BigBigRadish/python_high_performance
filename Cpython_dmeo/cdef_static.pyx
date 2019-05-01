# -*- coding: utf-8 -*-
'''
Created on 2019年5月1日 下午2:50:50
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#使用cython添加静态类型
import Cython
cdef int i=0 #将变量i声明为16位的整数
#可声明多个变量
cdef double a,b=2.0,c=3.0
#对于类型化标签。
a='hello'
#静态类型让编译器很容易执行优化。如果我们将一个循环所以呢声明为 int类型，Cython将使用纯粹的c代码重写循环，这样就不用依赖python解释器。
'''
#Cython
def example():
    cdef int i,j=0
    for i in range(100):
        j+=1
    return j
#比pypython提升性能100倍
'''
#在Cython中，可将变量声明为任何c语言类型，还可使用经典的c语言结构（如struct，enum和typedef）来定义自定义类型
#如果我们将变量声明为object，就可将任何python对象赋给它，这样对性能并不好有好处
#类型转换
cdef int a=0
cdef double b
b=<double> a
print(b)
#定义函数
cdef int max_py(int a,int b):
    return a if a>b else b
#这样的函数不能在python中使用，只能在Cython中使用
#下面这种都能使用
cpdef int max_py(int a,int b):
    return a if a>b else b
