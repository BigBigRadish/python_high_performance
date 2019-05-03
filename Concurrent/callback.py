# -*- coding: utf-8 -*-
'''
Created on 2019年5月3日 下午3:01:08
Zhukun Luo
Jiangxi University of Finance and Economics
'''
import time
import threading
#回调函数
def wait_and_print(msg):
    time.sleep(1.0)
    print(msg)
#非阻塞式程序
def wait_and_print_async(msg):
    def callback():
        print(msg)
    timer=threading.Timer(1.0,callback)
    timer.start()
#其主要特征是其中所有语句都不会阻塞程序的执行，threading.Timer的策略是启动一个新的线程，该线程能够并行执行代码。
wait_and_print(1.0)
wait_and_print(2.0)
wait_and_print_async(1.0)
wait_and_print_async(2.0)
#这种注册回调函数，以便在特定事件发生时执行它的方式称为好莱坞原则
#先提交，提交之后，接着往前走
#重写network_request()
def network_request_async(number,on_done):
    def timer_done():
        on_done({'success':True,'result':number**2})
    timer=threading.Timer(1.0,timer_done)
    timer.start()
def on_done(result):
    print(result)
network_request_async(2, on_done)
network_request_async(3, on_done)
def fetch_square(number):
    def on_done(response):
        if response['success']:
            print('Result is: {}'.format(response['result']))
    network_request_async(number, on_done)
fetch_square(1)
fetch_square(2)
'''
1.0
2.0
1.0
2.0
{'result': 4, 'success': True}
{'result': 9, 'success': True}
Result is: 1
Result is: 4
'''
    
    