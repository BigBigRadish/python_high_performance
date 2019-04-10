# -*- coding: utf-8 -*-
'''
Created on 2019年4月10日 下午5:00:24
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#堆的应用实例
import heapq
collection=[10,3,3,4,5,6]
heapq.heapify(collection)#转换为堆
#要对堆执行插入和提取操作，可使用函数heapq.heappush和heapq.heappop,heappop用于提取最小值
print(heapq.heappop(collection))
'''
3
'''
heapq.heappush(collection, 1)#压入一个数
#另外一种方法是使用queue.PriorityQueue类，它还是线程和进程安全的
from Queue import PriorityQueue
queue=PriorityQueue()
for element in collection:
    queue.put(element)#填充元素
queue.get()#获取最小值
#要获取最大值，可使用简单的技巧，将每个元素都*-1这将反转元素的排列顺序；如果要将每一个元素关联到一个对象上，可插入如（number,object）的元祖，这是因为元组的比较运算符将根据第一个元素进行排序
queue=PriorityQueue()
queue.put((3,'priority 3'))
queue.put((2,'priority 2'))
queue.put((1,'priority 1'))
queue.get()#获取最小值