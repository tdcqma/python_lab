#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

'''
实验方法与效果：
    1. 运行该脚本
    2. 浏览器访问http://127.0.0.1:8000/后即可出现"Hello World"内容
'''

import socket

def handle_request(client):
    buf = client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n",encoding='utf-8'))
    client.send(bytes("Hello World",encoding='utf-8'))

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',8000))
    sock.listen(5)
    while True:
        connection,address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()