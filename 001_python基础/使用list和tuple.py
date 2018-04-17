# python内置的一种数据类型是列表：list，
#list 是一种有序的集合，可以随时添加或删除其中的元素

classmates = ['natasha','harry','sarah']
print(classmates)

#以上的变量classmates就是一个list，用len()函数就可以查看该list的元素个数

print('classmates列表元素个数为：',len(classmates))

# 用索引来调出列表中每一个位置的元素，索引从0开始
print('第一个元素是：',classmates[0])
print('第二个元素是：',classmates[1])
print('第三个元素是: ',classmates[2])

#当索引超出来范围就会报'Indexerror'错误，随后一个索引的位置总是len(classmates)-1个。
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：

print('最后一个元素：',classmates[-1])
print('倒数第二个元素：',classmates[-2])

#list是一个有序表，添加新元素的时候使用append()方法自动添加到列表末尾，如：
classmates.append('jack')
print('append()方法插入到列表末尾：',classmates)

#也可以把元素插入到指定的索引位置，使用方法insert()方法，比如插入到索引是1的位置

classmates.insert(1,'daniel')
print('insert（）方法插入指定位置：',classmates)

#删除指定索引位置的元素用pop(i)方法，i是索引的位置如
classmates.pop(-1)
print('删除倒数第一个元素：',classmates)
classmates.pop(1)
print('删除第2个元素：',classmates)

#把某个元素替换成别的值，可以直接赋值给对应索引位置的元素，如
print('赋值前：',classmates)
classmates[1] = 'daniel'
print('赋值后：',classmates)

#list里面的数据类型也可以不同，下面的例子里有字符串、整数、浮点、布尔、列表，
employee_infomation = ['harry',21,178.2,True,classmates]
print('employee_infomation的列表打印：',employee_infomation)
#其中employee_information因嵌套这classmates列表，所以employee_infomation可以看作是一个
#二维数组，类似的还有三维数组、四维数组，不过都很少会用到。
#如果想要取出classmates的第2个元素可以通过一下方式拿出来
print('打印classmates：',classmates)
print('打印employee_information:',employee_infomation)
print('取出employees_information列表里的classmates列表的第二个元素：',employee_infomation[4][1])

print('\n----------------------华丽丽的分割线----------------------\n')

#除了列表外，还有一个叫作tuple（元组）的序列，tuple与list非常的像，不同的是tuple一旦初始化后
#就不能被改变了，比如同样是classmates，用元组tuple表示需要使用小括号表示：

classmates = ('张三','李四','王五')
print('tuple元组classmates的打印：',classmates)
#现在classmates这个元组已经创建了，已经不能被改变了。
# 它没有append()、insert()这样的方法。
#但是获取元素的方法和list是一样的，仍然可以使用classmatest[1]这样的方式来获取
print('数组classmates的第2个元素是：',classmates[1])

#如果要定义一个空的tuple的话:
t = ()
print('打印空的元组t = ',t)

#但是如果要定义只有一个元素的tuple的话
t = (1)
print('打印t = (1)：',t)
#因为数组中只包含一个元素的时候，小括号与数学运算中的小括号会产生奇异，为了避免这种现象发生
#在使用tuple打印一个元素的时候一定要在末尾加上一个逗号，比如
t = (1,)
print('打印 t = (1,) :',t)

#tuple元组虽然是不可以改变的，但是当tuple里面包含了一个list的时候，是可以更改list内部的元素内容的，如：
classmates_A = ['小红','小强','小明'] # 定义一个列表list
classmates_B = ('小花','小草',classmates_A) #定义一个元组，其中里面包含了列表
print('打印classmates_A与classmatest_B：\n',classmates_A,'\n',classmates_B)
classmates_B[2][0] = '小静'   #更改元组里列表的元素
print('元组中的列表内容\'小红\'已被改变为\'小静\'',classmates_B) #已被改变





