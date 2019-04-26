# python内置了很多有用的函数，我们只需要记住函数名和需要的参数既可以调用函数，
# 函数的帮助文档可以在python的官网查看https://docs.python.org/3/library/index_bak2.html
# 也可以使用help()来查看，如：
help(abs)
print(abs(-2))

#当传入函数中的参数数量个数不一致的时候，python会报错。TypeError: abs() takes exactly one argument (2 given)
#print(abs(1,2))

#如果传输的参数个数是对的，但是传输的数据类型不对那么也会包typeerror错误
# TypeError: bad operand type for abs(): 'str' 如：
#print(abs('a'))

#而max()函数可以接受任意多个参数并且返回最大的那个参数

print('最大值：',max(1,2,3,4,5))

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋值给一个变量，相当于给这个函数起来一个别名
a=abs
print(a(-1))