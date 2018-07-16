__author__ = 'tdcqma'

# [方法一]：指名道姓，即父类名.父类方法()
"""
class Vehicle:
    country = 'China'

    def __init__(self,name,speed,load,power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print('开动了...')

class Subway(Vehicle):
    def __init__(self,name,speed,load,power,line):
        Vehicle.__init__(self,name,speed,load,power)
        self.line = line

    def run(self):
        print('地铁%s号线欢迎您。' % self.line)

line13 = Subway('中国地铁','180km/h','100人/节','电',13)
line13.run()
"""

# [方法二] 使用super()来调用
class Vehicle:
    country = 'China'

    def __init__(self,name,speed,load,power):

        # super(Subway,self)相当于实例本身
        # 在python3中super()等同于super(Subway,self)

        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print('run...')


class Subway(Vehicle):
    def __init__(self,name,speed,load,power,line):
        super().__init__(name,speed,load,power)
        self.line = line

    def run(self):
        print('地铁%s号线欢迎您' % self.line)
        super(Subway,self).run()

line13 = Subway('中国地铁','180km/h','1人/每节','电',13)
line13.run()