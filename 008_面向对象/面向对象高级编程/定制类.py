# 看到类似__slots__这种形如__xxx__的变量或这函数名就要注意，这些在python中是有特殊用途的。
# __slots__ 的作用就是限定有外部创建的属性，__len__()方法为了能让class作用于len()函数。

# 初次之外，python的class中还有许多这样有特殊用户的函数，可以帮助我们定制类。

# 《 __str__ 》
# 我们先定义一个Student类，打印一个实例：

class Student(object):
    def __init__(self,name):
        self.name = name

print(Student('Michael'))
# 打印了一堆<__main__.Student object at 0x102a23438>，不好看。
# 我们可以定义好__str()__方法，返回一个好看的字符串就可以了。

class Student(object):

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
print(Student('Michael'))

# 这样打印出来的实例不仅好看，而且很容易看出实例内部重要的数据。
# 但是直接乔变量不用print，打印出来的实例还是不好看。
# 下面这个例子在交互式下可以实验。

s = Student('Michael')
s

'''
是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的
字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，
有个偷懒的写法：
'''
class Student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name = %s) ' % self.name

    __repr__ = __str__

print('----------------------------__iter__--------------------------------')

# __iter__

# 如果一个类想被用于for ... in 循环，类似list或tuple那样，就必须实现一个__iter__方法，
# 该方法返回一个迭代对象，然后python的for循环就会不断调用该迭代对象的__next__()方法拿到
# 循环的下一个值，知道遇到StopIteration错误时退出循环。

# 我们以斐波那契数列为例，写一个Fib类，可以作用域for循环

class Fib(object):

    def __init__(self):
        self.a,self.b = 0,1 # 初始化两个记数器a,b

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b  = self.b ,self.a + self.b # 计算下一个值

        if self.a > 100000: # 退出循环条件
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

print('----------------------------__getitem__--------------------------------')
# __getitem__

# Fib实例虽然能作用于for循环，看起来和list和tuple有点像，但是，把它当作list来使用
# 还是不行，比如，获取第5个元素

#print(Fib()[3])
# 会报错：TypeError: 'Fib' object does not support indexing

# 要表现的像list那样按照下标取出元素需要实现__getitem__()方法：

class Fib(object):
    def __getitem__(self, n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a
# 现在访问任意一项，输入下标即可

f = Fib()
s1 = f[1]
s2 = f[2]
s3 = f[3]
s10 = f[10]

print(s1,s2,s3,s10)

# 但是,list有个神奇的切片方法：

a = list(range(100))
print(a)
b = list(range(100))[5:10]
print(b)

# 但是，对于Fib却会报错，原因是__getitem__()传入的参数可能是一个int，也可能是一个
# 切片对象slice，所以要做判断：


class Fib(object):

    def __getitem__(self, n): # n 是索引
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a , b = b , a+b
            return a

        if isinstance(n,slice):
            start = n.start
            stop = n.stop

            if start is None:
                start = 0
            a, b = 1,1

            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a , b  = b , a+b
            return L

# 现在试试Fib的切片：
print('----')
f = Fib()
print(f[0:5])
print(f[:10])
print(f[2:5])

# 执行结果：
# [1, 1, 2, 3, 5]
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# [2, 3, 5]

# 但是没有对step参数的处理：

print(f[:10:2])
#打印#  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# 如果把对象看成dict，__getitem__()的参数也可能是一个可以作为key和object，
# 例如str

print('----------------------------__getattr__--------------------------------')

# 正常情况下，当我们调用类的方法或属性时，如果不存在就会报错，比如定义Student类

class Student(object):

    def __init__(self):
        self.name = 'Michael'

# 调用name属性，没问题，但是调用不存在的score属性，就有问题了：

s = Student()
print(s.name)

# 调用不存在的属性时报错：AttributeError: 'Student' object has no attribute 'score'
# print(s.score)

# 错误信息很清楚的告诉我们，没有找到score这个attribute。
# 要避免这个错误，除了可以加上一个score属性外，python还有另一个机制，那就是写
# 个__getattr__()方法，动态返回一个属性，修改如下：

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

# 当调用不存在的属性时，比如score，python解释器会试图调用__getattr__(self,'score')来尝试获得属性，
# 这样，我们就有机会返回score的值：

s = Student()
print(s.name)
print(s.score)

# 返回函数也是完全可以的：

class Student(object):

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25


print('----------------------------__getattr__--------------------------------')

# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用
# 能不能直接在实例本身上调用呢？ 在python中，答案是肯定的。

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。

class Student(object):
    def __init__(self,name):
        self.name = name

    def __call__(self):
        print('my name is %s' % self.name)

# 调用方式如下所示：

s = Student('Michael')
print(s())

# __call__()还可以定义参数，对实例进行直接调用就好比对一个函数进行调用一样，所以
# 你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没撒区别。

