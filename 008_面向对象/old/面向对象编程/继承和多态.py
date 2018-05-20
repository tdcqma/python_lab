# 在OOP（面向对象）程序设计中，当我们定义一个class的时候，可以从某个现有的
# class继承，新的class成为子类（Subclass），而被继承的class成为基类、父类或
# 超类（base class、Super class）

# 比如，我们已经编写类一个名为Animal的Class，有一个run()方法可以直接打印：

class Animail(object):
    def run(self):
        print('Animal is running...')

# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：

class Dog(Animail):
    pass

class Cat(Animail):
    pass

# 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。

# 那么，继承有什么好处？最大的好处就是子类获得了父类的的全部功能。由于Animail实现了
# run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run方法。

dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 当然，也可以对子类增加一些新的方法，比如Dog类：

class Dog(Animail):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat ...')

dog = Dog()
dog.run()

print('----')
# 继承的第二个好处需要我们对代码做一点改进，你看到了，无论是Dog还是Cat，他们
# run()的时候，现实的都是Animal is running... ,符合逻辑的做法是分别判断显示
# Dog is running... 和 Cat is running... ,因此，对Dog和Cat类改进如下：

class Dog(Animail):

    def run(self):
        print('Dog is running...')

class Cat(Animail):

    def run(self):
        print('Cat is running...')

# 再次运行，结果如下：

dog = Dog()
dog.run()
cat = Cat()
cat.run()

# 当子类和父类都存在相同的run（）方法时，我们说，子类的run（）方法覆盖了父类的run（）方法，
# 在代码运行的时候，总会调用子类的run（），这样我们就获得了继承的另一个好处：多态。

# 要理解什么是多态，我们首先要对数据类型再做一点说明。当我们定义一个class的时候，我们实际上
# 就定义了一种数据类型。我们定义的数据类型和python自带的数据类型。比如：str，list，dict没什么两样。

a = list() # a是list列表烈性
b = Animail() # b是Animal类型
c = Dog() # c是Dog类型

# 判断一个变量是否是某个类型可以用isinstance()判断：
print(isinstance(a,list))
print(isinstance(b,Animail))
print(isinstance(c,Dog))

# 看来a、b、c确实对应着list、Animal、Dog这3种类型
# 但是等等，试试：

print(isinstance(c,Animail))

# 看来c不仅仅是Dog,c还是Animal ！
# 不过仔细 想想也有道理，因为Dog是从animal继承下来的，当我们创建了一个dog的实例c时，
# 我们认为c的数据类型是dog没错，但c同时也是animal也没错，dog本来就是animal的一种。

# 所以在这种继承关系中，如果一个实例的数据类型是某个子类，那么它的数据类型也可以被看作
# 是他的父类。但是反过来就不行：

b = Animail()
print(isinstance(b,Dog))

# dog可以看成animal，但是animal不可以看成dog
# 要理解多态的好处，我们还需要编写一个函数，这个函数接收一个animal类型的变量：


def run_twice(animal):
    animal.run()
    animal.run()

# 当我们传入Dog的实例时，run_twice()就打印出：

run_twice(Animail())
run_twice(Dog())
run_twice(Cat())

# 看上去没什么意思，但是仔细想想，现在，如果我们再定义一个Tortoise类型，也从
# Animail派生：

class Tortoise(Animail):
    def run(self):
        print('Tortoise is running slowly...')

# 当我们调用run_twice()时，传入Tortoise的实例：

run_twice(Tortoise())

# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是
# 则传入的对象必须是Animal类型活着他的子类