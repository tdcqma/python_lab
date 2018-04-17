# map()函数接收两个参数，一个是函数，另一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把
# 结果作为新的Iterable返回。

# 举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
# 用python代码实现：

def f (x):
    return x * x
r = map(f,[1,2,3,4,5,6,7,8,9,10])
print(list(r))

# map传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterable,Iterable是一个惰性序列，因此通过list()函数让它把整个
# 序列都计算出来并返回一个list
# 你可能会想，不需要map（）函数，写一个循环也可以结算出结果。
L = []
for n in [1,2,3,4,5,6,7,8,9,10]:
    L.append(f(n))
print(L)

# 的确可以，但是，从上面的循环代码，能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”吗？
# 所以，map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x*x，
# 还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串

a = list(map(str,[1,2,3,4,5,6,7,8,9,10]))
print(a)
# 只需要一行代码。


# 《reduce》

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 比方说对一个序列求和，就可以用reduce实现：

from functools import reduce
def add (x,y) :
    return x+y
a = reduce(add,[1,3,5,7,9])
print('reduce:',a)
# 当然，求和运算可以直接用sum()函数来计算。

#  但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：

from functools import reduce
def fn (x,y):
    return x * 10 + y
a = reduce(fn,[1,3,5,7,9])
print(a)

# 这个例子本身没有多大的用处，如果考虑到字符串str也是一个序列，对上面的例子杀价修改
# 在配合map()，我们就剋写出把str转换为int的函数了。

from functools import reduce
def fn (x,y):
    return x * 10 + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

a = reduce(fn, map(char2num, '1378'))
print(a)

# 整理成一个str2int的函数就是：

from functools import reduce
def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num,s))

a = str2int('123')
print(a)
print(type(a))