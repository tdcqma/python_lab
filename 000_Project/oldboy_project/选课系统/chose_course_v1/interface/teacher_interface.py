#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma
from db import class_models

def choose_course(teacher_name,course_name):
    teacher_obj = class_models.Teacher.select_or_get_obj(teacher_name)
    teacher_obj.add_course_to_list(course_name)

def get_selected_course(teacher_name):
    teacher_obj = class_models.Teacher.select_or_get_obj(teacher_name)
    return teacher_obj.tell_teach_course()

def get_student_by_course(course_name):
    '''
    通过课程名称获取该课程下所有的学生名称
    :param course_name:
    :return:
    '''
    course_obj = class_models.Course.select_or_get_obj(course_name)
    return course_obj.student_list

def get_all_teached_course(teacher_name):
    teacher_obj = class_models.Teacher.select_or_get_obj(teacher_name)
    return teacher_obj.tell_teach_course()

def teacher_change_student_score(teacher_name,student_name,course_name,score):
    teacher_obj = class_models.Teacher.select_or_get_obj(teacher_name)
    student_obj = class_models.Student.select_or_get_obj(student_name)
    teacher_obj.edit_student_score(student_obj,course_name,score)
