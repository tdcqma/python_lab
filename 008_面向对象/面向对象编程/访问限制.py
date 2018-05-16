# 在class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来
# 操作数据，这样就隐藏了内部的复杂逻辑。

# 但是从前面student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性


class Student (object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s : %s' % (self.name,self.score))


bart = Student('Bart Simpson',98)
print(bart.score)

bart.score = 59
print(bart.score)

# 如果要让内部属性不被外部访问，可以把属性名称前加上两个下划线__，在python 中，
# 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问
# 外部不能反问，所以，把Student类改一改

class Student (object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s : %s' % (self.__name,self.__score))

# 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和
# 实例变量.score了。

bart = Student('Bart Simpson',982)
# print(bart.__name) 报错：AttributeError: 'Student' object has no attribute '__name'

# 这样就确保了外部代码不能随意修改内部的状态，通过访问限制的保护，代码更加健壮了。
# 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score方法呀。
# 同样，如果又要允许外部代码修改score怎么办，可以再给Student类增加set_score方法：

class Student (object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s : %s' % (self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        self.__score = score

# 你也许会问，原先那种通过bart.score = 59 也可以修改啊，为什么要定义一个方法大费周折呢，
# 这是因为在方法中，可以对参数作检查，避免传入无效的参数：

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

# 需要注意的是，在python 中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
# 是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、
# __score__这样的变量名。

# 有时候，一个下划线开头的实例变量名，比如_name，这样的实例比阿亮外部是可以访问的，
# 但是按照约定俗成的规定，当你看到这样的变量时，意思就是"虽然我可以被访问，但是
# 请把我视为私有变量，不要随意访问"

# 双下划线开头的实例变量是不是一定不能从外部访问呢，其实也不是。不能直接访问
# __name是因为python解释器对外把__name变量改成类_Student__name,所以，仍然可以通过
# _Student__name来访问变量：

#a = bart._Student__name
#print(a)

bart = Student('Bart Simpson',982) # 创建实例对象

bart.set_score(88)  # 通过set_score()方法赋值给score
print(bart.get_score()) # 通过get_score()方法获得score值






