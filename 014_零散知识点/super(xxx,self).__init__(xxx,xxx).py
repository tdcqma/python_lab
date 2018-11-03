#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

class A:
    def __init__(self,xing,gender):
        self.namea = 'aaa'
        self.xing = xing
        self.gender = gender

    def funca(self):
        print('function a : %s' % self.namea)

class B(A):
    def __init__(self,xing,age):
        super(B,self).__init__(xing,age)
        self.nameb = 'bbb'
        self.namea = 'ccc'
        self.xing = xing.upper()
        self.age = age

    def funcb(self):
        print('function b: %s' % self.nameb)

b = B('xi',22)
print(b.namea)
print(b.nameb)
print(b.xing)
print(b.age)
b.funca()
b.funcb()