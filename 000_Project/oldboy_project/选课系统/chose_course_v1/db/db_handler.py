#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma
from conf import setting
import os
import pickle

'''
思路解析：
select:
    1.两种用途
        用途一：
            判断对象是否存在，以方便后续操作。
                如要先判断学校对象是否存在，才能决定是否可以创建教师等，
                又比如要想创建一个叫admin的管理员，首先要判断这个admin对象是否已经存在，如果不存在则可以创建。
        用途二：
            获取对象并return返回
    2.如何传参
        参数1：name参数，也就是要查找对象的名称
        参数2：type参数，项目根目录下DB文件夹内用于保存pickle序列化后的对象，而对象会分为管理员对象、教师对象、学生对象、
                学校对象和课程对象等。为方便管理对每种不同类型的对象都保存在以各自类名称命名的文件夹内，方便开发者管理和
                程序读取。那么对象在读取的时候要去哪个文件夹下查找呢，这时就需要给出一个参数来标示具体在哪个文件夹里查找，
                因为文件夹命名时是以类名命名的，只要知道这个类的类型就知道在哪个路径下查找，这就是select(obj,type)中
                type的用意了。

save:
    1. 如何传参数
        参数1：obj_name，因为类名就是文件夹名，所以通过【obj_name.__class__.__name__.lower()】获取，
        即对象获取类名，然后把类名全小写化。
    
    2.作用
        用于保存对象，借助pickle序列化到各自对应的文件夹内
'''

def select_or_get_obj(obj_name,obj_type):
    obj_dir = os.path.join(setting.PROJECT_BASE_DB_DIR,obj_type)

    if not os.path.isdir(obj_dir):
        os.mkdir(obj_dir)

    obj_file = os.path.join(obj_dir,obj_name)
    if os.path.exists(obj_file):
        with open(obj_file,'rb') as f:
            return pickle.load(f)
    else:
        return False

def save_obj(obj_name):
    obj_dir = os.path.join(setting.PROJECT_BASE_DB_DIR,obj_name.__class__.__name__.lower())

    if not os.path.isdir(obj_dir):
        os.mkdir(obj_dir)

    obj_file = os.path.join(obj_dir,obj_name.name)
    with open(obj_file,'wb') as f:
        pickle.dump(obj_name,f)
        f.flush()