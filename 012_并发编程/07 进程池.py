#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

'''
限定进程池的大小，确保进程不会因为客户端的请求而无限变大。
'''

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import os,time,random

def task(n):
    print('进程ID:%s is running...' % os.getpid())
    time.sleep(random.randint(1,3))
    return n**2

if __name__ == '__main__':
    executor = ProcessPoolExecutor(max_workers=3)
    futures = []
    for i in range(11):
        future = executor.submit(task,i)
        futures.append(future)
    executor.shutdown(True)

    print('+++>')
    for future in futures:
        print(future.result())