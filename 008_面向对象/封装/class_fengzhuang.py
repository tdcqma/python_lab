#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

class Foo:

    __n = 1 # _Foo__n=1

    def __init__(self,name):
        self.__name = name  # _Foo__name

    def __f1(self): # _Foo__f1
        print('f1')

# print(Foo.__n)  # AttributeError: type object 'Foo' has no attribute '__n'
# print(Foo.__f1) # AttributeError: type object 'Foo' has no attribute '__f1'

#obj = Foo('egon')
# print(obj.__name)   # AttributeError: 'Foo' object has no attribute '__name'

#obj = Foo('egon')
# print(obj.__dict__) # {'_Foo__name': 'egon'}

#print(Foo.__dict__) # '_Foo__n': 1 ...


