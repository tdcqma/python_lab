######## dict  ########
# python的内置字典，全程dictionary，在其他语言中也称为map，使用键-值（key-value）来表示，有点是
#相对于list而言，查询速度要快太多了。

#使用dict来实现一个'名字-成绩'的对照表
d = {'harry':95,'natasha':80,'sarah':88}
print('原始成绩：',d)
#想要打印出某个特定key的value，d[key]即可，如：
print('harry的成绩为：',d['harry'])
#如果要改变某个set里的value值，使用以下方式即可（之前的值会被覆盖掉）
d['harry'] = 33
print('harry成绩变更后为：',d)

# 想dict字典里添加一条key-value值时，需要使用  dict名['key-name'] = value 的方式，如：
d['daniel'] = 22
print('添加一条dict记录后：',d)

# 如果要打印的某个key不存在，dict就会报错，如：
#print(d['anyone'])
#要避免因key不存在而报错的方式有两种，
# 一个是通过'in'来判断key是否存在，如
print('mary' in d)
print('daniel' in d)
print('linda' in d)
# 另一个是通过dict提供的get方法来判断,如果不存在某个key就返回none,
# 如果存在的话就返回该key对应的value值。
print( d.get('danielabc') )
print( d.get('daniel') )
print( d.get('natasha') )
#当没有某个key值的时候除了返回none，也可以指定其他的返回值，如指定返回-1
print(d.get('danielabc',-1))
print(d.get('david',-2))


######## set  ########
# set和dict类似，也是一组key的集合，但不能存储value。
# 由于key不能重复，所以在set中没有重复的key
# 要创建一个set，需要先创建一个list集合作为输入源
#注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素
s = set ([1,2,3])
print(s)
#重复的元素在set中会被自动过滤掉的
a = [1,2,2,3,4,5,6,6,7]
s = set (a)
print('去掉重复元素后的set：',s)
#通过add()方法可以添加重复的元素，但是最终不会成功添加。
s.add(7)
print('添加重复key后的s',s)
#通过remove方法可以删除set中的key
s.remove(7)
print('删除7的key后：',s)

######## 不可变对象  ########

# str是不可以变对象，list是可变对象
#比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c','b','a']
a.sort()
print(a)
#而对于不可变的对象，如str
a = 'abc'
print(a.replace('a','A'))
print(a)


