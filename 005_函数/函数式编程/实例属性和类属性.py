 # 由于python是动态语言，根据类创建的实例可以任意绑定属性。
 # 给实例绑定属性的方法是通过实例变量，或者通过self变量。

class Student(object):

    name = 'Student'

    def __init__(self,name):
        self.name = name

s = Student('Bob')
s.score = 90
# 但是，如果Student类本身需要绑定一个属性呢，可以直接在class中定义属性，
# 这种属性是类属性，归Student类所有：

class Student(object):

    name = 'Student'

# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。


class Student(object):
     name = 'Student'

s = Student() # 创建实例s
print('实例的name属性',s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性。

print('类的name属性：',Student.name) # 打印类的name属性

s.name = 'Michael' # 给实例绑定name属性
print(s.name)
print(Student.name)
del s.name
print(s.name)

