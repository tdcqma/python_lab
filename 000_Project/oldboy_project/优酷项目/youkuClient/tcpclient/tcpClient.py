#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import socket
from conf import setting


def get_client():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(setting.server_address)
    return client