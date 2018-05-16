# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例
# 绑定任何属性和方法，这就是动态语言的灵活性。先定义class：

class Student(object):
    pass

def set_score(self,score):
    self.score = score

#Student.set_score = set_score()

# 然后，尝试给实例绑定一个属性：

s = Student()
s.name = 'Michael'
print(s.name)

s.set_score()


# 还可以尝试给实例绑定一个方法：

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

# 但是,给一个实例绑定的方法，对另一个实例是不起作用的

# s2 = Student() # 创建新的实例
# s2.setage(25)
# print(s2)
# 报错信息：AttributeError: 'Student' object has no attribute 'setage'

# 为了给所有的实例都绑定方法，可以给class绑定方法：





# 给class绑定方法后，所有实例均可以调用：

# 使用__slots__

#如果想限制实例的属性怎么办，比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，python允许在定义class的时候，定义一个特殊的__slots__变量。

class Student(object):
    __slots__ = ('name','age')

# 然后我们试试：

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性name
s.age = 25 # 绑定属性age

#s.score = 99
# 绑定属性s.score=99的时候报错：AttributeError: 'Student' object has no attribute 'set_score'
# 因为__slots__里没有score属性，所以外部不能创建。