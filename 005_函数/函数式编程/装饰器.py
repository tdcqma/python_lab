# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也可以调用函数。

def now():
    print('2017-4-11')
f = now
print(f())

#函数对象有一个__name__属性，可以拿到函数的名字
a = now.__name__
print('函数的名字：',a)

#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望
#now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为"装饰器(Decorator)"

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们定义个能打印日志的的decorator

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper

# 观察上面的log，因为他是一个decorator，所以接收一个函数作为参数，并返回一个函数。
# 我们要借助python的@语法，把decorator置于函数的定义处：

@log
def now():
    print('2015-3-25')

# 调用now()函数，不仅会运行now()函数本身，还会运行now()函数前打印一行日志：
print(now())

# 把@log放在now()函数的定义处，相当于执行了语句
# now = log(now)

