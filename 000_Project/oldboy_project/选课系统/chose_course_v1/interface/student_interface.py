#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma
from db import class_models

def register(student_name,student_password):
    student_obj = class_models.Student.select_or_get_obj(student_name)

    if not student_obj:
        student_obj = class_models.Student()
        student_obj.register(student_name,student_password)
        return True,'\033[1;32mCongratulation, [%s] is register successfully.\033[0m'% student_name
    else:
        return False,'\033[1;31mYou have already registed use [%s],please change your username.\033[0m' % student_name

def student_choose_school(student_name,school_name):
    student_obj = class_models.Student.select_or_get_obj(student_name)
    # 先检查是否已经选择校区，如果已经选择了校区就不能在选了。
    if student_obj.school:
        return False,'\033[1;31mYour have already choosed school.please do not select repeat!\033[0m'
    else:
        student_obj.select_school(school_name)
        return True,'\033[1;32mCongratulation,student:[%s] has selected school:[%s].\033[0m' % (student_name,school_name)


def get_can_choose_course(student_name):
    student_obj = class_models.Student.select_or_get_obj(student_name)
    if student_obj.school:
        school_obj = class_models.School.select_or_get_obj(student_obj.school)
        return True,'success.',school_obj.course_list
    else:
        return False,'please choose school first.',None

def student_choose_course(student_name,course_name):
    '''

    :param student_name:
    :param course_name:
    :return:
    '''

    course_obj = class_models.Course.select_or_get_obj(course_name)
    student_obj = class_models.Student.select_or_get_obj(student_name)
    student_obj.select_course(course_name)
    course_obj.add_student_to_course(student_name)

    return True,'\033[1;32m%s choosed course[%s] successfully.\033[0m'%(student_name,course_name)

def get_student_score(student_name):
    student_obj = class_models.Student.select_or_get_obj(student_name)
    return student_obj.scores

def tell_all_my_course(student_name):
    student_obj = class_models.Student.select_or_get_obj(student_name)
    return student_obj.tell_all_course_list()


