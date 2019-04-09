# -*- coding: utf-8 -*-
'''
Created on 2019年4月9日 下午3:17:52
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#cprofile+kcachegrind+app
#三个泰勒展开式
def factorial(n):#阶乘
    if n==0:
        return 1.0
    else:
        return n*factorial(n-1)
def taylor_exp(n):
    return [1.0/factorial(i) for i in range(n)]
def taylor_sin(n):
    res=[]
    for i in range(n):
        if i%2==1:
            res.append((-1)**((i-1)/2)/float(factorial(i)))
        else:
            res.append(0.0)
    return res
def benchmark():
    taylor_exp(500)
    taylor_sin(500)
if __name__ == "__main__":
    benchmark()
'''
访问剖析信息，首先需要生成cprofile输出文件
python -m cProfile -o prof.out taylor.py
然后使用pyprof2calltree将输出文件转换并启动kcachegrind
'''

