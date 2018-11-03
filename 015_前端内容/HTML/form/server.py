#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')

        self.write("hello %s,welcome to china,your password is [%s]" % (username,password))

    def post(self, *args, **kwargs):
        self.write("this is a test")

application = tornado.web.Application([
    (r"/index",MainHandler),
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()