'''
Created on 2019年4月10日
Zhukun Luo
Jiangxi University of Finance and Economics
'''
from functools import lru_cache
@lru_cache()
def sum2(a,b):
    print('Calculating {} +{}'.format(a, b))
    return a+b
print(sum2(1,2))
print(sum2(1,2))
'''
Calculating 1 +2
3
3
'''
#装饰器lru_cache还提供其他功能。要限制缓存区的大小，可使用参数max_size指定保留的元素个数；如果希望缓存区大小不受限制，
#可将参数置为none
#这样，当我们使用不同的参数执行sum2时，缓存区将逐渐增大到16，然后再调用这个函数时，会进行覆盖。前缀lru就是这个策略，最近最少被用
#可使用cache_info查看缓存的性能，还可使用cache_clear清除缓存
print(sum2.cache_info())
#比较fibonacci使用缓存后的性能
def fibonacci(n):
    if n<1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
fibonacci(20)
import timeit
results=timeit.repeat('fibonacci(20)',repeat=1000,number=1)
fibonacci_memoized=lru_cache(maxsize=None)(fibonacci)
