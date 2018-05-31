#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from interface import admin_interface,teacher_interface,student_interface
from interface import common_interface
from lib import common

admin_status = {
    'name':None
}

def register():

    if admin_status['name']:
        print('\033[1;31mYou are logged in and can do other things.\033[0m')
        return

    while True:
        # \033[1;34m *** \033[0m
        name = input('Please input your name(q to exit):').strip()
        if name == 'q':break
        first_password = input('Please input your password:').strip()
        second_password = input('Please input your confirm password:').strip()

        if first_password == second_password:
            flag,res = admin_interface.register(name,first_password)
            if flag:
                print(res)
                break
            else:
                print(res)
                continue
        else:
            print('\033[1;31mThe passwords you entered do not match.\033[0m')

def login():
    if admin_status['name']:
        print('\033[1;35mYou have already logined.\033[0m')
        return
    while True:
        name = input('Please input your username:').strip()
        if name == 'q':break
        password = input('Please input your password:').strip()
        flag,res = common_interface.common_login(name,password,'admin')
        if flag:
            admin_status['name'] = name
            print(res)
            break
        else:
            print(res)

@common.login_auth(auth_type='admin')
def create_school():
    while True:
        school_name = input('please input school\'s name:').strip()
        if school_name == 'q':break
        school_address = input('please input school\'s address:').strip()
        flag,res = admin_interface.create_school(admin_status['name'],school_name,school_address)
        if flag:
            print(res)
            break
        else:
            print(res)

@common.login_auth(auth_type='admin')
def create_teacher():
    '''
    创建教师
    (1)输入教师用户名密码
    (2)调用admin_interface.create_teacher()借口创建教师
    :return:
    '''
    while True:
        teacher_name = input('please input teacher\'s name:')
        if teacher_name == 'q':break

        flag,res = admin_interface.create_teacher(admin_status['name'],teacher_name)
        if flag:
            print(res)
            break
        else:
            print(res)

@common.login_auth(auth_type='admin')
def create_course():
    '''
    创建课程
    每个学校可能有不同的课程，所以课程是在学校下面被关联的。即，创建课程前先选择课程对应的学校。
    :return:
    '''
    exist_school_list = common_interface.get_all_schools()
    while True:
        if not exist_school_list:
            print('There\'s no school is created,please create school first.')
            return

        for i,school_name in enumerate(exist_school_list):
            print('\033[1;32mID：%s \t SchoolName: %s\033[0m' % (i,school_name))

        school_choose = input('Please select school before you select course(Enter num):').strip()
        if school_choose == 'q':break

        if school_choose.isdigit():
            school_choose = int(school_choose)
            if school_choose >= 0 and school_choose < len(exist_school_list):
                course_name = input('Please input course\'s name:').strip()
                course_price = input('Please input course\'s price: ').strip()
                course_time = input('Please input course\'s time:')
                flag,res = admin_interface.create_course(admin_status['name'],exist_school_list[school_choose],course_name,course_price,course_time)
                if flag:
                    print(res)
                    break
                else:
                    print(res)
            else:
                print('\033[1;31mYour selected school is not exist.\033[0m')
        else:
            print('\033[1;31mPlease enter num of school.\033[0m')