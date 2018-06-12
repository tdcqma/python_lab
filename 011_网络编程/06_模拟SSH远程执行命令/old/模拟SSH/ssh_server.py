#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import socket
import subprocess

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8082))

phone.listen(5)
while True:
    conn,client_addr = phone.accept()
    while True:
        try:
            cmd = conn.recv(1024)
            if not cmd:break
            print('客户端数据：%s' % cmd)

            obj = subprocess.Popen(cmd.decode('utf-8'),shell=True,
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE
                             )

            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            # conn.send(stdout + stderr)  # 浪费内存空间，不推荐使用，替代方案是发送两次，如下所示
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break
    conn.close()
phone.close()