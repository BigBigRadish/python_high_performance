# -*- coding: utf-8 -*-
'''
Created on 2019年5月5日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#同步和锁示例
import multiprocessing
shared_variable=multiprocessing.Value('f')
shared_variable=0
#使用共享内存，必须考虑同时访问的问题
#定义一个进程类
lock=multiprocessing.Lock()
class Process(multiprocessing.Process):
    def __init__(self,counter):
        super(Process,self).__init__()
        self.counter=counter
    def run(self):
        for i in range(1000):
            with lock: #获取锁，同步元语
                self.counter.value+=1
def main():
    counter=multiprocessing.Value('i',lock=True)
    counter.value=0
    processes=[Process(counter) for i in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]#until task END
    print(counter.value)
if __name__=='__main__':
    main()#3450
    #需要同步对共享变量的访问，确保每次只有一个进程访问该变量
    #multiprocessing.Lock()提供同步功能获取锁使用acquire,释放使用release,也可将锁用作上下文管理
    
    