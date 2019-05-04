# -*- coding: utf-8 -*-
'''
Created on 2018年11月11日 上午11:38:41
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#实现threading.Timer的非线程版本
import time
class Timer:
    def __init__(self,timeout):
        self.timeout=timeout
        self.start=time.time()
    def done(self):
        return time.time()-self.start>self.timeout
timer=Timer(1.0)
while True:
    if timer.done():
        print('Timer is done')
        break
#使用循环不断轮询来等待事件发生，忙等待
class Timer1:
    def __init__(self,timeout):
        self.timeout=timeout
        self.start=time.time()
    def done(self):
        return time.time()-self.start>self.timeout
    def on_timer_done(self,callback):
        self.callback=callback
timer1=Timer1(1.0)
timer1.on_timer_done(lambda :print ('first timer is done'))
while True:
    if timer1.done():
        timer1.callback()
        break
#实现多个定时器
timers=[]
timer2=Timer1(1.0)
timer2.on_timer_done(lambda : print ('first timer is done'))

timer3=Timer1(2.0)
timer3.on_timer_done(lambda : print ('second timer is done'))

timers.append(timer2)
timers.append(timer3)
while True:
    for timer in timers:
        if timer.done():
            timer.callback()
            timers.remove(timer)
    if len(timers)==0：#定时器为空则退出
        break
#事件循环的主要局限性是绝不能用于阻塞调用，事件负责监视资源是否已经就绪，并在就绪后回调函数。可同时监视多项资源。
#事件通知常是通过操作系统调用实现的，操作系统会在事件就绪后恢复程序执行，而不是忙等待。pyhon标准库asyncio就是基于事件循环的并发框架
