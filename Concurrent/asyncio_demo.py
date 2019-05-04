# -*- coding: utf-8 -*-
'''
Created on 2019年5月4日 下午2:24:59
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#asyncio框架使用例子,python3支持
# import asyncio
from asyncio import events
loop=events.get_event_loop()
def callback():
    print('hello,asyncio')
    loop.stop()
loop.call_later(1.0,callback)
loop.run_forever()