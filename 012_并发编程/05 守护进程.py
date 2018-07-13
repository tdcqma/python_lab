'''
守护进程
    守护：在主进程代码结束的情况下，就立刻死掉。

    守护进程的本质也是一个子进程，该子进程守护着主进程。

为何要用守护进程
    守护进程的本质就是一个子进程，所以在主进程需要将任务并发执行的时候需要开启子进程
    当该子进程执行任务的生命周期伴随主进程整个生命周期的时候，就需要将该子进程做成守护进程。

如何创建守护进程：

'''

# from multiprocessing import Process
# import os,time
#
# def task(x):
#     print('%s is running...' % x)
#     time.sleep(3)
#     print('%s is done' % x)
#
# if __name__ == '__main__':
#     p1 = Process(target=task,args=('守护进程',))
#     p2 = Process(target=task,args=('子进程',))
#     p1.start()
#     p2.start()
#     print('主')

from multiprocessing import Process
from threading import Thread
import time

def foo():
    print('123')
    time.sleep(1)
    print('end123')

def bar():
    print('456')
    time.sleep(3)
    print('end456')

if __name__ == '__main__':
    p1 = Process(target=foo)
    p2 = Process(target=bar)

    p1.daemon = True
    p1.start()
    p2.start()
    time.sleep(0.1)
    print('main------')



























