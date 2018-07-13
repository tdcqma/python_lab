#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import os,sys

path = os.path.dirname(__file__)
sys.path.append(path)

from tcpserver import tcpServer

if __name__ == '__main__':
    tcpServer.server_run()