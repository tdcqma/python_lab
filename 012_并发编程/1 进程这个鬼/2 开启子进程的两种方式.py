#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from multiprocessing import Process
import time

'''
# 创建子进程方式一 #
'''
# class MyProcess(Process):
#
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print('%s is running...' % self.name)
#         time.sleep(3)
#         print('%s is done...' % self.name)
#
#     def func(self):
#         print('new func')
#
# if __name__ == '__main__':
#     p = MyProcess('sanfeng')
#     p.start()
#     print('这里是主进程...')
#     p.func()
#
# # 解读上述p.start()
#     # p.start() 只是给操作系统发送一个开启子进程的信号，真正执行会在调用资源的
#     # 过程中浪费一部分时间。而这些时间足以导致发好这个信号后后面的print操作被先执行了。
#     # 所以你看到的输出效果是：
#     '''
#     这里是主进程...
#     new func
#     sanfeng is running...
#     sanfeng is done...
#     '''
#     # 而不是
#     '''
#     sanfeng is running...
#     sanfeng is done...
#     这里是主进程...
#     new func
#     '''


'''
# 创建子进程方式二
'''

def task(name):
    print('%s is running...' % name)
    time.sleep(3)
    print('%s is done...' % name)

def func():
    print('new func')

if __name__ == '__main__':
    p = Process(target=task,args=('任务1',))
    p.start()
    print('这里是主进程...')
    func()