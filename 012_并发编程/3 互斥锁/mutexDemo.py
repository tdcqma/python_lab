#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from threading import Thread
from multiprocessing import Process,Lock
import os,random,time
import json

mutex = Lock()  # 创建互斥锁

def check():
    with open('db.json','rt',encoding='utf-8') as f:
        dic = json.load(f)
    print('%s 剩余票数:%s' % (os.getpid(),dic['count']))

def get():
    with open('db.json','rt',encoding='utf-8') as f :
        dic = json.load(f)
    time.sleep(1)

    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(random.randint(1,3)) #模拟网络延迟
        with open('db','wt',encoding='utf-8') as f:
            json.dump(dic,f)
            print('%s 抢票成功' % os.getpid())

def task(mutex):

    # 并发查看
    check()

    # 穿行购票
    # mutex.acquire()
    get()
    # mutex.release()

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=task,args=(mutex,))
        p.start()


