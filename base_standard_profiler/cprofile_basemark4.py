# -*- coding: utf-8 -*-
'''
Created on 2019年4月8日 下午9:21:00
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#memory profiler
from app import ParticleSimulator,particle
from random import uniform
from memory_profiler import profile
import sys
def test_evolve():
    particles=[particle(0.3,0.5,1),particle(0.0,-0.5,-1),particle(-0.1,-0.4,3)]
    simulator=ParticleSimulator(particles)
    simulator.evolve(0.1)
    p0,p1,p2=particles
    def fequal(a,b,eps=1e-5):
        return abs(a-b)<eps
    assert fequal(p0.x, 0.210269,eps=1e-5)
    assert fequal(p0.y,0.543863,eps=1e-5)
    assert fequal(p1.x, -0.099334)
    assert fequal(p1.y,-0.490034)
    
    assert fequal(p2.x, 0.191358)
    assert fequal(p2.y, -0.365227)
@profile
def benchmark():
    particles=[particle(uniform(-1.0,1.0),uniform(-1.0,1.0),uniform(-1.0,1.0)) for i  in range(1000)]#生成1000个随机测试用例
    simulator=ParticleSimulator(particles)
    simulator.evolve(0.1)
     
if __name__ == "__main__":
#     test_evolve()    
    benchmark()
'''
Filename: /home/agnostic/git/python_high_performance/base_standard_profiler/cprofile_basemark4.py

Line #    Mem usage    Increment   Line Contents
================================================
    26     70.3 MiB     70.3 MiB   @profile
    27                             def benchmark():
    28     70.4 MiB      0.2 MiB       particles=[particle(uniform(-1.0,1.0),uniform(-1.0,1.0),uniform(-1.0,1.0)) for i  in range(1000)]#生成1000个随机测试用例
    29     70.4 MiB      0.0 MiB       simulator=ParticleSimulator(particles)
    30     70.4 MiB      0.0 MiB       simulator.evolve(0.1)
'''

  