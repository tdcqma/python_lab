# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)

# L 和g的区别仅在与[]与（），L 就是一个list而g是一个generator，
# 如何打印generator呢，可以使用next()函数获取g的下一个返回值
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# generator保存的是算法，即每次调用next(g)都会计算出g的下一个元素值，直到计算出最后一个值。
# 没有更多的元素时就会抛出StopIteration的错误。
# 通过next（）函数一个一个的调用是在是太麻烦了，正确的方法是使用for循环，因为generator也是可迭代对象：

g = (x * x for x in range(10))
for n in g:
    print('generator:',n)

# 所以，我们创建了一个generator后基本上永远不会调用next()，而是通过for循环来迭代它。
# 并且不需要关心stopiteration错误。

# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

def fib (max) :
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1
    return 'done'
print(fib(11))

# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，
# 推算出后续任意的元素，这种逻辑其实非常类似generator。
# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：

def fib (max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b , a+b
        n = n+1
    return 'done'

#这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# 举个简单的例子，定义一个generator，依次返回数字1，3，5：
'''
def odd ():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
'''
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)

o = odd()
print(next(o))
print(next(o))
print(next(o))

# 可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。
# 执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。

# 回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
# 同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代：
for n in fib(6):
    print(n)
