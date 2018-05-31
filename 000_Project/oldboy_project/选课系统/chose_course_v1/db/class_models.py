#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma
from db import db_handler

class BaseClass():
    '''
    基类，后边很多类需要继承该类
    '''

    @classmethod
    def select_or_get_obj(cls,name):
        return db_handler.select_or_get_obj(name,cls.__name__.lower())

    def save(self):
        db_handler.save_obj(self)   # 调用db_handler的save_obj将对象保存

class Admin(BaseClass):

    def register(self,name,password):
        self.name = name
        self.password = password
        self.save() # 调用基类BaseClass的save方法，在初始化管理员对象后立刻进行pickle序列化保存。

    def create_school(self,school_name,address):
        school_obj = School(school_name,address)
        school_obj.save()

    def create_teacher(self,teacher_name,teacher_password='123'):
        teacher_obj = Teacher(teacher_name,teacher_password)
        teacher_obj.save()

    def create_course(self,course_name):
        course_obj = Course(course_name)
        course_obj.save()

class School(BaseClass):

    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.course_list = []
        self.course_info = {}

    def add_course_to_school(self,course_name,course_price,course_time):
        self.course_list.append(course_name)
        self.course_info[course_name] = {'price':course_price,'time':course_time}
        self.save()

class Teacher(BaseClass):

    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.course_list = []

    def add_course_to_list(self,course_name):
        self.course_list.append(course_name)
        self.save()

    def tell_teach_course(self):
        return self.course_list

    def edit_student_score(self,student_obj,course_name,score):
        student_obj.scores[course_name] = score
        student_obj.save()

class Course(BaseClass):

    def __init__(self,name):
        self.name = name
        self.student_list = []

    def add_student_to_course(self,student_name):
        self.student_list.append(student_name)
        self.save()

class Student(BaseClass):

    def __init__(self):
        self.school = None
        self.course_list = []
        self.scores = {}

    def register(self,name,password):
        self.name = name
        self.password = password
        self.save()

    def select_school(self,school_name):
        self.school = school_name
        self.save()

    def select_course(self,course_name):
        self.course_list.append(course_name)
        self.scores[course_name] = 0
        self.save()

    def tell_all_course_list(self):
        return self.course_list




