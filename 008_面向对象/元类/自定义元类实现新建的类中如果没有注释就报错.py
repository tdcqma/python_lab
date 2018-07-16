#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

'''
自定义元类，控制类的产生过程
实现判断新建类中如果没有注释就报错
'''

class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        super(Mymeta,self).__init__(class_name,class_bases,class_dic)

        if '__doc__' not in class_dic.keys():
            raise TypeError('创建类%s时必须添加类注释' % class_name)

class People(object,metaclass=Mymeta):

    country='china'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s is eating' % self.name)