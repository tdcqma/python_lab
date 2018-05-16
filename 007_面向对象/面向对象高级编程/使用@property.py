# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是没办法检查参数，
# 导致可以把成绩随便改

class Student(object):
    pass

a = Student()
a.score = 9999
print(a.score)

# 这个显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩
# 再通过一个get_score()来获取成绩，这样，在set_score()方法里，可以检测参数：

class Student(object):

    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value> 100:
            raise ValueError('score must between 0 - 100!')
        self._score = value

# 现在，对任意的Student实例进行操作，就不能随心所欲地设置score了

s = Student()
s.score = 60
#print(s)

s.set_score(60)
print(s.get_score())

#s.set_score(9999)
#print(s.get_score())



# 上面的调用方法又略显复杂，没有直接用属性这么直接简单。
# 装饰器（decorator）可以给函数动态加上功能，对于类的方法，装饰漆一样起作用。
# 在python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an interger@')
        if value < 0 or value >100:
            raise ValueError('score must between 0 - 100!')

        self._score = value
# @property 的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上
# @property 就可以类，此时，@property本身又创建类另一个装饰器@score.setter,
# 负责把一个setter方法变成属性赋值，于是，我们就拥有了一个可控的属性操作：

s = Student()
s.score = 60
print(s.score)

#s.score = 9999
#print(s)

# 注意到这个神奇的@property，我们对实例属性操作的时候，就知道该属性很可能不是直接暴露的
# 而是通过getter和setter方法来实现的。

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

s1 = Student()
s1.birth = 20
print(s1.birth)

print(s1.age)
