# -*- coding: utf-8 -*-
'''
Created on 2019年4月8日 下午8:45:34
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#重写
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.figure import figaspect
import numpy as np
from PIL._imagingmath import add_I

#重写例子模拟器
class particle:
    __slots__=('x','y','ang_vel')
    '''
    在CPython中，当一个A类定义了__slots__ = ('x', 'y')，
    A.x就是一个有__get__和__set__方法的member_descriptor，
    并且在每个实例中可以通过直接访问内存（direct memory access）获得。
    '''
    def __init__(self,x,y,ang_vel):
        self.x=x
        self.y=y
        self.ang_vel=ang_vel
class ParticleSimulator:
    def __init__(self,particle):
        self.particle=particle
    def evolve(self,dt):
        timestep=0.0001
        nsteps=int(dt/timestep)
        
        for i in range(nsteps):
            for p in self.particle:
                #计算方向
                norm=(p.x**2+p.y**2)**0.5
                v_x=-p.y/norm
                v_y=-p.x/norm
                #计算位移
                d_x=timestep*p.ang_vel*v_x
                d_y=timestep*p.ang_vel*v_y
                
                p.x+=d_x
                p.y+=d_y
    #使用numpy改写的evolve程序
    def evolve_numpy(self,dt):
        timestep=0.0001
        nsteps=int(dt/timestep)
        r_i=np.array([[p.x,p.y] for p in self.particle])
        ang_vel_i=np.array([p.ang_vel] for p in self.particle)
        for i in range(nsteps):
            norm_i=np.sqrt((r_i**2).sum(axis=1))
            v_i=r_i[:,[1,0]]#第一列和第二列交换
            v_i[:,0]*=-1
            v_i/=norm_i[:,np.newaxis]#填充成固定维度
            d_i=timestep*ang_vel_i[:,np.newaxis]*v_i
            r_i+=d_i
            for i,p in enumerate(self.particle):
                p.x,p.y=r_i[i]
'''
     使用numpy时，应将数据放在大型数组中，并使用广播功能计算数组。
'''   
def visualize(simulator):
    X=[p.x for p in simulator.particle]
    Y=[p.y for p in simulator.particle]
    
    fig=plt.figure()
    ax=plt.subplot(111,aspect='equal')
    line,=ax.plot(X,Y,'ro')
    
    #指定坐标轴的取值范围
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    
    #这个方法将在动画开始时候运行
    def init():
        line.set_data([],[])
        return line,
    def animate(i):
        #让粒子运动0.01个时间单位
        simulator.evolve(0.01)
        X=[p.x for p in simulator.particle]
        Y=[p.y for p in simulator.particle]
        
        line.set_data(X,Y)
        return line,
    anim=animation.FuncAnimation(fig,animate,init_func=init,blit=True,interval=200)
    plt.show()
    
def test_visualize():
    particles=[particle(0.3,0.5,1),particle(0.0,-0.5,-1),particle(-0.1,-0.4,3)]
    simulator=ParticleSimulator(particles)
    visualize(simulator)
if __name__ == "__main__":
    test_visualize()
                