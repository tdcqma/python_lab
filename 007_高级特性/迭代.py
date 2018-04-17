# 如果给定一个list或tuple，我们可以通过for循环进行遍历，这种方式就成为迭代（Iteration）
# 在python中迭代是通过for...in... 来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的，比如Java代码：
# for (i=0; i<list.length; i++) {
#    n = list[i];
# }

#从以上java的例子可以看出，python的抽象程度高于java的for循环，因为python 的for循环不仅可以
#应用与list或tuple循环中，还可以用于其他可迭代的对象上，list这种数据类型虽然有下标，但很多其他
#数据都没有下标的，但是python中无论有没有下标，只要是可迭代对象都可以迭代，比如dict就可以迭代。

d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)

# 因为dict的存储顺序不像list一样顺序存储，所以迭代的结果顺序可能不一样。
# 默认情况下，dict迭代的就是key的值，如果要迭代value可以用for value in d.value(),
# 如果要迭代key-value可以用for k,v in d.items()

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,v)

# 由于字符串也是可以迭代的对象，因此也可以用于for循环
for ch in 'ABCDEFG':
    print(ch)
# 所以用python的迭代时，不关心是list还是其他数据类型，只要是可迭代的都可以迭代。
# 那么如何判断一个对象是可迭代对象呢，方法是通过collections模块的iterable类型来判断。

from collections import Iterable
print('判断abc是否可迭代：',isinstance('abc',Iterable))
print('判断[1，2，3]是否可迭代：',isinstance([1,2,3],Iterable))
print('判断123是否可迭代：',isinstance(123,Iterable))

# 如果要对list实现像java那样的下标循环怎么办呢，python内置的enumerate函数
# 可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身了。

for i,value in enumerate(['A','B','C']):
    print(i,value)

# 在上面的for循环中同时引入了两个变量，在python里也是很常见的，如下：
for x,y in [(1,1),(2,2),(3,3)]:
    print(x,y)



