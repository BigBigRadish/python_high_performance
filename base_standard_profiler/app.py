# -*- coding: utf-8 -*-
'''
Created on 2019年4月8日 下午3:33:43
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#编写一个粒子运行轨迹类
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.figure import figaspect
class particle:
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
    
                