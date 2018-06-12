#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from socket import *
import struct
import json

client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8001))

while True:
    cmd = input('>>:').strip()
    if not cmd:continue
    client.send(cmd.encode('utf-8'))

    # 1.先接收报头长度
    obj = client.recv(4)
    header_size = struct.unpack('i',obj)[0]

    # 2.再接收报头内容
    header_bytes = client.recv(header_size)
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)
    # print(header_dic)

    # 3. 获取真是数据的大小
    total_size = header_dic['total_size']

    # 循环接收真实数据，直到收干净为止
    recv_size = 0
    res = b''
    while recv_size < total_size:
        recv_data = client.recv(1024)
        res += recv_data
        recv_size += len(recv_data)

    print(res.decode('utf-8'))

client.close()