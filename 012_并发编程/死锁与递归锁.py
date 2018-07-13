from threading import Thread,Lock,RLock
import time

# 以下创建两把锁会造成死锁现象，解决方案使用递归锁
# mutexA = Lock()
# mutexB = Lock()

# 递归锁,可以连续acquire()
mutexB = mutexA = RLock()


class Mythread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('\033[45m%s 抢到了A锁\033[0m' % self.name)

        mutexB.acquire()
        print('\033[45m%s 抢到了B锁\033[0m' % self.name)
        mutexB.release()

        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 抢到了B锁' % self.name)
        time.sleep(1)

        mutexA.acquire()
        print('%s 抢到了A锁' % self.name)
        mutexA.release()

        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t = Mythread()
        t.start()