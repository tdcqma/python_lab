#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

'''
【1】子类继承父类，子类自动拥有父类的所有功能
'''
# class Animal(object):
#
#     def run(self):
#         print('Animal is running...')
#
# class Dog(Animal):
#     '''
#     Dog继承Animal，有了Animal的run方法
#     '''
#     pass
#
# class Cat(Animal):
#     '''
#     Cat继承了Animal，有了Animal的run方法
#     '''
#     pass
#
# d = Dog()
# d.run() # Animal is running...
#
# c = Cat()
# c.run() # Animal is running...
#
# # 从Dog与Cat继承Animal来看，Dog和Cat的实例均有了父类Animal的全部功能。

'''
[2] 子类继承父类有了父类的所有功能后，也可以在自己的类里面添加自己特有的功能
比如这里新增加的eat函数
'''
# class Animal():
#
#     def run(self):
#         print('Animal is running...')
#
# class Dog(Animal):
#
#     def eat(self):
#         print('Dog is eating...')
#
# class Cat(Animal):
#
#     def eat(self):
#         print('Cat is eating...')
#
# d = Dog()
# d.run() # Animal is running...
# d.eat() # Dog is eating...
#
# c = Cat()
# c.run() # Animal is running...
# c.eat() # Cat is eating...

'''
[3] 通过上面的代码看到，无论是Dog的实例还是Cat的实例，在调用run方法的时候
打印的统统都是Animal is running...  ,正常的逻辑应该是dog的实例打印dog is running, 
而cat的实例应该打印cat is running，这个就需要在各子类中来改写覆盖run方法，
这个实现就是python的多态。

换句话说，子类和父类有相同的方法名，不同的地方在于子类根据自己的需要改写了这个方法
'''

# class Animal():
#     def run(self):
#         print('Animal is running...')
#
# class Dog(Animal):
#     def run(self):
#         print('dog is running...')
#
# class Cat(Animal):
#     def run(self):
#         print('cat is running...')
#
# d = Dog()
# c = Cat()
# d.run() # dog is running...
# c.run() # cat is running...


'''
[4] 多层次理解多态概念：如果在继承关系中，一个实例的数据类型是某个子类，那么
它的数据类型也可以看作是父类，比如下面的代码：
'''
# class Animal():pass
# class Dog(Animal):pass
#
# l = list()
# a = Animal()
# d = Dog()
#
# # 判断一个变量是否是某个类型可以借助isinstance()来判断
# print(isinstance(l,list))
# print(isinstance(a,Animal))
# print(isinstance(d,Dog))    # 在这里d即属于Dog类型
# print(isinstance(d,Animal)) # 也属于它的父类Animal类型
# print(isinstance(a,Dog))    # 但是反过来，父类的实例不会是属于一个子类的数据类型的
#
# # 执行结果：
# #     True
# #     True
# #     True
# #     True
# #     False

'''
[5] 多层次理解多态概念：
我们来编写一个函数，这个函数的作用就是来接受一个Animal类型的变量
'''

class Animal():

    def run(self):
        print('Animal is running...')

class Dog():
    def run(self):
        print('Dog is running...')

def run_twice(animal):
    animal.run()

run_twice(Animal())
run_twice(Dog())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())
