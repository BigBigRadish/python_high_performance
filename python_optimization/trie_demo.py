'''
Created on 2019年4月10日
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#使用trie树进行查询
from random import choice
from string import ascii_uppercase
def random_string(length):
    #生成一个由length个大写ascii字符组成的随机字符串
    return ''.join(choice(ascii_uppercase) for i in range(length))
print(random_string(10))
strings=[random_string(32) for i in range(1000)]
matches=[s for s in strings if s.startswith('AA')]#str.stratswith在其中搜索前缀
print(matches)
from patricia import trie
strings_dict={s:0 for s in strings}#一个所有值都是0的字典
string_trie=trie(**strings_dict)
#要查询与前缀匹配的内容，可使用方法trie.iter，它还回一个迭代器，该迭代器可作用于迭代匹配的字符串
matches=list(string_trie.iter('AA'))
print(matches)
#trie效率是普通字符串匹配的三倍