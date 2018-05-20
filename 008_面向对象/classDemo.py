'''
类：如果说对象是特征与技能的结合体，那么类就是一系列对象相似的特征与技能的结合体
ps：站在不同的角度总结出的类是截然不同的

在现实世界中：一定是先有对象，再有分类的概念

在程序中，务必记住：一定要先定义类，后调用类来产生对象


在现实世界中（站在老男孩选课系统角度）
对象1：
    特征
        school='Oldboy'
        name='李泰迪'
        sex='male'
        age=18
    技能
        选课

对象2：
    特征
        school='Oldboy'
        name='牛榴弹'
        sex='female'
        age=38
    技能
        选课

对象3：
    特征
        school='Oldboy'
        name='张随便'
        sex='male'
        age=38
    技能
        选课

对象4：
    特征
        name='Egon'
        sex='male'
        age=18
        level=10
    技能
        打分
        点名

现实世界中老男孩学生类
    相似的特征
        school='Oldboy'
    相似的技能
        选课

'''
#在程序中
#先定义类
class OldboyStudent:
    school = 'Oldboy'

    def choose_course(self):
        print('is choosing course')


# 后调用类来产生对象，调用类的过程又称之为实例化
stu1=OldboyStudent()  # stu1可称为一个对象，也可以称为一个实例