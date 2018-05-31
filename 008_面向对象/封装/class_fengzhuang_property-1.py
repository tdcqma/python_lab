class People:

    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,val):
        if type(val) is not str:
            raise TypeError('名字必须为字符串')
        self.__name = val

    @name.deleter
    def name(self):
        # del self.__name
        print('禁止删除！')

p  = People('egon')
print(p.name)