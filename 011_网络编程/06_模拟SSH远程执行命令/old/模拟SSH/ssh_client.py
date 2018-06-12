#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8082))
print('SSH客户端')
while True:s
        msg = input('root@test#:').strip()
        if not msg:continue
        phone.send(msg.encode('utf-8'))
        data = phone.recv(1024)
        if not data:continue
        print(data.decode('utf-8'))

phone.close()