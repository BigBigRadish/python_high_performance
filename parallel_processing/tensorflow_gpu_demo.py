# -*- coding: utf-8 -*-
'''
Created on 2019年5月6日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#tensorflow gpu编程
import tensorflow as tf
import time
import numpy as np
N=5000
a_data=np.random.rand(N,N)
b_data=np.random.rand(N,N)
#创建一个图
# with tf.device('/gpu:0'):
a=tf.placeholder('float32')
b=tf.placeholder('float32')
c=tf.matmul(a,b)
gpu_options = tf.GPUOptions(allow_growth=True)
with tf.Session(config=tf.ConfigProto(gpu_options=gpu_options)) as sess:#动态分配显存
    start=time.time()
    sess.run(c,{a:a_data,b:b_data})
    print('Matrix multiply ({})took: {}'.format(N,time.time()-start))#Matrix multiply (5000)took: 1.076734781265258