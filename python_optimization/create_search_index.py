# -*- coding: utf-8 -*-
'''
Created on 2019年4月10日 下午3:44:50
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#创建字典查找索引
#假设包含四个文档的集合
docs=['the cat is under the table',
       'the dog is under the table',
       'cats and dogs smell roses',
       'Carla eats an apple']
#要获取与查询匹配的所有文档，简单方式是扫描每个文档，并检查是否包含制定单词
matches=[doc for doc in docs if 'table' in doc]
print(matches)
'''
['the cat is under the table', 'the dog is under the table']
'''
#一种更佳的策略是花些时间对文档进行预处理，以便查询时更容易找到他们。创建一个反向索引的结构，将集合中的每一个单词都关联到包含该单词的文档列表
#创建索引
index={}
for i,doc in enumerate(docs):
    #遍历每个文档中的每一个单词
    for word in doc.split():
        #创建一个列表，其中包含所有包含制定单词的文档的索引
        if word not in index:
            index[word]=[i]
        else:
            index[word].append(i)
            
results=index['table']
result_documents=[docs[i] for i in results]
print(result_documents)
#查询时间O(1)