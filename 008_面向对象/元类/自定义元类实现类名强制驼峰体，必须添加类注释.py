#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

class Mymeta(type):
    '''
    自定义元类
    作用：控制类的产生过程
    '''
    def __init__(self,class_name,class_bases,class_dic):

        super(Mymeta,self).__init__(class_name,class_bases,class_dic)

        if class_name.islower():
            raise TypeError('类名%s请改为驼峰体' % class_name)

        if '__doc' not in class_dic or len(class_dic['__doc__'].strip(' \n')) == 0:
            raise TypeError('类中必须有文档注释,并且文档注释不能为空')

# class oldboyteacher(object,metaclass=Mymeta):
class OldboyTeacher(object,metaclass=Mymeta):

    """
    类OldboyTeacher的文档注释
    """
    school = 'oldboy'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say(self):
        print('%s says welcome to the oldboy to learn python.' % self.name)
