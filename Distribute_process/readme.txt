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
三.使用Dask数组，Bag和Dataframe编写并行代码
Dask的主要用途是自动生成并行数组操作，可以极大地简化规模超过内存容量的数组处理工作。Dask采用的策略是，将数组分割为大量的子单元-Dask块
Dask在模块dask.array中实现了一个类似于numpy的数组接口。要从numpy数组创建一个dask数组，可使用函数dask.from_array.这个函数要求你指定块大小，并返回一个dask.array对象，而
dask.array对象负责将原始数组分割为指定大小的子单元，如da_array_demo.py所示。
(2.Dask Bag and Dataframe)
Dask提供了其他用于自动生成计算图的数据结构。dask.bag.bag和dask.dataframe.DataFrame，前者是一种通用的元素集合，可用来编写MapReduce算法代码，后者是pandas.Dataframe的分布式版本
如dask_bag_df_demo.py所示。
四.使用Dask distributed实现分布式并行算法
Dask的单机版本使用的是基于线程或者进程的调度器。分布式后端实现，可用在计算机网络上创建和运行Dask图
默认情况下，Dask将在本地计算机上启动几个重要的进程。要通过Client实例调度和执行分布式任务，这些进程必不可少。Dask集群的主要组件是一个调度器和一系列工作进程。
调度器负责将工作分配给工作进程并监视和管理结果的进程。在使用函数（如nogil块中的numpy，pandas，和Cython函数）不会获取GIL，这样可实现并行性。Client向调度器提交一系列任务，对于每个任务
，都将获得一个future实例。用于跟踪资源。Dask distributed不仅提交任务，还将计算结果缓存到工作进程的内存中。Dask还提供用于诊断的WebUI，可用来监视状态以及在集群上执行的每项任务花费的时间。
五.mpi4py执行科学计算
常用于超算，这种系统用来实现并行的库主要是MPI(消息传递接口),适合用来运行数千个几乎不互相发送数据的进程。
在MPI中，并行性是通过在多个可能位于不同节点上的进程中运行同一脚本实现的。进程之间的通信和同步由一个专门的进程处理，这个进程为root，ID0标识。
如mpi_demo.py所示
