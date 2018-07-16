#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

class_body = """
school = 'oldboy'

def __init__(self,name,age):
    self.name = name
    self.age = age

def say(self):
    print('%s says welcome to the oldboy to learn Python' % self.name)
"""

class_dic = {}
exec(class_body,{},class_dic)
print(class_dic)


