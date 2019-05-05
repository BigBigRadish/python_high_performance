# -*- coding: utf-8 -*-
'''
Created on 2019年4月29日 下午3:27:36
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#编写一个setup.py脚本，就可将.pyx文件直接编译成拓展模块。
from distutils.core import setup
from distutils.extension import  Extension
from Cython.Build import cythonize
Cython_parallel=Extension('Cython_parallel',['Cython_parallel.pyx'],extra_compile_args=['-fopenmp'],extra_link_args=['-fopenmp'])#openMP支持
setup(name='Cython_parallel',
      ext_modules=cythonize('Cython_parallel.pyx'))
# python setup.py build_ext --inplace