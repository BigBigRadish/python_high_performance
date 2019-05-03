# -*- coding: utf-8 -*-
'''
Created on 2019年5月3日 下午4:19:03
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#future详解
#创建future类实例
from concurrent.futures import Future
import threading
fu=Future()
print(fu)#<Future at 0x7f9108d106d0 state=pending>
#future表示一个还不可用的值，pending即未确定。要让结果可用，可使用方法Future.set_result
fu.set_result('hello')
print(fu)#<Future at 0x7f75beedb6d0 state=finished returned str>
print(fu.result())#hello
'''
设置结果后，Future将指出任务结束，可使用.result()访问结果。还可给future制定一个回调函数，这样一旦结果可用，就将执行这个回调函数。
要指定回调函数，只需向方法Future.add_done_callback传递一个函数即可。这样任务结束后指定的函数将被调用，并将future实例作为第一个参数。
'''
fut=Future()
fut.add_done_callback(lambda future:future.result())
fut.set_result('hello')
#重写network_request_async
#不再接受回调函数on_done,因为可使用add_done_callback关联到回调函数。通过set_result作为回调函数传递给threading.Timer，这次可以返回一个值
def network_request_async(number):
    future=Future()
    result={'success':True,'result':number**2}
    timer=threading.Timer(1.0,lambda: future.set_result(result))
    timer.start()
    return future
fut=network_request_async(2)
def fetch_square(number):
    fut=network_request_async(number)
    def on_done_future(future):
        response=future.result()
        if response['success']:
            print('Result is: {}'.format(response['result']))
    fut.add_done_callback(on_done_future)
fetch_square(1)
fetch_square(2)
'''<Future at 0x7f0353dd0850 state=pending>
<Future at 0x7f0353dd0850 state=finished returned str>
hello
Result is: 1
 Result is: 4
'''
#future提供了一种使用回调函数的方式，且更加方便。因为它能跟踪资源状态，撤销已调度的任务及更自然地方式处理异常


