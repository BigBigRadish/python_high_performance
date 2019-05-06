# -*- coding: utf-8 -*-
'''
Created on 2019年5月1日 下午7:14:43
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#c语言数组和指针
cdef double a
from libc.stdio cimport printf
printf("%p",&a)
#声明指针
from libc.stdio cimport printf
cdef double b
cdef double *b_pointer
b_pointer=&b
b=3.0
printf("%p",*b_pointer)
#需要简历到既有c语言库的借口或需要细致地控制内存时，应使用c语言数组和指针，而且他们的性能都非常高。为提高安全性可使用NUmpy和类型化内存视图
