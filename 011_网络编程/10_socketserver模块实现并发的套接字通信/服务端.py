#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import socketserver

# 通信循环
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                data = self.request.recv(1024)
                if not data:break
                self.request.send(data.upper())
            except ConnectionResetError:
                break
        self.request.close()

if __name__ == '__main__':
    # 连接循环
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8033),MyTCPHandler)
    server.serve_forever()