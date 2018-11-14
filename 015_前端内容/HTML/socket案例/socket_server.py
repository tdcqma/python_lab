#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import socket

sk = socket.socket()
sk.bind(("127.0.0.1",8782),)
sk.listen(5)

while True:
    conn,addr = sk.accept()
    data = conn.recv(1024)
    conn.send(b"hello world!")
    conn.close()