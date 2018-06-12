#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from socket import *
import subprocess

server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8025))
server.listen(5)

# 连接循环
while True:
    conn,client_addr = server.accept()

    # 通信循环
    while True:
        try:
            cmd = conn.recv(1024)
            if not cmd:break
            obj = subprocess.Popen(cmd.decode('utf-8'),shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   )
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            print(len(stdout) + len(stderr))
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError:
            break

    conn.close()

server.close()
