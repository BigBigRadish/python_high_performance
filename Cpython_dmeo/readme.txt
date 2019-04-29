Cpython是一种拓展python的语言，这是通过支持给函数、变量和类声明类型来实现的。这种类型声明让Cpython能够将python脚本变异成高效的c语言代码。
Cpython还可充当python与c语言的桥梁，因为它提供易于使用的结构，让你能够编写到外部c和c++例程的接口
本章主要内容：
Cpython的基本语法；
如何变异Cpython程序；
如何使用静态类型生成快速代码；
如何使用类型化内存视图高效操作数组；
优化粒子模拟器；
有关jupyter notebook中使用Cpython的提示；
Cpython剖析工具；
一.编译程序
cython hello.pyx

agnostic@hadoop:~/桌面$ gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -lm -I /usr/include/python2.7/ -o hello.so hello.c
agnostic@hadoop:~/桌面$ python
Python 2.7.15rc1 (default, Nov 12 2018, 14:31:15) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import hello
>>> hello.hello()
hello world!
生成了一个xx.so的c语言拓展模块
distutils是标准的python打包工具，使用它编译cython程序更简单。通过编写一个setup.py脚本，就可将.pyx文件直接编译成拓展模块。
如setup.py所示,使用命令 python setup.py build_ext --inplace

