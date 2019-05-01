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
2.添加静态类型
在python中，在程序执行期间，变量可关联到不同类型的对象。这种语言很灵活，但也会给解释器带来较大的负担，因为解释器必须在运行阶段确定变量的类型及其包含的方法，这让很多优化难以进行。
Cpython拓展了语言，它支持显示的类型声明，因此能够通过编译生成高效的c语言拓展。
在Cython中，声明数据类型的主要方式是使用cdef语句。如声明变量，函数，拓展类型，见cdef_static.pyx
二.共享声明
编写Cython模块时，你可能想重新组织最常用的函数和类声明，将它们放在一个独立的文件中，以便在不同的模块中重用。在Cython中，可将这些声明放在定义文件中，并使用cimport语句访问它们。
如mathlib.pxd，mathlib.pyx，distance.pyx所示
三.使用数组
高性能数值计算常常用到数组，Cython提供了一种与数组交互的简单方式：直接使用低级C语言数组或更通用的类型化内存视图
(1.)C语言数组和指针
详见Cython_list.py
(2.)Cython中的numpy数组
当你以常规方式访问numpy数组的元素时，在解释器层面将执行其他一些操作，这将带来很大开。cython可避开这些操作和检查，直接操作numPy数组使用的内存区域，从而极大改善性能。
如cy_numpy.py所示
(3.)类型化视图
c数组和numpy数组与内置对象bytes,bytearray和array.array相似，因为它们都在连续的内存区域（内存缓冲区）。Cython提供一个通用接口-类型化内存视图，
该接口统一并简化了对所有上述数据类型的访问。
内存视图是一个对象，维护着一个指向特定内存区域的引用。该内存区域并不归内存视图所有，但内存视图能够读取和修改其内容。换而言之，内存视图是一个有关底层数据的视图。
详见memory_view.pyx



