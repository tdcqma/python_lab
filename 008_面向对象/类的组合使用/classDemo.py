#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import pickle

class OldboyPeople:
    school = 'oldboy'

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def save(self):
        with open('%s' % self.name,'wb') as f:
            pickle.dump(self,f)

class OldboyStudent(OldboyPeople):
    def __init__(self,name,age,sex):
        OldboyPeople.__init__(self,name,age,sex)
        self.courses = []

    def choose_course(self,course):
        print('%s is choosing course:%s' % (self.name,course))

class Course:
    def __init__(self,name,price,period):
        self.name = name
        self.price = price
        self.period = period

    def tell_info(self):
        print('''
            课程名 : %s
            价格 : %s
            周期 : %s
        ''' % (self.name,self.price,self.period))

python = Course('python',8000,'5mons')
linux = Course('linux',10000,'3mons')

stu1 = OldboyStudent('李三炮',18,'male')
stu1.courses.append(python)
stu1.courses.append(linux)
print('%s的选课信息：' % stu1.name)
for course in stu1.courses:
    course.tell_info()

stu2 = OldboyStudent('李二炮',38,'female')
stu2.courses.append(python)
print('%s的选课信息：' % stu2.name)
for course in stu2.courses:
    course.tell_info()