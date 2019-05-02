# -*- coding: utf-8 -*-
'''
Created on 2019年5月2日 下午5:09:08
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#python原生模式及对象模式
import numba as nb
import numpy as np
x=np.random.rand(1000)
@nb.jit(["float64(float64[:])","float64(float32[:])"])
def sum_sq2(a):
    result=0
    N=len(a)
    for i in range(N):
        result+=a[i]
    return result
sum_sq2(x.astype('float32'))
print(sum_sq2.inspect_types())
'''

    # --- LINE 13 --- 
    #   a = arg(0, name=a)  :: array(float64, 1d, A)
    #   $const0.1 = const(int, 0)  :: Literal[int](0)
    #   result = $const0.1  :: float64
    #   del $const0.1

    result=0

    # --- LINE 14 --- 
    #   $0.2 = global(len: <built-in function len>)  :: Function(<built-in function len>)
    #   $0.4 = call $0.2(a, kws=[], args=[Var(a, /home/agnostic/git/python_high_performance/JIT_tools/numba_ys_obj.py (13))], func=$0.2, vararg=None)  :: (array(float64, 1d, A),) -> int64
    #   del $0.2
    #   N = $0.4  :: int64
    #   del $0.4
    #   jump 18
    # label 18

    N=len(a)
'''
#打印为这个函数的每个版本推断出的类型，对于每一行，numba都打印有关变量，函数和中间结果的详细描述。
#每个变量都有明确的类型，这种编译方式成为原生模式。
#反例：对字符串的操作有限
@nb.jit
def concatenate(strings):
    result=''
    for s in strings:
        result+=s
    return result
concatenate(['hello','world'])
print(concatenate.signatures)#[(reflected list(str),)]
print(concatenate.inspect_types())
'''
    # --- LINE 46 --- 
    #   strings = arg(0, name=strings)  :: pyobject
    #   $const0.1 = const(str, )  :: pyobject
    #   result = $const0.1  :: pyobject
'''
#每个变量都是通用类型pyobject，这意味着不能求助于python解释器，numba无法对这个函数进行编译。而且编译版本比原始版本慢3倍。增加了额外开销
#这种模式称为对象模式
#可强制使用原生模式
@nb.jit(nopython=True)
def concatenate1(strings):
    result=''
    for s in strings:
        result+=s
    return result
concatenate1(['hello','world'])#numba.errors.TypingError: Failed in nopython mode pipeline (step: nopython frontend)
#报错，这样就可以确保所有的代码的速度很快且指定了正确的类型