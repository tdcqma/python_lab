#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import socket

# 创建socket
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# 建立socket连接
phone.connect(('127.0.0.1',8022))

while True:

    msg = input('>>>:').strip()

    # 发送信息
    phone.send(msg.encode('utf-8'))

    # 接收信息
    data = phone.recv(1024)
    print(data)

# 关闭连接
phone.close()