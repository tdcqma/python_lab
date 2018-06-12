'''方式一'''

# from multiprocessing import Process
# import time
#
# def task(name):
#     print('%s is running...' % name)
#     time.sleep(3)
#     print('%s is done' % name)
#
# if __name__ == '__main__':
#     p  = Process(target=task,args=('任务1',))
#     p.start()
#     print('主')

'''方式二'''
# from multiprocessing import Process
# import time
#
# class MyProcess(Process):
#
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print('%s is running...' % self.name)
#         time.sleep(3)
#         print('%s is done.' % self.name)
#
# if __name__ == '__main__':
#     p = MyProcess('egon')
#     p.start()
#     print('主')