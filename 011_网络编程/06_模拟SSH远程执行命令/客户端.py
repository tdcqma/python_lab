#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from socket import *

client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8025))

while True:
    cmd = input('>>>:').strip()
    if not cmd:continue
    client.send(cmd.encode('utf-8'))

    res = client.recv(1024)
    print(res.decode('utf-8'))

client.close()
