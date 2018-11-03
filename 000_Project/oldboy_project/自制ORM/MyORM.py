#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

class Model(dict):
    def __init__(self,**kwargs):
        super(Model,self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('没有属性:%s' % key)

    def __setattr__(self, key, value):
        self[key] = value

class Field:
    '''
    name:字段的名称，如tid、tname
    column_type:字段类型，如int(11)、varchar(32)
    primary_key:主键,如PRIMARY KEY (`tid`)
    default_value:默认值，如NOT NULL

    CREATE TABLE `teacher` (
        `tid` int(11) NOT NULL AUTO_INCREMENT,
        `tname` varchar(32) NOT NULL,
        PRIMARY KEY (`tid`)
    ) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8
    '''

    def __init__(self,name,column_type,primary_key,default_value):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default_value = default_value

class StringField(Field):
    def __init__(self,name,column_type='varchar(100)',primary_key=False,default_value=None):
        super().__init__(name,column_type,primary_key,default_value)

class IntegerField(Field):
    def __init__(self,name,primary_key = False,default_value=0):
        super().__init__(name,'int',primary_key,default_value)

class ModelMetaclass(type):
    def __new__(cls, name,bases,attrs):

        if name == 'Model':
            '''
            如果是Model类，默认不让type进行任何处理，直接返回
            '''
            # type是默认的元类，通过元类创建一个类时需要传三个参数，
            # 分别是类名、基类(要继承的类，默认是object)，类体执行后的名称空间，保存在字典中
            # 下面就是调用type的__new__来初始化一个新的类，给出类名name,基类bases以及类体执行后的字典类型的名称空间attrs
            # 有类这三个参数即可通过type创建出一个类
            return type.__new__(cls,name,bases,attrs)

        # attrs是元类创建类时所需的参数，代表创建类时类体执行后的名称空间，是字典类型，
        # 可以通过get获取字典内key对应的value，如果没有对应的key返回None
        table_name = attrs.get('table_name',None)
        if not table_name:
            table_name = name

        primary_key = None

        for k,v in attrs.items():
            if isinstance(v,Field):
                pass