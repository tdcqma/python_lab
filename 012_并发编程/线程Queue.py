import queue

# 队列，先进先出
#
# q = queue.Queue(3)
# q.put(1)
# q.put(2)
# q.put(3)
#
# print(q.get())
# print(q.get())
# print(q.get())


# 堆栈，先进后出
# q = queue.LifoQueue(3)
# q.put(1)
# q.put(2)
# q.put(3)
#
# print(q.get())
# print(q.get())
# print(q.get())

# 优先级队列：优先级高的先出来，数字代表优先级，数字越小优先级越高。
#
# q = queue.PriorityQueue(3)
# q.put((13,'lxx'))
# q.put((10,'egon'))
# q.put((11,'alex'))
#
# print(q.get())
# print(q.get())
# print(q.get())