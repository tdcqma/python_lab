#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

class_name = 'HelloWorld'
class_bases=(object,)
class_dic = {}
class_body = """
name = 'python'

def __init__(self,name):
    self.name = name

def look(self):
    print('%s is looking...' % (self.name))
"""

exec(class_body,{},class_dic)

Hw = type(class_name,class_bases,class_dic)
# print(Hw,type(Hw))

hwok = Hw('ok')
# print(hwok.__dict__)
hwok.look()