#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

'''
配置文件信息：
    [python]
    name = hello
    age = 123
    salary = 3.1
    is_good = True

    [java]
    name = world
    age = 5555
    salary = 6.1
    is_good = False

    [group1]
    course1 = python
    course2 = java
'''

import configparser

config = configparser.ConfigParser()
config.read('my.ini')

# 判断配置文件里是否有某个属性
print("has_section:",config.has_section('python'))  # True
print("has_section:",config.has_section('Linux'))   # False

# 由于group1选项里分别指向了[python]与[java]两个标签，因此可以有如下调用方式：
print(config.options('group1'))
print(config.get('group1','course1'))
print(config.options(config.get('group1','course2')))

# 通过套用的方式可以读取单独的[]里的选项
print(config.get(config.get('group1','course2'),'name'))