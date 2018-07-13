#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma
import socket
import struct
import json
import struct

from conf import setting
from threading import Lock
from concurrent.futures import ThreadPoolExecutor   # 导入线程池
from threading import current_thread
from interface import common_interface,admin_interface,user_interface
from tcpserver import user_data
from db import models
from lib import common

# 生成锁，用于创建session时锁定
mutex = Lock()
user_data.mutex = mutex

dispatch_dic = {
    'login': common_interface.login,
    'register': common_interface.register,
    'release_notice': admin_interface.release_notice,
    'check_movie_list':common_interface.check_movie_list,
    'delete_movie':common_interface.delete_movie,
    'upload_movie':admin_interface.upload_movie,
}

def send_back(back_dic,conn):
    head_json_bytes = json.dumps(back_dic).encode('utf-8')
    conn.send(struct.pack('i',len(head_json_bytes))) # 先发报头长度
    conn.send(head_json_bytes)

def dispatch(message_dic,conn):
    '''
    分发器，用于匹配用户想干什么的地方
    :param message_dic:
    :param conn:
    :return:
    '''
    if message_dic['type'] in dispatch_dic:
        dispatch_dic[message_dic['type']](message_dic, conn)
    else:
        back_dic = {'flag': False, 'msg': '请求不合法.'}
        common.send_back(back_dic, conn)

def working(conn,addr):
    while True:
        try:
            head = conn.recv(4)

            head_len = struct.unpack('i',head)[0]
            message = conn.recv(head_len)
            message_dic = json.loads(message.decode('utf-8'))
            message_dic['addr'] = str(addr)
            dispatch(message_dic,conn)
        except Exception as e:
            # 服务端配置会话
            # live_user = {addr:[session],addr:[session],addr:[session]}
            # live_user.pop(addr1)

            print(e)
            conn.close()
            user_data.mutex.acquire()
            user_data.alive_user.pop(addr)
            user_data.mutex.release()
            break

# 创建线程池，提供异步调用，设定线程池大小为10，即最大允许同时十个进程运行。
server_pool = ThreadPoolExecutor(10)

def server_run():
    '''
    建立socket连接
    :return:
    '''
    socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_server.bind(setting.server_address)
    socket_server.listen(5)

    while True:
        conn,addr = socket_server.accept()
        server_pool.submit(working,conn,addr)    # 将任务添加到线程池内，conn是传递到参数