from multiprocessing import Queue,Process
import time

def producer(name,q):
    for i in range(5):
        res = '包子%s' % i
        time.sleep(1)
        print('\033[45m厨师%s生产了%s\033[0m' % (name,res))
        q.put(res)

def consumer(name,q):
    while True:
        res = q.get()
        time.sleep(2)
        print('\033[47m吃货%s吃了%s\033[0m' %(name,res))

if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=producer,args=('egon',q))
    c1 = Process(target=consumer,args=('alex',q))

    p1.start()
    c1.start()
    print('主。。。')