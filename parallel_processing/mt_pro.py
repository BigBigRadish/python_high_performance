# -*- coding: utf-8 -*-
'''
Created on 2019年5月5日 下午2:39:26
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#使用multiprocessing实例
import multiprocessing
import time
class Process(multiprocessing.Process):#继承父类,实现多进程
    def __init__(self,id):#初始化资源
        super(Process,self).__init__()
        self.id=id
    def run(self):
        time.sleep(1.0)
        print('我是进程 {} 号'.format(self.id))#等待一秒钟打印自己的id
def square(x):
        return x**2
if __name__=='__main__':
    p=Process(1)
    p.start()#我是进程 1 号
    #start后面的指令将立即执行，而不是等到p结束再执行，要等到任务结束可使用Process.join()
    p.join()
    #启动多个并行执行的进程
    processes=Process(2),Process(3),Process(4),Process(5)
    [p.start() for p in processes]
    '''
    我是进程 2 号
我是进程 3 号
我是进程 4 号
我是进程 5 号
'''
    #执行顺序无法预测的
    #模块multiprocessing暴露了一个方便的接口，轻松地给驻留在multiprocessing.pool类中的进程分配任务
    #multiprocessing.pool类生成一组工作进程。要提交任务可使用方法apply，apply_async和map/map_async
    '''
1. map() 是一个Series的函数，DataFrame结构中没有map()。map()将一个自定义函数应用于Series结构中的每个元素(elements)。
2. apply()和applymap()是DataFrame结构中的函数，Series中没有。它们的区别在于，apply()将一个函数作用于DataFrame中的每个行或者列，而applymap()是将函数做用于DataFrame中的所有元素(elements)。​
'''
#pool.map对列表中的每一个元素执行指定的函数，并返回一个包含结果的列表，与内置map函数相同。要使用并行映射(map)，必须先初始化一个multiprocessing.pool对象。它将工作进程数作为第一个参数。默认为系统包含的内核数量
    pool=multiprocessing.Pool(processes=4)
    
    inputs=[0,1,2,3,4,5,6]
    outputs=pool.map(square,inputs)#阻塞主程序
    print(outputs)#[0, 1, 4, 9, 16, 25, 36]
    outputs1=pool.map_async(square,inputs)
    print(outputs1)#<multiprocessing.pool.MapResult object at 0x7fd972905690>，不阻塞
    print(outputs1.get())#[0, 1, 4, 9, 16, 25, 36]
    #pool.apply_async将由单个函数组成的任务分配给一个工作进程，它将这个函数及其参数作为参数，返回一个asyncResult对象
    result_async=[pool.apply_async(square,i) for i in range(100)]
    results=[r.get() for r in result_async]
    print(results)

        