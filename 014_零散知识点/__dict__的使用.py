#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

'''
对象调用.__dict__返回对象的所有属性，不包括函数数据
类调用.__dict__返回类所有的属性，不包括对象里的属性
'''

class Friends():
    def __init__(self):
        self.name = 'xxx'
        self.gender = 'female'

def say_to_friend():
    print('hello python')


if __name__ == '__main__':
    f = Friends()
    print('f.__dict__:',f.__dict__)
    print()
    print('Friends.__dict__:',Friends.__dict__)