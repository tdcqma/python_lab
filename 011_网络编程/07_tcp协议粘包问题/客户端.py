#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from socket import *
import time
phone=socket(AF_INET,SOCK_STREAM)
phone.connect(('127.0.0.1',8026))

phone.send(b'hello')
# time.sleep(3)
phone.send(b'world')

