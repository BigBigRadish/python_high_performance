# -*- coding: utf-8 -*-
'''
Created on 2019年5月4日 下午4:04:18
Zhukun Luo
Jiangxi University of Finance and Economics
'''
import time
import asyncio
import requests
#阻塞代码重写非阻塞代码
from concurrent.futures import ThreadPoolExecutor
executor=ThreadPoolExecutor(max_workers=5)
def wait_and_return(msg):
    time.sleep(1.0)
    return msg
print(executor.submit(wait_and_return,'hello world'))#<Future at 0x7f64aed00450 state=running>，返回future
loop=asyncio.get_event_loop()
fut=loop.run_in_executor(executor,wait_and_return,'hello world')#<Future pending --more info-->
#这个future仅在启动循环后才会运行。
loop.run_until_complete(fut)#运行循环
#hello world
#便利函数asyncio.gather(一次性提交所有的协程并收集结果)
def fetch_urls(urls):#可以使用aiohttp
    return asyncio.gather(*[loop.run_in_executor (executor,requests.get,url) for url in urls])

    
