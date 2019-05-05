# -*- coding: utf-8 -*-
'''
Created on 2019年5月5日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#ProcessPoolExecutor类的用法
import asyncio
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import wait,as_completed
def square(x):
    return x**2
if __name__=='__main__':#需要在main中执行
    executor=ProcessPoolExecutor(max_workers=4)
    fut=executor.submit(square,2)#跟踪函数执行情况
    print(fut.result)#<Future at 0x2484bca2ef0 state=running>
    result=executor.map(square,[0,1,2,3,4])
    print(list(result))#[0, 1, 4, 9, 16]
    #要从多个future中提取结果，可使用函数concurrent.futures.wait和concurrent.futures.as_completed.函数wait将一个future李彪作为参数，并阻塞程序执行，直到所有future都执行完毕，
    #然后使用future.result来提取结果。函数as_completed也将一个函数作为参数，但返回一个包含结果的迭代器
    fut1=executor.submit(square,2)
    fut2=executor.submit(square,3)
    wait([fut1,fut2])
#     print(fut1.result())
#     fut2.result()
    results=as_completed([fut1,fut2])
    print(list(results))
    #还可使用asyncio.run_in_executor来生成future，这样可同时实现并发和并行
    loop=asyncio.get_event_loop()
    fut3=loop.run_in_executor(executor,square,2)
    print(loop.run_until_complete(fut3))#4
    