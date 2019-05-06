# -*- coding: utf-8 -*-
'''
Created on 2019年5月1日 下午5:20:50
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#具体实现
from mathlib cimport max
def chebyshev(int x1,int y1,int x2 ,int y2):
    return max(abs(x1-x2),abs(y1-y2))