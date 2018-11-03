#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import socket

def handle_request(client):
    pass

def main():

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("127.0.0.1",8002))
    sock.listen(5)

    while True:
        print('server is waiting')

        print('hello world')