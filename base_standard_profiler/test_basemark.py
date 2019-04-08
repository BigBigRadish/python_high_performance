# -*- coding: utf-8 -*-
'''
Created on 2019年4月8日 下午9:21:00
Zhukun Luo
Jiangxi University of Finance and Economics
'''
from app import ParticleSimulator,particle
from random import uniform
def test_evolve():
    particles=[particle(0.3,0.5,1),particle(0.0,-0.5,-1),particle(-0.1,-0.4,3)]
    simulator=ParticleSimulator(particles)
    simulator.evolve(0.1)
    p0,p1,p2=particles
    def fequal(a,b,eps=1e-5):
        return abs(a-b)<eps
    assert fequal(p0.x, 0.210269)
    assert fequal(p0.y,0.543863)
    assert fequal(p1.x, -0.099334)
    assert fequal(p1.y,-0.490034)
    
    assert fequal(p2.x, 0.191358)
    assert fequal(p2.y, -0.365227)
def benchmark():
    particles=[particle(uniform(-1.0,1.0),uniform(-1.0,1.0),uniform(-1.0,1.0)) for i  in range(1000)]#生成1000个随机测试用例
    simulator=ParticleSimulator(particles)
    simulator.evolve(0.1)
     
if __name__ == "__main__":
#     test_evolve()    
    benchmark()
'''
计算基准测试程序的运行时间，使用unix命令time，可轻松测量任何进程的执行时间
time有三个指标：
real：从头到尾运行进程实际花费的时间，与人用秒表测量的时间相当
user：从计算期间，所有cpu所花费的时间
sys：在执行与系统相关的任务（如内存分配）期间。所有cpu花费的时间
在有些情况下，user+sys>real,这是因为可能有多个处理器在并行的工作
user适合监控cpu的性能
'''   