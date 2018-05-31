class ParentClass1:
    pass

class ParentClass2:
    pass

class Subclass1(ParentClass1):
    pass

class Subclass2(ParentClass1,ParentClass2):
    pass

# 查看继承
print(Subclass1.__bases__)  # 查看继承的所有类
#=> (<class '__main__.ParentClass1'>,)

print(Subclass2.__bases__)
#=> (<class '__main__.ParentClass1'>, <class '__main__.ParentClass2'>)

