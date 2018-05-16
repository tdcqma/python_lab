# 面向对象最重要的概念就是类（class）和实例（instance），必须牢记类时抽象的
# 模版，比如Student类，而实例时根据类创建出来的一个个具体的"对象"，每个对象都拥有
# 相同的方法，但各自的数据可能不同。

# 仍以student类为例，在python中，定义类时通过class关键字：

class Student(object):
    pass

# class后面紧跟着的时雷鸣，即Student,类名通常是大写开头的单词，紧接着是（object）
# 表示该类是从那个类继承下来的，通常，如果没有合适的继承类，就使用object类，这是所有类
# 最终都会继承的类。

# 定义好类Student类，就可以根据Student类创建Student的实例，创建实例通过
# 类名+（）实现的。

bart = Student()
print(bart)

print(Student)

# 可以看到，变量bart指向的是一个Student的实例，后面的0x102260400是内存地址，每个
# object的地址都不一样，而Student本身则是一个类。
# 可以自由的给一个实例绑定属性，比如，给实例bart绑定一个name属性。

bart.name = 'Bart Simpson'
print(bart.name)

# 由于类可以起到模板的作用，因策，可以在创建实例的时候，把一些我们认为必须绑定的
# 属性强制绑定进去，通过定义一个特殊的__init__方法，在创建实例的时候，就把
# name，score等属性绑定上去：

class Student (object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

# 注意：特殊方法init前后有两个下划线！！！

# 注意到 __init__方法的第一个参数永远是self，表示创建的实例本身，因此在__init__方法
# 内部，就可以把各种属性绑定到self，因为self就是指向类创建的实例本身。

# 有了__init__方法，在创建实例的时候，就不能传入空的参数类，必须传入与
# __init__方法匹配的参数，但self不需要传，python解释器会自己把实例变量传进去。

bart = Student('Bart Simpson',59)
print(bart.name)
print(bart.score)

# 《数据封装》
# 面向对象编程的一个重要特点就是数据封装。在上面的student类中，每个实例就拥有
# 各自的name和score这些数据。我们可以通过函数来访问这些数据，比如打印一个学生的
# 成绩：

def print_score(std):
    print('%s : %s' % (std.name,std.score))

print(print_score(bart))

# 但你，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的
# 函数去访问，可以直接在Student类的内部定义访问数据的函数，这样就可以把"数据"给封装起来。
# 这些封装数据的函数是和Student类本身关联起来的，我们称之为类的方法：

class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s' % (self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        if self.score >= 60:
            return 'B'
        else:
            return 'C'

# 要定义一个方法，除了第一个参数是self外，其他和普通的函数一样。要调用一个方法，只需要
# 在实例变量上直接调用，除了self不用传递，其他参数正常传入：

bart = Student('harry',123)
bart.print_score()
a = bart.get_grade()
print(a)
# 这样以来，我们从外部看student类，就只需要知道，创建实例需要给出name和score，
# 而如何打印，都在student类的内部定义的，这些数据和逻辑被"封装"起来了，调用很容易，
# 但却不知道内部实现的细节。

# 封装的另一个好处是可以给student类增加新的方法，比如get_grade:
