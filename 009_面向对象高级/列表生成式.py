# 列表生成式，即list Comprehensions，是python内置的非常简单却十分强大的可以用来创建list的生成式
# 举个例子，要生存[1,2,3,4,5,6,7,8,9,10],可以用list(range(1,11))

a = list(range(1,11))
print(a)

# 但是要生成1*1,2*2,3*3...10*10的话怎么办，还可以用循环。
L = []
for i in range(1,11):
    L.append(i*i)
print(L)

#但是以上的循环太繁琐，使用列表生成式的话一行语句就可以替代上面的for循环语句。

a = [x * x for x in range(1,11)]
print('列表生成式 a:',a)

# 写列表生成式的时候需要把x * x 放到for的前边，就可以把list创建出来，
# for循环后面还可以跟上if判断
# 如：进筛选偶数的平方

a = [x * x for x in range(1,11) if x % 2 ==0]
print('列表式生成1-10，筛选其中偶数的平方：',a)

# 还可以使用两层循环
a = [m + n for m in ['a','b','c'] for n in ['1','2','3']]
print(a)

# 使用列表生成式还可以写出非常简介的代码，例如列出当前目录的所有文件和目录名

import os # 导入os模块，
d = [d for d in os.listdir('/')] # os.listdir可以列出目录名和文件名
print(d)

# for循环其实可以同时使用两个甚至更多的变量，比如dict的items()可以同时迭代key和walue：
d = {'x':'a','y':'b','z':'c'}
for k,v in d.items():
    print(k,'=',v)
# 因此列表生成式也可以使用两个变量生成list
d1 = [k + ':' + v for k,v in d.items()]
print('d1:',d1)

# 把一个list中的所有字符串都变成小写
L = ['Hello','World','IBM','Apple']
a = [s.lower() for s in L]
print(a)

