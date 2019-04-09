# -*- coding: utf-8 -*-
'''
Created on 2019年4月8日 下午9:21:00
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#line profiler
from app import ParticleSimulator,particle
from random import uniform
import line_profiler
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
def benchmark():
    particles=[particle(uniform(-1.0,1.0),uniform(-1.0,1.0),uniform(-1.0,1.0)) for i  in range(1000)]#生成1000个随机测试用例
    simulator=ParticleSimulator(particles)
    simulator.evolve(0.1)
     
if __name__ == "__main__":
#     test_evolve()    
    
    prof = line_profiler.LineProfiler(benchmark)
    prof.enable()  # 开始性能分析
    benchmark()
    prof.disable()  # 停止性能分析
    prof.print_stats(sys.stdout)
'''
Timer unit: 1e-06 s

Total time: 1.90074 s
File: /home/agnostic/git/python_high_performance/base_standard_profiler/cprofile_basemark3.py
Function: benchmark at line 26

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    26                                           def benchmark():
    27      1001       2375.0      2.4      0.1      particles=[particle(uniform(-1.0,1.0),uniform(-1.0,1.0),uniform(-1.0,1.0)) for i  in range(1000)]#生成1000个随机测试用例
    28         1          2.0      2.0      0.0      simulator=ParticleSimulator(particles)
    29         1    1898363.0 1898363.0     99.9      simulator.evolve(0.1)
'''
'''
line:运行的代码行号
Hits:代码行运行的次数
Time：代码行的执行时间，单位为微秒
Per HIt：时间/次数
Time：代码行总执行时间所占百分比
line contents：代码行内容
'''

  