# encoding:utf-8

'''
>>  一个中文字符是3个字节
'''

# <1> 普通的文件打开方式
#f = open(r'/home/hbma/pylearn/ioTest/a.txt',mode='r',encoding='utf-8')
#data = f.read()
#print(data)
#f.close()

# <2> 使用with ... as f:的形式会自动将文件关闭，即f.close()
#with open(r'a.txt',mode='r',encoding='utf-8') as f:
#	data = f.read()
#	print(data)

# <3> 同时打开多个文件添加多个open，多个open之间换行显示，使用“\”
#with open(r'a.txt',mode='r',encoding='utf-8')as f1,\
#	open (r'b.txt',mode='r',encoding='utf-8') as f2:
#	d1 = f1.read()
#	d2 = f2.read()
#	print(d1)
#	print(d2)

# <4> -r模式下，使用f.readline()代表执行一次执行一行的代码>
#with open(r'a.txt',mode='r',encoding='utf-8') as f1:
#	d1 = f1.readline()
#	print('第一次：')
#	print(d1)
#	d2 = f1.readline()
#	print('第二次：')
#	print(d2)
#	d3 = f1.readline()
#	print('第三次：')
#	print(d3)
#	d4 = f1.readline()
#	print('第四次：')
#	print(d4)

# <5> readlines()类似于read(),一次全部读取，将读取的每一行当成一个元素存在列表里。
#with open(r'a.txt',mode='r',encoding='utf-8') as f:
#	data = f.readlines()
#	print(data)

# <6> -r模式的时候，如果文件不存在，则报错，报错内容：IOError: [Errno 2] No such file or directory: 'c.txt'
#with open(r'c.txt',mode='r',encoding='utf-8') as f:
#	pass

#<7>  -w 只写模式，写操作,内部代码什么都没写，只是pass的话，如果a.txt不存在，则创建；如果a.txt存在，则清空文件内容
#with open(r'a.txt',mode='w',encoding='utf-8') as f:
#	pass
#with open(r'c.txt',mode='w',encoding='utf-8') as f: # c.txt文件不存在，创建
#	pass


#<8> 判断对象是可读还是可写
#with open('b.txt',mode='w',encoding='utf-8') as f:
#	print(f.readable())
#	print(f.writable())

#<9> -w模式为写模式，使用f.write()写入文件，写的操作没有换行 
#with open(r'a.txt',mode='w',encoding='utf-8') as f:
#	f.write('wolegequ\n')
#	f.write('ganmaonanshou')

# <10> f.writelines()相当于把一个列表进行for循环，然后依次把列表里的每个元素都写入到指定文件中。
#l = ['china is good\n','china is ok\n','shanghai is beautiful\n']
#with open(r'a.txt',mode='w',encoding='utf-8') as f:
#	f.writelines(l)

#<11> a模式：追加写模式(不可读)，文件存在指针移动到文件末尾进行添加，文件不存在则创建文件
#with open(r'a.txt',mode='a',encoding='utf-8') as f:
#	f.writelines('!!!!\n')
#	f.writelines('@@@@\n')

#<12> 读取文件内所有的内容，使用for循环读取，去除print自带的换行使用end=''来解决
#with open(r'a.txt',mode='r',encoding='utf-8') as f:
#	for line in f:
#		print(line,end='')
