#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import os

def login_auth(auth_type):
    '''
    登录装饰器
    :param auth_type:
    :return:
    '''
    from core import admin,teacher,student
    def auth(func):
        def wrapper(*args,**kwargs):
            if auth_type == 'admin':
                if not admin.admin_status['name']:
                    print('\033[1;31mYou have not log on,Pleae log on first.\033[0m')
                    admin.login()
                else:
                    return func(*args,**kwargs)
            elif auth_type == 'teacher':
                if not teacher.teacher_status['name']:
                    print('\033[1;31mYou have not log on,Pleae log on first.\033[0m')
                    teacher.login()
                else:
                    return func(*args,**kwargs)
            elif auth_type == 'student':
                if not student.student_status['name']:
                    print('\033[1;31mYou have not log on,Pleae log on first.\033[0m')
                    student.login()
                else:
                    return func(*args,**kwargs)
        return wrapper
    return auth

def get_all_file(file_dir):
    '''
    用于返回某一目录下所有的文件名，保存到列表里。
    如：指定school则返回所有到学校名，指定teacher则返回所有的教师名称
    :param file_dir:
    :return:
    '''
    file_list = os.listdir(file_dir)
    return file_list

