分布式处理
在计算机集群中，python提供了易于使用且可靠的分布式处理包
本章内容:
分布式计算和MapReduce模型
Dask有向无环图
使用Dask数组，Bag和Dataframe编写并行代码
使用Dask distributed实现分布式并行算法
Pyspark简介
Spark弹性分布式数据集和DataFrame
使用mpi4py进行科学计算
一.分布式计算和MapReduce模型
可以参考我的另外两个项目：
MapReduce：https://github.com/BigBigRadish/DataAnaysisWithHadoop
PySpark：https://github.com/BigBigRadish/spark-machine-learning
二.Dask有向无环图
Dask是一个用于并行和分布式计算的python库，擅长数据分析任务。
Dask最初用于在单机上处理超过内存量的数据集，但是更新后能够在集群中执行任务。Dask支持MapReduce型任务以及复杂的数值算法。
(2.有向无环图)
Dask使用有向无环图(DAG)来表示变量和操作，可使用简单的python字典来表示。如dask_demo.py所示。

