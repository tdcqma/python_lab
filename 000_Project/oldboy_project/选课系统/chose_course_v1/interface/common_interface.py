#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from db import class_models
from conf import setting
from lib import common

def common_login(name,password,type):
    if type == 'admin':
        obj =class_models.Admin.select_or_get_obj(name)
    elif type == 'teacher':
        obj = class_models.Teacher.select_or_get_obj(name)
    elif type == 'student':
        obj = class_models.Student.select_or_get_obj(name)
    else:
        return False,'error'

    if obj:
        if password == obj.password:
            return True,'\033[1;32m%s[%s] is login successfully.\033[0m' % (type,name)
        else:
            return False,'\033[1;31mPassword incorrect,Please check your password and try again.\033[0m'
    else:
        return False,'\033[1;31m%s:[%s] is not exist,please check again!\033[0m' % (type,name)

def get_all_schools():
    return common.get_all_file(setting.PROJECT_BASE_DB_SCHOOL_DIR)

def get_all_courses():
    return common.get_all_file(setting.PROJECT_BASE_DB_COURSE_DIR)