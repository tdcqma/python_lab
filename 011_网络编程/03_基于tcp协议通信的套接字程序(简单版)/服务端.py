#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8021))
phone.listen(5)

# 等待连接
conn,client_addr = phone.accept()
print(conn)
print(client_addr)

# 收消息
data = conn.recv(1024)
print('客户端数据：',data)

# 发消息
conn.send(data.upper())

conn.close()
phone.close()
