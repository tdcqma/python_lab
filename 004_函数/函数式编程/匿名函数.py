# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
# 在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，
# 除了定义一个f(x)的函数外，还可以直接传入匿名函数：

a = list(map(lambda x : x * x,[1,2,3,4,5,6,7,8]))
print(a)

# lambda 其实等价于函数：

def f (x):
    return x * x
# 关键字lambda表示匿名函数，冒号前边的x表示函数的参数
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

# 可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

f = lambda x: x*x
print(f)
print(f(3))

# 同样，也可以把匿名函数作为返回值返回
def build (x,y):
    return lambda : x*x + y*y

a = build(2,4)
print(a())
