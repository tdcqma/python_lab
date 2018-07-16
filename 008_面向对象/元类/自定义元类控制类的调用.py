#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

'''
通常调用类产生对象，即类()产生对象
但是如果对象()的话会报错。原因在于创建该对象的类中没有__call__方法
'''

# class Foo:
#     def __call__(self, *args, **kwargs):
#         print(self)
#         print(args)
#         print(kwargs)
#         print('ok')
#
#
# obj = Foo()
#
# # 1, 要想让obj这个对象变成一个可调用的对象，需要在该类中定义一个方法__call__方法，该方法会在调用对象时自动触发
# # 2, 调用obj的返回值就是__call__方法的返回值
#
# obj(1,2,3,x=1,y=2)

#
# class Mymeta(type):
#     def __call__(self, *args, **kwargs):
#         print(self)
#         print(args)
#         print(kwargs)
#         return 123
#
# class OldboyTeacher(object,metaclass=Mymeta):
#     school='oldboy'
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def say(self):
#         print('%s says welcome to the oldboy to learn Python.' % self.name)
#
#
# t1 = OldboyTeacher('egon',18)
# print(t1)

#
# class Mymeta(type): #只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
#     def __call__(self, *args, **kwargs): #self=<class '__main__.OldboyTeacher'>
#         #1、调用__new__产生一个空对象obj
#         obj=self.__new__(self) # 此处的self是类OldoyTeacher，必须传参，代表创建一个OldboyTeacher的对象obj
#
#         #2、调用__init__初始化空对象obj
#         self.__init__(obj,*args,**kwargs)
#
#         # 在初始化之后，obj.__dict__里就有值了
#         # print('--->',self.__name__)
#         for k,v in obj.__dict__.items():
#             print('_%s__%s:%s' % (self.__name__,k,v))
#             # {'_OldboyTeacher__name': 'egon', '_OldboyTeacher__age': 18}
#
#         obj.__dict__={'_%s__%s' %(self.__name__,k):v for k,v in obj.__dict__.items()}
#         #3、返回初始化好的对象obj
#         return obj
#
# class OldboyTeacher(object,metaclass=Mymeta):
#     school='oldboy'
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def say(self):
#         print('%s says welcome to the oldboy to learn Python' %self.name)
#
# t1=OldboyTeacher('egon',18)
# print(t1.__dict__)


class Mymeta(type): #只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    n=444

    def __call__(self, *args, **kwargs): #self=<class '__main__.OldboyTeacher'>
        obj=self.__new__(self)
        self.__init__(obj,*args,**kwargs)
        return obj

class Bar(object):
    #n=333
    pass

class Foo(Bar):
    # n=222
    pass

class OldboyTeacher(Foo,metaclass=Mymeta):
    # n=111

    school='oldboy'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say(self):
        print('%s says welcome to the oldboy to learn Python' %self.name)

print(OldboyTeacher.n)