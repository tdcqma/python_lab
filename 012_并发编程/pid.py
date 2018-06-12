#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from multiprocessing import Process
import time
import os

def task():
    print('自己成的pid:%s ppid: %s' % (os.getpid(),os.getppid()))
    time.sleep(500)

if __name__ == '__main__':
    p = Process(target=task,)
    p.start()
    print('主：',os.getpid(),os.getppid())