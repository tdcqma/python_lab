#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

# 示例一：
# class MyClass:
#
#     def __init__(self,work):
#         self.work = work
#
#     def __getattribute__(self, name):
#         print('你正在访问一个存在的属性')
#         return super().__getattribute__(name)
#
#     def __getattr__(self, name):
#         print('您正在访问一个不存在的属性')
#         return super().__getattr__(name)
#
#     def __setattr__(self, name, value):
#         print('您正在设置一个存在的属性的值')
#         return super().__setattr__(name,value)
#
#     def __delattr__(self, name):
#         print('您正在删除一个属性')
#         return super().__delattr__(name)
#
# a = MyClass(1)
# # print(a.NotExist)
# # a.work = 1
# del a.work


# 示例二：

class ObjectDict(dict):
    def __init__(self,*args,**kwargs):
        super(ObjectDict,self).__init__(*args,**kwargs)

    # self:--> {'asf': {'a': 1}, 'd': True}
    # name:--> asf
    def __getattr__(self, name):
        print('name:-->',name)
        print('self:-->',self)
        value = self[name]
        print('value:-->',value)
        if isinstance(value,dict):
            value = ObjectDict(value)
        return value

if __name__ == '__main__':
    od = ObjectDict(asf={'a':1},d=True)
    # print(od.asf)
    print(od.asf.a)
    # print(od.d)


























