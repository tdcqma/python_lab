#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma
from db import db_handler
from db import class_models

def register(name,password):
    admin_obj = class_models.Admin.select_or_get_obj(name)
    if not admin_obj:   # 如果admin_obj不存在允许创建admin_obj
        admin = class_models.Admin()
        admin.register(name,password)
        return True,'\033[1;32mCongratulation, [%s] is register successfully.\033[0m'% name
    else:
        return False,'\033[1;31mYou have already registed for [%s],please change your name.\033[0m' % name

def create_school(admin_name,school_name,school_address):
    school_obj = class_models.School.select_or_get_obj(school_name)
    if not school_obj:
        admin_obj = class_models.Admin.select_or_get_obj(admin_name)
        admin_obj.create_school(school_name,school_address)
        return True,'\033[1;32mschool create successfully.\033[0m'
    else:
        return False,'\033[1;31msorry. school already exist.\033[0m'

def create_teacher(admin_name,teacher_name):
    teacher_obj = class_models.Teacher.select_or_get_obj(teacher_name)
    if not teacher_obj:
        admin_obj = class_models.Admin.select_or_get_obj(admin_name)
        admin_obj.create_teacher(teacher_name)
        return True,'\033[1;32mteacher [%s] create successfully.\033[0m' % teacher_name
    else:
        return False,'\033[1;31mteacher [%s] is already exist.\033[0m' % teacher_name

def create_course(admin_name,school_name,course_name,course_price,course_time):
    '''
    创建课程借口
    1) 先确认要创建的课程是否存在
    2) 如果课程不存在则创建，存在则提示无法创建
    3) 把创建好的课程添加到学校的course_list属性里
    :param admin_name:
    :param school_name:
    :param course_name:
    :return:
    '''

    course_obj = class_models.Course.select_or_get_obj(course_name)
    if not course_obj:
        # 创建课程
        admin_obj = class_models.Admin.select_or_get_obj(admin_name)
        admin_obj.create_course(course_name)

        # 将创建好的课程添加到学校course_list
        school_obj = class_models.School.select_or_get_obj(school_name)
        school_obj.add_course_to_school(course_name,course_price,course_time)
        return True,'\033[1;32mCourse [%s] is created successfully.\033[0m' % course_name
    else:
        return False,'\033[1;33mThis course is already exist,please select again.\033[0m'

