# 面向过程的例子
# 假设我们要处理学生的成绩，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示

std1 = {'name':'Michael','score':93}
std2 = {'name':'Bob','score':81}

# 在处理学生成绩时可以通过函数实现，比如打印学生的成绩：
def print_score(std):
    print('%s:%s' % (std['name'],std['score']))

print(print_score(std1))
print(print_score(std2))


# 面向对象的例子：
print('--------------')

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s' % (self.name,self.score))

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',88)

bart.print_score()
lisa.print_score()