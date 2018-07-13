#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from multiprocessing import Process
import time
import os

def task():
    print('子进程的pid：%s ppid:%s' % (os.getpid(),os.getppid()))

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    print('这里是主程序...',os.getpid(),os.getppid())