#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma
import os
import json
import time

from core import db_handler
from conf import settings
from core import logger

def acc_auth(account,password):
    '''
    account auth function
    :param account:  接收用户名
    :param password:    接收用户密码
    :return: 如果通过认证返回用户认证信息的一个对象，否则返回None
    '''

    db_path = db_handler.db_handler(settings.DATABASE)   # 获取到认证文件的目录
    account_file = "%s/%s.json" % (db_path,account)  # 每个用户都是单独一个认证文件，拼接目录与用户名文件以获取该用户文件的绝对路径，相当于数据库
    print(account_file)

    if os.path.isfile(account_file):    # 判断用户信息的文件是否存在，不存在则说明没有这个用户
        with open(account_file,'r',encoding='utf-8') as f:

            # json.load的文件必须为json后缀的文件，key与value需要用到引号时需要使用双引号
            # 本例中调用的位置为db/accounts/用户名.json，返回结果为字典格式且保存至account_data中
            account_data = json.load(f)

            if account_data['password'] == password:    # 因文件名存在则证明用户存在，此处仅需判断密码即可。
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'],'%Y-%m-%d')) # 判断将用户信用卡有效期，将过期日期转换为时间戳形式
                if time.time() > exp_time_stamp:    # 如果程序运行时间大于过期时间的时间戳，则提示信用卡到期。
                    print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
                else:
                    return account_data # 用户认证成功且在有效期内的话返回该用户对象（字典格式）
    else:
        print("\033[31;1mAccount [%s] does not exist!\033[0m")

def acc_login(user_data,log_obj):
    '''

    :param user_data:
    :param login_obj:
    :return:
    '''

    retry_count = 0 # 统计登录失败次数,次数小于3次允许认证，大于3次时进行日志记录并退出程序
    while user_data['is_authenticated'] is not True and retry_count < 3 :
        account = input('\033[32;1maccount:\033[0m').strip()
        password = input('\033[32;1mpassword:\033[0m').strip()
        auth = acc_auth(account,password)

        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        retry_count += 1
    else:
        log_obj.error("account [%s] too many login attempts" % account)


