#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

# 判断类的实例a_obj里是否有name属性或run方法属性

class Atest():
    name = 'hello'

    def run(self):
        print('run method')

a_obj = Atest()
print(hasattr(a_obj,'name'))
print(hasattr(a_obj,'run'))
print(hasattr(a_obj,'run2'))

'''
输出结果：
    True
    True
    False
'''