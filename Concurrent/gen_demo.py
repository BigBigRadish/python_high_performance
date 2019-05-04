# -*- coding: utf-8 -*-
'''
Created on 2019年5月4日 下午2:59:54
Zhukun Luo
Jiangxi University of Finance and Economics
'''
import asyncio
# import asyncio
#生成器使用例子
def range_generator(n):
    i=0
    while i<n:
        print('Generating value {}'.format(i))
        yield i#可以视为一个断点
        i+=1
generator=range_generator(3)
print(next(generator))#使用next函数迭代生成器
print(next(generator))
'''
Generating value 0
0
Generating value 1
1
'''
#可使用yield语句将值注入生成器(不是提取中间值)，可将yield赋给一个变量，将值插入生成器，使用方法send。能够接收值的生成器-基于生成器的协程
def parrot():
    while True:
        message=yield
        print('Zhukun says: {}'.format(message))
generator1=parrot()
generator1.send(None)#将函数执行到第一条yield语句
generator1.send('hello')
generator1.send('world!')
'''
Zhukun says: hello
Zhukun says: world!
'''
#事件循环可以让多个生成器逐步推进，而不阻塞整个程序的执行流程。在相关资源就绪时才推进，从而不需要回调函数。
async def hello():#定义协程
    print('hello,async!')
coro=hello()#返回一个coroutine对象。asyncio不支持next，但可在asyncio事件循环中轻松运行它们，使用方法run_until_complete
print(coro)
loop=asyncio.get_event_loop()
loop.run_until_complete(coro)
#使用async定义的协程也叫原生协程
#模块asyncio提供了资源(awaitable)
async def wait_and_print(msg):
    await asyncio.sleep(1)#await给事件提供了一个断点，因此事件循环可以在等待资源期间管理其他协程
    print('message:',msg)
#重写network_request
async def network_request(number):
    await asyncio.sleep(1.0)
    return {'success':True,'result':number**2}
async def fetch_square(number):
    response=await network_request(number)
    if response['success']:
        print('result is: {}'.format(response['result']))
loop.run_until_complete(fetch_square(2))#分别运行,调试
loop.run_until_complete(fetch_square(3))
loop.run_until_complete(fetch_square(5))
#asyncio提供函数ensure_future，并发运行
asyncio.ensure_future(fetch_square(2))
asyncio.ensure_future(fetch_square(3))
asyncio.ensure_future(fetch_square(5))
loop.run_forever()
#ensure_future,当向它传入一个协程，将返回一个Task实例，既能使用await语法，又能跟踪资源状态

    