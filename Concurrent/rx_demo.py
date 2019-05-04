# -*- coding: utf-8 -*-
'''
Created on 2019年5月4日 下午7:02:01
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#响应式编程实例，RxPY
from rx import Observable
from rx.testing.marbles import on_next, on_completed
from rx.core.py2.observable import Observable
obs=Observable.from_iterable(range(4))#基于迭代器创建数据流，为此可使用工厂方法Observable.from_iterable
#要接受来自obs的数据，可使用方法Observable.subscrible，这样将对数据源发射的每个值执行传入的函数
# obs.subscribe(print)
'''
0
1
2
3
有序集合
'''
#Observable是由Observer和iterable组合而成的。观察者是一个对象，可迭代对象能够生成并跟踪迭代器。生成器是一种特殊的迭代器
#注册一个观察者，并使用参数on_next和on_completed注册了两个回调函数，这两个回调函数将分别在下一项数据可用及没有更多数据时被调用。
obs.subscribe(on_next=lambda x : print(on_text='Next item: {}'),on_completed=lambda:print('no more data'))
'''
Next item: 1
Next item: 2
Next item: 3
Next item: 4
no more data
'''
#我们可以使用处理迭代器的方法来处理事件流
obs2=obs.take(1)#返回一个观察者
#Next item: 1
#运算符
Observable.from_iterable(range(4)).map(lambda x:x**2).subscribe(print)#求平方
'''
0
1
4
9
'''
obs=(Observable.from_iterable(range(4)).group_by(lambda x :x%2))#按奇偶分组
obs.subscribe(lambda x: print('group key:',x.key))#提取键值
obs.take(1).subscribe(lambda x:x.subscribe(print))#返回一个观察者并打印
#rxpy提供操作merge和concat，用他们来合并独立的观察者
#merge_all()和concat_all()。前者接受多个观察者，并生成一个观察者，其中包含接受的被观察者中的所有元素，而这些元素的排列顺序与发射顺序相同。
#而后者返回一个新的观察者，先发射第一个观察者的元素，再发射第二个观察者的元素。
#observable.interval接受一个以毫秒为单位的时间段(参数period)，并创建一个每隔指定时间就发射一个值的被观察者。
obs=Observable.interval(1000)
obs.take(4).subscribe(print)
'''
0
1
2
3
'''
#订阅之后才会启动
#interval生成的观察者称为惰性的，请求才会生成值。
#publish为hot类型的

