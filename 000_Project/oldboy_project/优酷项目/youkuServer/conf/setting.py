#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_MOVIE_DIR = os.path.join(BASE_DIR,'movie_dir')


host = '127.0.0.1'
port = 3306
user = 'root'
password = '123456'
database = 'youku2'
charset = 'utf8'
autocommit = True

server_address = ('127.0.0.1',9093)