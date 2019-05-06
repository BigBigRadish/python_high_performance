# -*- coding: utf-8 -*-
'''
Created on 2019年4月29日 下午3:27:36
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#编写一个setup.py脚本，就可将.pyx文件直接编译成拓展模块。
from distutils.core import setup
from Cython.Build import cythonize
setup(name='Hello',
      ext_modules=cythonize('hello.pyx'))
