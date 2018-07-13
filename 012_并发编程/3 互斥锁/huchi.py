import json
import os
import time
import random
from multiprocessing import Process

def check():
    with open('db.json','rt',encoding='utf-8') as f:
        dic = json.load(f)
    print('%s 剩余票数：%s' % (os.getpid(),dic['count']))


def get():
    with open('db.json','rt',encoding='utf-8')as f :
        dic = json.load(f)
    time.sleep(1)

    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(random.random(1,3))
        with open('db.json','wt',encoding='utf-8') as f:
            json.dump(dic,f)
            print('%s 抢票成功' % os.getpid())

def task():
    # 并发查看
    check()

    # 穿行购票
    get()


if __name__ == '__main__':
    for i in range(10):
        p = Process(target=task)
        p.start()
