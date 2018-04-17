#x平方的函数

def power(x):
    return x * x

print(power(3))
print(power(15))

#《位置参数》
#函数的2次方还好算，那如果函数的3次方、6次方.....的话怎么办，我们不可能无限多个函数，
#那么这个时候就需要在函数的参数上做文章了，比如power(x,n),也就是x的n次方

def power(x,n = 2): # 设置n的默认参数为2
    s = 1
    while n > 0 :
        n = n -1
        s = s * x
    return s

print(power(3,2))
print(power(3,4))

# 《默认参数》
#新的代码power(x,n)没有问题，但是旧的代码调用失败了，原因是我们增加了一个参数，
#导致旧的代码因为缺少一个参数而无法执行，而且错误原因也很明确：
# TypeError: pow expected at least 2 arguments, got 1
# 那么这个时候默认参数就登场了，由于我们经常计算x的2次方，完全可以把第二个参数n的值设置为2
# 这样当我们调用power(5)的时候就相当于调用power(5,2)
print(power(5))
print(power(5,2))

def enroll (name,age):
    print('name:',name)
    print('gender:',age)
#在调用上面函数的时候只需要传入一个姓名和性别即可。
print(enroll('harry','6'))
# 如果继续传入年龄、城市信息呢，由于输入的东西太多会使得程序调用的复杂度大大增加，
# 而如果大多数人的年龄与城市都是6岁和上海的情况时，我们可以把年龄和城市设置为默认参数。

def enroll (name,gender,age=6,city='shanghai') :
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

#这样大多数学生在注册的时候都不需要输入年龄、城市等信息了，只有与默认信息不符的人才有必要输入，如：
print(enroll('linda','M',8,'beijing'))

# 坑
def add_end(L = []):
    L.append('END')
    return L
#正常调用时好像没有错误，依次输出1,2,3,END
print(add_end([1,2,3]))
#使用默认参数调用时也没有错误
print('默认参数调用：',add_end())
#但是，再次调用默认参数时貌似就不对了,连续输出了两次 ['END', 'END']
print('再次默认参数调用：',add_end())
'''
原因解释如下：
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，
它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，
不再是函数定义时的[]了。
所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
'''
#要修正以上的例子，我们可以使用none这个不变对象来实现

def add_end (L = None):
    if L is None:
        L = []
    L.append('END')
    return L

# 现在，无论调用多少次都不会出现错误了。

#print('第1次调用默认参数：', add_end())
#print('第2次调用默认参数：', add_end())
#print('第3次调用默认参数：', add_end())


#《可变参数》

#在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的
# 参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

#以数学题为例子，给定一组数字a，b，c……，请计算a方 + b方 + c方 + ……。
def calc (numbers):
    sum1 = 0
    for n in numbers:
        sum1 = sum1 + n * n
    return sum1
# 在调用的时候不能输入calc(3),而是要给出一个list或是tuple，如：
print(calc([1,2,3]))
# 如果利用可变参数，调用函数的方式可以简化成这样：
#   print(calc(1,2,3))
#   print(calc(1,2,3,4,5,6,7,8))
# 所以，我们把函数的参数变为可变参数
def calc (*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print('配置可变参数后：',calc(1,2,3,4,5))
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，
# 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：

#如果已经有了一个list或tuple了，怎么办？
nums = [1,2,3]
print('已有了一个list的情况：',calc(nums[0],nums[1],nums[2]))

#《关键字参数》
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时会自动组装成一个tuple。
# 而关键字参数允许你传入0个或任意个包含参数名的参数，这些关键字参数在函数内部自动组建成一个
# dict。
def person (name,age,**kw) :
    print('name:',name,'age:',age,'other:',kw)
#函数person除了必选的name和age外，还接受关键字参数kw。
# 在调用函数时可以只传入必选参数。
print(person('harry',20))
#也可以传入任意个数个关键参数
print(person('bob',32,city='shanghai'))
print(person('linda',23,job='engineer',gender='女'))
# 关键字参数的作用：它可以扩展函数的功能，比如在person函数里面我们能保证收到name和age参数，
# 但是如果调用者愿意提供更多的参数我们也能收到。试想一个注册页面，用户在输入了必填项姓名和年龄外，
# 其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
# 和可变参数类似，也可以先组建一个dict，然后把该dict转换为关键字参数然后穿进去。

extra = {'city':'shanghai','job':'enginner'}
print(person('daniel',24,city=extra['city'],job=extra['job']))

#当然，上面的这个复杂的写法可以简化成:
print(person('jack',24,**extra))
# **extra 就是把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict
# 而这个dict只是extra的一份拷贝，对kw的改动不会影响到函数外的extra()函数。

# 《命名关键字参数》
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数，至于具体传递了哪些参数就需要
# 函数内容通过kw来查看，还是以person()函数为例，我们希望检查是否传入来city和job参数：

def person (name,age,**kw):
    if 'city' in kw:
        # 存在city参数
        pass
    if 'job'  in kw:
        # 存在job参数
        pass
    print('name',name,'age',age,'other',kw)
# 但是调用者仍可以传入不受限制的关键字参数
print(person('jack',24,city='shanghai',addr='jiading',zipcode=123456))
# 如果要限制关键字参数的名字，可以用命名关键字参数，例如，只接受city和job作为关键字参数，定义方式如下所示：
def person (name,age,*,city,job):
    print(name,age,city,job)
# 和关键字参数不同，命名关键字参数需要一个特殊的分隔符号*，*后面的参数名被视为命名关键字参数。调用方式如下所示：
print(person('harry',23,city='shanghai',job='enigneer'))


#《参数组合》
