# 在python中定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号：
# 然后在缩紧块中写函数体，函数的返回值用return语句来返回。

# 自定义一个求绝对值的my_abs函数

def my_abs (x) :
    if not isinstance(x,(int,float)) :
        raise TypeError('bad operand tye')
    if x >= 0 :
        return x
    else:
        return -x

# 《空函数》
# 如果定义一个什么事都不做的函数用pass,pass语句的作用实际上就是占位符，
# 比如现在还没想好写什么代码，但是又想让程序能正常跑通，就先用pass来暂时替代。
def nop():
    pass

age = 3
if age >= 18 :
    pass

# 《参数检查》
# 调用函数时如果参数个数不对，python解释器会自动检查出来，并抛出typeerror错误。
#print(my_abs(1,2))
# TypeError: my_abs() takes 1 positional argument but 2 were given

# 如果参数类型错误的时候，我们自定义的my_abs()函数不会返回详细的报错信息，
# 而python内置的abs()函数会给出详细的报错信息，说明my_abs函数不够完善。
#print( abs('a'))    # TypeError: bad operand type for abs(): 'str'
#print( my_abs('a')) # TypeError: '>=' not supported between instances of 'str' and 'int'

# 进一步完善my_abs()函数，这里我们把函数重命名为my_abs_yh()函数

def my_abs_yh(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0 :
        return x
    else:
        return -x

print('my_abs优化函数：',my_abs_yh(-2))
print(my_abs_yh('a')) # 报错信息已变为：TypeError: bad operand type

# 《返回多个值》

