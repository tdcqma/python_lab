#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma
from lib import common
from interface import student_interface
from interface import common_interface

student_status = {
    'name':None
}

def register():
    if student_status['name']:
        print('\033[1;31mYou are logged in and can do other things.\033[0m')
        return

    while True:
        student_name = input('Please input your username:').strip()
        if student_name  == 'q':break
        password = input('please input your password:').strip()
        confirm_password = input('please input your password again:').strip()

        if password == confirm_password:
            flag,res = student_interface.register(student_name,password)
            if flag:
                print(res)
                break
            else:
                print(res)
        else:
            print('\033[1;31mThe passwords you entered do not match.\033[0m')

def login():
    if student_status['name']:
        print('\033[1;31mYou are logged in and can do other things.\033[0m')
        return

    while True:
        student_name = input('Please input your username:').strip()
        if student_name == 'q':break
        student_password = input('Please input your password:').strip()
        flag,res = common_interface.common_login(student_name,student_password,'student')
        if flag:
            student_status['name'] = student_name
            print(res)
            break
        else:
            print(res)
            continue

@common.login_auth(auth_type='student')
def select_school():
    while True:
        exist_school_list = common_interface.get_all_schools()
        if not exist_school_list:
            print('There\'s no school is created,please create school first.')
            return

        print('\033[1;34mschool info:\033[0m')
        for i,school_name in enumerate(exist_school_list):
            print('\033[1;34m  %s | School: %s\033[0m' % (i,school_name))

        school_choose = input('please select school name(Enter num):').strip()
        if school_choose == 'q': break

        if school_choose.isdigit():
            school_choose = int(school_choose)
            if school_choose >= 0 and school_choose < len(exist_school_list):
                flag,res = student_interface.student_choose_school(student_status['name'],exist_school_list[school_choose])
                if flag:
                    print(res)
                    break
                else:
                    print(res)
                    break
            else:
                print('\033[1;31mYour selected school is not exist,please choose again.\033[0m')
        else:
            print('\033[1;31mYour selected school is not exist,please choose again.\033[0m')

@common.login_auth(auth_type='student')
def select_course():
    while True:
        flag,res,can_choose_course_list = student_interface.get_can_choose_course(student_status['name'])

        if not can_choose_course_list:
            print('no course to choose!')
            return

        print('\033[1;34mCourse info:\033[0m')
        for i,course_name in enumerate(can_choose_course_list):
            print('\033[1;34m  %s | CourseName:%s\033[0m' %(i,course_name))

        course_choice = input('please choose course:').strip()
        if course_choice == 'q':break

        if course_choice.isdigit():
            course_choice = int(course_choice)
            if course_choice >= 0 and course_choice < len(can_choose_course_list):
                flag,res = student_interface.student_choose_course(student_status['name'],can_choose_course_list[course_choice])
                if flag:
                    print(res)
                    break
                else:
                    print(res)
            else:
                print('\033[1;31mYour selected course is not exist,please choose again.\033[0m')
        else:
            print('Please input number of course!')

@common.login_auth(auth_type='student')
def look_score():
    score_dic = student_interface.get_student_score(student_status['name'])
    if score_dic:
        for k,v in score_dic.items():
            print('\033[1;34m课程名称:%s\t课程分数:%s\033[0m' %(k,v))
    else:
        print('you have no score!')

@common.login_auth(auth_type='student')
def get_all_my_course():
    all_selected_course_list = student_interface.tell_all_my_course(student_status['name'])
    if all_selected_course_list:
        all_selected_course_list = set(all_selected_course_list)
        print('\033[1;34m已选课程：\033[0m')
        for i,selected_course_name in enumerate(all_selected_course_list):
            print('课程%s : %s' % (i+1,selected_course_name))
    else:
        print('\033[1;31mYou haven\'t choosed course yet,Please chose again.\033[0m')
