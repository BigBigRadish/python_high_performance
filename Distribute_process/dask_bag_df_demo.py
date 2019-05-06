# -*- coding: utf-8 -*-
'''
Created on 2019年5月6日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#dask bag 和dataframe实例
import dask.bag as dab
dab_at=dab.from_sequence(range(100),npartitions=4)
print(dab_at)#dask.bag<from_se..., npartitions=4>
collection=dab.from_sequence(['the cat sat on the mat','the dog sat on the mat'],npartitions=2)
binop=lambda total,x:total+x['count']
combine=lambda a,b:a+b
print((collection.map(str.split).concat()).map(lambda x:{'word':x,'count':1}).foldby(lambda x:x['word'],binop,0,combine,0).compute())
#dataframe实例
words=collection.map(str.split).concat()
df=words.to_dataframe(['words'])
df.head()
df.words.value_counts().compute()
#dask先对每个pd.series执行value_count,再使用value_counts_aggregate将次数合并
