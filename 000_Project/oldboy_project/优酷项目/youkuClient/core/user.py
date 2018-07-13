#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma
from tcpclient import tcpClient

def user_register():
    pass

def user_login():
    pass

def buy_member():
    pass

def get_movie_list():
    pass

def down_free_movie():
    pass

def down_charge_movie():
    pass

def check_download_record():
    pass

def check_notice():
    pass

func_dic = {
    '1':user_register,
    '2':user_login,
    '3':buy_member,
    '4':get_movie_list,
    '5':down_free_movie,
    '6':down_charge_movie,
    '7':check_download_record,
    '8':check_notice,
}

def user_view():
    client = tcpClient.client_conn()
    while True:
        print('''
            1 注册
            2 登录
            3 充会员
            4 查看视频
            5 下载免费视频
            6 下载收费视频
            7 查看观影记录
            8 查看公告
        ''')

        choose = input('please choose>>:').strip()
        if 'q' == choose:break
        if choose not in func_dic:continue