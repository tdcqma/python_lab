'''
我们已经知道，可以用于for循环迭代的数据类型有以下几种：
  一类是集合数据类型：list、tuple、dict、set、str等
  另一类是generator（生成器），包括生成器和带yield的generator function。
  这些可用于for循环迭代的对象统称为Iterable.
  可以使用isinstance()判断一个对象是否是Iterable对象
'''

from collections import Iterable
a = isinstance([],Iterable)
print(a)

a = isinstance({},Iterable)
print(a)

a = isinstance('abc',Iterable)
print(a)

a = isinstance((x for x in range(10)),Iterable)
print(a)

a = isinstance(100,Iterable)
print(a)

