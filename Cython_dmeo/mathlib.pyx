# -*- coding: utf-8 -*-
'''
Created on 2019年5月1日 下午5:20:50
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#具体函数
cdef int  max(int a ,int b):
    return a if a>b else b
cdef int  min(int a,int b):
    return a if a<b else b
