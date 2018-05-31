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
        with open('%s'%self.name,'wb') as f:
            pickle.dump(self,f)

class OldboyStudent(OldboyPeople):
    def choose_course(self,course):
        print('%s is choosing course:%s' % (self.name,course))

class OldboyTeacher(OldboyPeople):
    def __init__(self,name,age,sex,level):
        OldboyPeople.__init__(self,name,age,sex)
        self.level = level

    def score(self,stu):
        print('%s is scoring %s' %(self.name,stu.name))

stu1 = OldboyStudent('sanfeng',18,'f')
print(stu1.__dict__)

tea1 = OldboyTeacher('taidi',20,'m',10)
print(tea1.__dict__)