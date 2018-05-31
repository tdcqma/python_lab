# 创建类
class OldboyStudent:
    school = 'Oldboy'

    def choose_course(self):
        print('%s is choosing course' % self)

# 类有两种用途
# 【1】用途一：类本身就是一个容器（名称空间），所以可以增删改查类的属性
# print(OldboyStudent.__dict__)   # 打印类所有的属性（数据与函数）
# print(OldboyStudent.__dict__['school']) # Oldboy
# print(OldboyStudent.__dict__['choose_course'])
# OldboyStudent.__dict__['choose_course'](123)

# print(OldboyStudent.school)
# print(OldboyStudent.xxx)
# print(OldboyStudent.choose_course)
# OldboyStudent.choose_course(123)

# 类的属性可以进行增删查改操作
# 增
# OldboyStudent.country="China"
# print(OldboyStudent.__dict__)

# 改
# OldboyStudent.school = "Oldgirl"
# print(OldboyStudent.__dict__)

# 删
# del OldboyStudent.school
# print(OldboyStudent.__dict__)

# 【2】用途二：调用类来产生对象，调用类的过程又称为实例化

class OldboyStudent:
    school = "Oldboy"

    def choose_course(self):
        print('is choosing course')

stu1 = OldboyStudent()
stu2 = OldboyStudent()
stu3 = OldboyStudent()

def init(obj,x,y,z):
    obj.name = x
    obj.sex = y
    obj.age = z

init(stu1,'李泰迪','male',18)
init(stu2,'牛柳蛋','female',38)
init(stu3,'张随便','female',48)


# !!! 注意 !!!
# 对象的属性查找是先从对象自己的名称空间里找，找不到则在类中查找,如果类中存放的
# 数据是所有对象共有的，内存地址都一样。如以下示例：
# print(stu1.x)
# print(stu1.school,id(stu1.school))
# print(stu2.school,id(stu2.school))
# print(stu3.school,id(stu3.school))

print(stu1.choose_course,id(stu1.choose_course))
print(stu2.choose_course,id(stu2.choose_course))
print(stu3.choose_course,id(stu3.choose_course))