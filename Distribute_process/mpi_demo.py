# -*- coding: utf-8 -*-
'''
Created on 2019年5月6日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#mpi4py实例
'''
此时需要安装msmpisetup.exe，
按照链接中在windows的安装方法：http://python-parallel-programmning-cookbook.readthedocs.io/zh_CN/latest/chapter3/11_Using_the_mpipy_Python_module.html。
下载msmpisetup.exe,并运行即可。直接下载链接：https://msdn.microsoft.com/en-us/library/bb524831%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396
'''
from mpi4py import MPI
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
print('this is process',rank)
#this is process 0
#使用命令mpiexec -n 4 pyhton mpi_demo.py 将生成四个不同的进程，执行同一脚本，id不同
'''
this is process 0
this is process 1
this is process 2
this is process 3
'''
#点对点通信
import mpi4py.MPI as MPI 
comm = MPI.COMM_WORLD 
comm_rank = comm.Get_rank() 
comm_size = comm.Get_size() 
data_send = [comm_rank] * 4 
comm.send( data_send, dest=(comm_rank+1)%comm_size ) # 如果comm_rank-1<0,会自动加comm_size变为正数
data_recv = comm.recv( source=(comm_rank-1)%comm_size ) 
print( "my rank is %d, I received :" % comm_rank ) 
print( data_recv )


