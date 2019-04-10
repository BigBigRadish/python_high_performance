'''
Created on 2019年4月10日
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#joblib存储在本地磁盘
from joblib import Memory
memory=Memory(cachedir='./')
@memory.cache
def sum2(a,b):
    return a+b
# 能够对操作numpy数组的函数进行高效的memoization