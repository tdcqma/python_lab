#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from socket import *

server = socket(AF_INET,SOCK_DGRAM) # SOCK_DGRAM 为数据报协议，改协议每个数据都自带数据头，所以无粘包问题。
# 无绑定server地址
# 无粘包问题，一发对应一收
#
server.bind(('127.0.0.1',8093))

while True:
    msg,client_addr = server.recvfrom(1024)
    if msg.decode('utf-8') == 'q':break
    server.sendto(msg.upper(),client_addr)