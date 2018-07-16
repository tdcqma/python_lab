


# class People(object):
#     county='china'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def eat(self):
#         print('%s is eating' %self.name)
#
#     def __call__(self, *args, **kwargs):
#         print('===>',self)
#         print(args)
#         print(kwargs)
#
# obj=People('egon',18)
#
# obj(1,2,3,x=1,y=2) #触发类People中的__call__，即调用对象就是在触发对象所在类的中的__call__
# #即对象之所以可以调用，一定是对象的类中定义了一个__call__



class Mymeta(type):
    def __call__(self, *args, **kwargs): #self=<class '__main__.People'>
        # print('=====>',self)
        # print('=====>',args)
        # print('=====>',kwargs)

        #1、先造一个People类的空对象obj
        obj=self.__new__(self)
        # print(obj.__dict__)
        #2、调用People类中__init__函数，完成初始化空对象obj的操作

        # print(self.__dict__)
        self.__init__(obj,*args,**kwargs)

        # print(obj.__dict__)

        # dic={}
        # for k,v in obj.__dict__.items():
        #     dic['_%s__%s' %(self.__name__,k)]=v
        #
        # # print(dic)
        # obj.__dict__=dic

        obj.__dict__={'_%s__%s' %(self.__name__,k):v for k,v in obj.__dict__.items()}
        #3、返回对象obj
        return obj

class People(object,metaclass=Mymeta):
    county='china'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def eat(self):
        print('%s is eating' %self.name)


p1=People('egon',18,'male') # 调用对象People，一定是对象People的类Mymeta中有一个__call__

# print(p1)
print(p1.__dict__)
# print(People.__dict__)


