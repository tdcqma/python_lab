
#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from socket import *
import subprocess

server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8026))
server.listen(5)

conn,client_addr=server.accept()


res1=conn.recv(5)
print(res1)
res2=conn.recv(5)
print(res2)

conn.close()
server.close()

