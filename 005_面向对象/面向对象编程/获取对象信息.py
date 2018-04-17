# 获取对象信息

# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型，有哪些方法呢。
# 使用 type()判断：

s1 = type(123)
print(s1)

s2 = type('str')
print(s2)

s3 = type(None)
print(s3)

# 如果一个变量指向函数或者类，也可以使用type判断：
s4 = type(abs)
print(s4)

# 但是type()函数返回的是什么类型呢？它返回对应的class类型。如果我们要在if语句中判断，
# 就需要比较两个变量的type类型是否相同：

s5 = type(123) == type(456)
print(s5)

print(type(123) == int)
print(type('abc') == str)
print(type('abc') == type(123))

print('------')
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办，
# 可以使用type模块定义的常量：

import types

def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
#print(types(x for x in range(10)) == types.GeneratorType)

# 使用isinstance()

# 对于class的继承关系来说，使用type就很不方便。我们要判断class的类型，可以使用
# isinstance()函数。
# 同时能用type()判断的基本类型也可以用isinstance()判断：
print('-------')
print(isinstance('a',str))
print(isinstance(123,int))
print(isinstance(b'a',bytes))

# 判断变量是某些类型中的一种，例如下面的代码可以判断是否是list或者是tuple
print('-------')
print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))

# 《使用dir()》

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list。
# 比如，获得一个str对象的所有属性和方法：

print(dir('ABC'))

# 类似__xxx__的属性和方法在python中都是有特殊用途的，比如__len__方法返回长度。在
# python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动会
# 去调用该对象的__len()__方法，下面的代码是等价的：


a1 = len('ABC')
a2 = 'ABC'.__len__()
print(a1)
print(a2)

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

# 仅仅把属性和方法列出来是不够的，配合getattr(),setattr()以及hasattr(),我们可以
# 直接操作一个对象的状态：

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
# 紧接着，可以测试该对象的属性：

print('判断对象obj里是否有属性x：',hasattr(obj,'x'))
print('判断对象obj里是否有属性y：',hasattr(obj,'y'))
setattr(obj,'y',19)
a = hasattr(obj,'y')
print(a)
a  = getattr(obj,'y')
print(a)
a = obj.y
print(a)