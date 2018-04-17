# python的functools模块提供了很多有用的功能，其中一个就是偏函数（partialfunction）
# 函数参数可以通过设定默认的默认值来降低函数调用的难度。而偏函数也可以做到这一点。

#int()函数可以把字符串转换为整数，当仅转入字符串时，int（）函数默认按十进制转换：

a = int('12345')
print(a)
print(type(a))

# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以作N进制转换：

a = int ('12345',base=8)
print(a)
print(type(a))

# 假设要转换大量的二进制字符串，每次都传入int(x,base=2)非常麻烦，于是，我们想到可以
# 定义一个int2()的函数，默认把base=2传进去：

def int2 (x,base=2):
    return int(x,base=2)

# 这样我们转换2进制就非常方便了：

a = int2('1000000')
print(a)
a = int2('1010101')
print(a)

# functools.partial 就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
# 可以直接使用下面的代码创建一个新的函数int2:

import functools
int2 = functools.partial(int,base=2)
a = int2('1000000')
print(a)
a = int2('1010101')
print(a)

# 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设定默认值）
# 返回一个新的函数，调用这个函数会更简单。

# 注意到上面的新的int2()函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值

a = int2('1000000',base=2)
print(a)

# 最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：

int2 = functools.partial(int,base=2)
#实际上固定了int（）函数的关键字参数base，也就是
# int2('10010') 相当于 kw = { 'base' :2 }
# int('10010',**kw)

# 当传入以下参数，实际上会把10作为*args的一部分自动加到左边，也就是：
max2 = functools.partial(max,10)
a = max2(5,6,7)
print(a)

# 相当于 args = (10,5,6,7)
#max(*args)
