#纯粹的python优化
改善应用程序的性能，最有效的方式之一是使用更合适的算法和数据结构。
本章介绍如何使用标准算法和数据结构来增强可伸缩性，并利用第三方库阐述更复杂的用例。本章还将介绍实现缓存的工具，缓存是一种以内存或磁盘空间换取响应时间
的技巧。
本章的内容如下：
计算复杂性
列表和队列
字典
如何使用字典创建反向索引
集
堆和优先队列
使用字典树trie实现自动补全
缓存
使用装饰器functools.lru_cache实现内存缓存
使用joblib.memory实现磁盘缓存
使用推导和生成器实现速度快且占用内存少的循环

一.有用的算法和数据结构
在有些情况下，运行时间可能取决于输入的结构，如集合是否有序，以及是否包含很多重复的元素。本章所说的运行时间指的是平均运行时间。

二.列表和双端队列
python列表是有序的元素集合，在python中使用大小可调整的数组实现的。由一系列连续的存储单元组成，其中每个内存单元都包含指向一个pyhton对象的引用（指针）
在访问，修改和附加元素方面，列表表现特别出色。访问，修改时间复杂度为o（1），，附加操作接近O(1),插入操作O(n)。
在有些情况下，必须高效的执行在集合开头和末尾插入或删除元素的操作，python通过collection.deque类提供了一种具有这种特性的数据结构。deque就是双端队列
，在python中双端队列的实现方式是双向链表。
在列表中 查找元素通常是O(n),这种操作是使用方法list.index来完成的。为提高列表查找速度，确保底层数组有序，并使用模块bisect来执行二分查找。
模块bisect让你能够在有序数组中进行快速查找。对于有序列表，可使用bisect.bisect来确定要插入的位置，同时可确保插入后元素有序。
'''
insert bisect
collection=[1,2,4,5,6]
bisect.bisect(collection,3)
'''
运行时间O(log(N)),但会返回后面的索引，可使用变种bisect.bisect_left

三.字典
字典是以散列映射的方式实现的，在插入，删除，访问的时间复杂度都为O(1).
散列码的通用函数hash
'''
hash('hello')
'''
散列码的实现比较棘手，因为必须处理冲突。对于字符串而言，散列计算与字符串的长度成正比。
'''
#自定义实现counter_dict
def counter_dict(items):
	counter={}
	for item in items:
		if item not in counter:
			counter[item]=0
		else:
			counter[item]+=1
	return counter
#利用collection.defaultdict简化代码
from collections import defaultdict
def counter_defaultdict(items):
	counter=defaultdict(int)
	for item in items:
		counter[item]+=1
	return counter
#collections还包含一个名为Counter的类，可实现同样的目的
from collections import Counter
counter=Counter(items)
上面三种方式使用Counter实现的效率最高
##使用散列映射在内存中创建反向查找索引
如create_search_index.py所示

三.集
#集是一个无序的元素集合，且其中的每个元素必须独一无二，集操作包括并集，差集，交集
在pyhton中，集与字典一样，使用基于散列的算法实现的，因此其加法，删除，和成员成员资格测试等操作的时间复杂度为O(1)，不受集合规模影响

四.堆
堆是一种设计用于快速查找并提取集合中最大值或最小值的数据结构，其典型任务是按优先级处理一系列任务
理论上，可结合使用有序列表和模块bisect中的工具来替代堆，这样提取最大值的时间复杂度为O(1)使用list.pop,但插入操作的时间复杂度仍为O(n),但是
堆的插入和最大值提取操作时间复杂度为O(log(N))
详情见 heapq_demo.py

五.字典树
字典树也被称为前缀树，在列表中查找与前缀匹配的字符串方面，字典树速度很快。非常适合来实现输入时查找和补全功能。实时响应
python标准库并没有提供字典树的实现，但PyPI可找到高效的实现，使用的实现是patricia-trie
详见 trie_demo.py
六.缓存和memoization
智能缓存技术，预先缓存，空间换取时间
python标准库提供了functools，可直接使用基于内存的缓存
通过使用装饰器functools.lru_cache,可轻松缓存函数的结果
详见lru_cache_demo.py
七.joblib
joblib是一个简单的库，提供了基于磁盘的简单的缓存。这个包的用法与lru_cache类似，但结果存储在磁盘，不会随应用程序消失而消失
八.推导和生成器
在python中，推导和生成器表达式是经过极度优化的操作，非常适合来替代显示的for循环，可读性强，速度并不比标准循环高多少，语法更加紧凑
详见 generator_demo.py
九.小结
通过优化算法，可改善应用程序的可伸缩性，使其处理更多数据。