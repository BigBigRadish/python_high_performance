# -*- coding: utf-8 -*-
'''
Created on 2019年5月2日 下午7:28:23
Zhukun Luo
Jiangxi University of Finance and Economics
'''
#JI类
#自定义Node类
import numba as nb
class Node:
    def __init__(self,value):
        self.next=None
        self.value=value
class LinkedList:#实现链表
    def __init__(self):
        self.head=None
    def push_front(self,value):
        if self.head==None:
            self.head=Node(value)
        else:
            #替换链表头
            new_head=Node(value)
            new_head.next=self.head
            self.head=new_head
    def show(self):
        node=self.head
        while node is not None:
            print(node.value)
            node=node.next
lst=LinkedList()
lst.push_front(1)
lst.push_front(2)
lst.push_front(3) 
lst.show()#321
@nb.jit
def sum_list(lst):
    result=0
    node=lst.head
    while node is not None:
        result+=node.value
        node=node.next
    return result
lst1=LinkedList()
[lst1.push_front(i) for i in range(1000)]
# print(sum_list(lst1))#无法推断类型
#可使用装饰器nb.jitclass 来编译Node和LinkedList类，装饰器接受一个参数，其中包含被装饰类的属性的类型。
#首先必须先声明属性，在定义类，使用nb.deferred_type()函数，其次属性next可以使NOne，也可以是一个Node实例，这被称为可选类型，nb.optional
node_type=nb.deferred_type()
node_spec=[('next',nb.optional(node_type)),('value',nb.int64)]
@nb.jitclass(node_spec)
class Node1:
    def __init__(self,value):
        self.next=None
        self.value=value
node_type.define(Node.class_type.instance_type)
ll_spec=[('head',nb.optional(Node.class_type.instance_type))]
@nb.jitclass(ll_spec)
class LinkedList1:#实现链表
    def __init__(self):
        self.head=None
    def push_front(self,value):
        if self.head==None:
            self.head=Node(value)
        else:
            #替换链表头
            new_head=Node(value)
            new_head.next=self.head
            self.head=new_head
    def show(self):
        node=self.head
        while node is not None:
            print(node.value)
            node=node.next
lst2=LinkedList1()
[lst2.push_front(i) for i in range(1000)]
#性能很大提升