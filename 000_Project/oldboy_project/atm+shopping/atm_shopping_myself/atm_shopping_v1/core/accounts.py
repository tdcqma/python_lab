#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import json
import datetime
from core import db_handler
from conf import settings
import os

def load_current_balance(acc_data,account_id):
    '''
    从用户db文件读取用户的所有信息
    :param account_id:
    :return:
    '''

    # db_path 路径指向ATM/db/accounts目录
    db_path = db_handler.db_handler(settings.DATABASE)  # settings.DATABASE可以直接通过导入包获得

    # account_id就是用户名，在被调用时传参就可以获得
    # db_path是用户数据文件的上层目录名称，后面是用户名.json，最后account_file得到的是db/accounts/用户名.json文件
    # 也就是用户的所有信息
    # account_file = '%s/%s.json' % (db_path,account_id)
    account_file = '%s/%s.json' % (db_path,acc_data['account_data']['id'])

    # 找到了用户数据文件的路径，就可以通过文件的读操作来获取用户的所有信息，保存在acc_data中并作为函数的返回值返回。
    with open(account_file) as f :
        acc_data = json.load(f) # 读取用户文件保存到acc_data中
        return acc_data

def dump_account(account_data):
    '''
    将更新后的数据写入用户db文件内
    :param account_data:
    :return:
    '''

    # db_path 路径指向ATM/db/accounts目录
    db_path = db_handler.db_handler(settings.DATABASE)

    # account_data['id'] 代表用户名
    # 以下语句通过将ATM/db/accounts目录与以用户名.json拼接的方式得到用户数据文件的绝对路径
    # 即：account_file = /ATM/db/accounts/用户名.json
    account_file = "%s/%s.json" % (db_path,account_data['id'])

    # 通过json.dump()写入数据
    with open(account_file,'w') as f:
        acc_data = json.dump(account_data,f)

    # 写入成功后返回True
    return True

def is_existUser(user_id):
    '''
    注册用户 - 判断用户id是否存在
    :param user_id:
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    user_names = [] # 存放所有的用户id
    for root, dirs, files in os.walk(db_path):
        for line in files:
            user_names.append(line.split('.')[0])

    reg_flag = False
    for line in user_names:
        if user_id == line: # 用户存在
            reg_flag = False
        else:
            reg_flag = True

    if reg_flag:
        return True
    else:
        return False

def transfer_existUser(user_id):
    '''
    转账操作 - 判断收款用户是否存在
    :param user_id: 收款用户ID
    :return:
    '''
    trans_flag = False
    db_path = db_handler.db_handler(settings.DATABASE)
    user_names = []
    for root,dirs,files in os.walk(db_path):
        for line in files:
            user_names.append(line.split('.')[0])

    for line in user_names:
        if int(user_id) == int(line):  # 用户存在其中，可以转账
            trans_flag = True

    if trans_flag:  # 用户存在，可以转账，返回真
        return True

def user_register(acc_dic):
    '''
    用户注册功能
    :param acc_dic: 用户注册需要填写的信息，保存在字典中
    :return: 返回注册是否成功
    '''

    # 用户的注册日期变量，获取当前日期，更新到用户注册信息字典中
    today = datetime.date.today()
    acc_dic['enroll_date'] = str(today)

    # 调用函数判断用户是否已注册
    is_reg = is_existUser(acc_dic['id'])

    if is_reg:
        # 获取用户数据存放的目录，此处db_path指向ATM/db/accounts/
        # account_file 指向ATM/db/accounts/***.json文件
        db_path = db_handler.db_handler(settings.DATABASE)
        account_file = "%s/%s.json" % (db_path,acc_dic['id'])

        with open(account_file,'w') as f :   # 打开account_file,通过json.dump（)将用户注册信息的字典文件写入
            acc_data = json.dump(acc_dic,f)

        return True

def get_allUser(acc_data):
    '''
    获取数据库所有用户
    :param acc_data:
    :return:
    '''

    # 获取保存用户数据的目录名称，此处指向ATM/db/accounts目录
    accounts_path = '%s/db/accounts' % settings.BASE_DIR

    users = []
    for root,dirs,files in os.walk(accounts_path):
        for user in files:
            # print(user.split('.')[0])
            # print(user.split('.')[0],type(user.split('.')[0]))
            if user.split('.')[0] != '001':
                users.append(user.split('.')[0])

    return users

def lock_user(acc_data,lockUser_id):
    '''
    锁定用户，读取锁定用户的数据文件，将status状态改为-1，即锁定用户的状态
    :param acc_data:管理员001用户的数据
    :param lockUser_id: 被锁定用户的ID,str类型
    :return:
    '''

    # 获取待锁定用户的数据文件路径
    account_file_path = '%s/%s.json' % (settings.DB_ACCOUNTS_DIR,lockUser_id)

    # 打开文件，将被锁定用户的数据文件读取到lock_user_data中保存
    lock_user_data = ''
    with open(account_file_path,'r') as f:
        lock_user_data = json.load(f)

    print('待锁定用户信息：',lock_user_data)

    # 判断待锁定用户是否已被锁定
    if lock_user_data['status'] == 0: # 正常用户（status=0）可以进行锁定，锁定后的status值变为-1
        lock_user_data['status'] = -1

        # 将更新后的lock_user_data 重新写入数据库内，并返回锁定成功的True
        with open(account_file_path,'w') as f:
            json.dump(lock_user_data,f)
        return True
    else:
        print('该用户已被锁定，请勿重复锁定！')