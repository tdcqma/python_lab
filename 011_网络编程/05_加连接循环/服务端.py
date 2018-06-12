#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8022))
phone.listen(5)

while True:
# 等待连接
    conn,client_addr = phone.accept()
    print('conn信息：',conn)
    print('client_addr信息:',client_addr)

    while True:
        try:
            # 收消息
            data = conn.recv(1024)
            if not data:break   # 针对linux系统
            print('客户端数据：',data)

            # 发消息
            conn.send(data.upper())
        except ConnectionResetError:
            break

    conn.close()
phone.close()
