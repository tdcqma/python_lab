#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from socket import *
import struct

client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8081))

while True:
    cmd = input('>>:').strip()
    if not cmd:continue
    client.send(cmd.encode('utf-8'))

    # 1.先接收保头,struct发送的数据大小为4
    header = client.recv(4)
    # 解压,解压后得到的结果是元祖，类似(17,)取出第一个值即可
    total_size = struct.unpack('i',header)[0]

    # 循环接收数据，直到数据接收干净为止
    recv_size = 0
    res = b''
    while recv_size < total_size:
        recv_data = client.recv(1024)
        res += recv_data
        recv_size += len(recv_data)
    print(res.decode('utf-8'))

client.close()

