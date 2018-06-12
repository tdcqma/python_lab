#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from multiprocessing import Process
import time,os

def task(n):
    print('%s is running...' % os.getpid())
    time.sleep(n)

if __name__ == '__main__':

    p_l = []
    start_time = time.time()
    for i in range(1,4):
        p = Process(target=task,args=(i,))
        p_l.append(p)
        p.start()

    for p in p_l:
        p.join()
    end_time = time.time()

    print('主',(end_time - start_time),os.getpid(),os.getppid())


