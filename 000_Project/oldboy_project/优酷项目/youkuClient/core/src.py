#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma
from core import admin,user


func_dic = {
    '1':admin.admin_view,
    '2':user.user_view,
}

def run():
    while True:
        print(
            '''
            1 管理员视图
            2 用户视图
            '''
        )

        choose = input('please choose>>:').strip()
        if 'q' == choose:break
        if choose not in func_dic:continue
        func_dic[choose]()