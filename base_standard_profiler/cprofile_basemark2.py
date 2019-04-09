# -*- coding: utf-8 -*-
'''
Created on 2019年4月8日 下午9:21:00
Zhukun Luo
Jiangxi University of Finance and Economics
'''
from app import ParticleSimulator,particle
from random import uniform
import cProfile
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
    cProfile.run('benchmark()')
'''
         7007 function calls in 0.709 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.709    0.709 <string>:1(<module>)
     1000    0.000    0.000    0.000    0.000 app.py:12(__init__)
        1    0.000    0.000    0.000    0.000 app.py:17(__init__)
        1    0.704    0.704    0.704    0.704 app.py:19(evolve)
        1    0.003    0.003    0.709    0.709 cprofile_basemark2.py:24(benchmark)
     3000    0.001    0.000    0.001    0.000 random.py:360(uniform)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     3000    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {range}
'''
'''
cProfile输出分成5列
ncalls：函数被调用的次数
tottime：执行函数花费的总时间，不考虑其他函数调用
cumtime：执行函数花费的总时间，考虑其它函数调用
percall：单次调用花费的时间-可通过将总时间除以调用次数得到
filename：文件名及其相应的行号
'''

  