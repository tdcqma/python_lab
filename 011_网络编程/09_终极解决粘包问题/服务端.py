#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from socket import *
import struct
import subprocess
import json

server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8001))
server.listen(5)

# 连接循环
while True:
    conn,client_addr = server.accept()
    print('client_addr:',client_addr)

    # 通信循环
    while True:
        try:
            cmd = conn.recv(1024)
            print('用户输入的数据是：',cmd.decode('utf-8'))
            if not cmd:continue

            obj = subprocess.Popen(cmd.decode('utf-8'),shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   )

            stdout = obj.stdout.read()
            stderr = obj.stderr.read()


            # 制作报头
            header_dic = {
                'filename':'a.txt',
                'total_size':len(stdout) + len(stderr),
                'sha-256':'78974328a567313874d0801f1e05411e93c48f765cfa668314432f783c5a8e48',
            }

            #将报文序列化
            header_json = json.dumps(header_dic)
            header_bytes = header_json.encode('utf-8')

            # 1. 先发送报头本身的长度
            conn.send(struct.pack('i',len(header_bytes)))

            # 2. 在发送报头
            conn.send(header_bytes)

            # 3. 最后发送真实的数据
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError:
            break
    conn.close()
server.close()