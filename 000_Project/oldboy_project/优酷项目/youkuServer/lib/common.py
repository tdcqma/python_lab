#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import json
import time
import hashlib
from tcpserver import user_data
import struct


# 定义装饰器
def login_auth(func):
    def wrapper(*args,**kwargs):
        # args = (user_dic,conn)
        for value in user_data.alive_user.values():
            if value[0] == args[0]['session']:
                user_id = value[1]
                args[0]['user_id'] = user_id
                break

        user_id = args[0].get('user_id',None)
        if user_id:
            func(*args,**kwargs)
        else:
            back_dic = {'flag':False,'msg':'您不是授权用户。'}
            send_back(back_dic,args[1])

    return wrapper


def send_back(back_dic,conn):
    '''
    tcpserver send data to client
    :param back_dic: 发送到客户端到字典
    :param conn: conn对象
    :return:
    '''

    back_bytes = json.dumps(back_dic).encode('utf-8')
    conn.send(struct.pack('i',len(back_bytes))) # 先发报头，再发实际的内容
    conn.send(back_bytes)

def make_md5(password):
    '''
    transfer password to md5.
    :param password:
    :return:
    '''
    md = hashlib.md5()
    md.update(password.encode('utf-8'))
    return md.hexdigest()

def get_uuid(name):
    '''
    获取随机字符串，用于服务端登录成功后生成cookie的session
    算法： 当前时间+用户名字后，MD5化
    :return:
    '''

    md = hashlib.md5()
    md.update(name.encode('utf-8'))
    md.update(str(time.clock()).encode('utf-8'))    # time.clock()是当前cpu处理线程的时间，绝对唯一
    return md.hexdigest()

def get_nowtime():
    now_time = time.strftime('%Y:%m:%d %X')
    return now_time