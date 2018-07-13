#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

'''
主线程要等待该进程内所有非守护线程（子线程）都死掉才算死掉，因为主线程的生命周期代表了该进程的
生命周期，该进程一定是要等到所有非守护线程都干完活才应该死掉。

可以简单理解为：
    守护线程是要等到该进程内所有非守护线程都运行完毕才死掉。
'''

# from threading import Thread
# import os,time
#
# def task(x):
#     print('%s is running...' % x)
#     time.sleep(3)
#     print('%s is done...' % x)
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=task,args=('守护线程',))
#     t1.daemon = True # 必须放到守护线程start的前边
#     t1.start()
#     print('主')


from threading import Thread
import time

def foo():
    print(123)
    time.sleep(10)
    print('end123')

def bar():
    print(456)
    time.sleep(3)
    print('end456')

if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)

    t1.daemon = True
    t1.start()
    t2.start()
    print('main----')