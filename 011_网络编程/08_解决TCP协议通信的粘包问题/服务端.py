#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from socket import *
import subprocess
import struct

server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8081))
server.listen(5)

print('服务的启动...')
while True:
    conn,client_addr = server.accept()
    print(client_addr)

    # 通讯循环
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

            # 1. 先发送固定长度的包头
            total_size = len(stdout) + len(stderr)
            conn.send(struct.pack('i',total_size))

            # 2. 发送真实数据
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError:
            break
    conn.close()
server.close()
