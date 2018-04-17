# 函数作为返回值

# 高阶函数除了可以接收函数作为参数外，还可以把函数作为结果值返回。
# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：

def calc_sum (*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和的结果，而是返回求和的函数：

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 当我们调用lazy_sum()时，返回的并不是求和的结果，而是求和的函数：
f = lazy_sum(1,2,3,4,5,)
print('调用函数lazy_sum:',f)
# 调用函数f时，才能计算真正的求和的结果
print('调用函数f：',f())

# 在这个例子中，我们在函数lazy_sum中定义来函数sum，并且，内部函数，内部函数sum
# 可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时
# 相关参数和变量都保存在返回的函数中，这种称为"闭包(closure)"的程序结构拥有极大的威力。

# 请注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print(f1 == f2)

# 《闭包》
#  返回的函数并没有立刻执行，而是直到调用了f()函数后才执行。来看一个例子

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1,f2,f3 = count()
# 在上面的例子中，每次循环，都创建了一个新的函数，然后把创建的3个函数都返回了。
print('f1() =>',f1(),'f2() =>',f2(),'f3() =>',f3())
# 在上面的点用结果看，返回值全部都是9，奇怪了，不是应该是1，4，9的吗
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def count():
    def f(j):
        def g ():
            return j * j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3= count()
print(f1())
print(f2())
print(f3())

# 缺点是代码较长，可利用lambda函数缩短代码。
