# -*- coding: utf-8 -*-
'''
Created on 2019年5月2日 下午9:11:58
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#模拟网络通信例子
import time
def network_request(number):
    time.sleep(1.0)#睡眠一秒，相当于延迟
    return {'success':True,'result':number**2}
def fetch_square(number):
    response=network_request(number)
    if response['success']:
        print('Result is: {}'.format(response['result']))
fetch_square(2)
fetch_square(3)
fetch_square(4)
#三个请求都是独立的，可以并行处理
'''
Result is: 4
Result is: 9
Result is: 16
'''