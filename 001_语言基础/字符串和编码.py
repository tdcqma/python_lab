#关于编码问题详细的说明请看http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000

# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，例如：
print('包含中文的str')

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示
b = ord('b')
print('b =',b)
print('a =',ord('a'))
print('我 =',ord('我'))
print('97 =',chr(97))
print('1111 =',chr(1111))
print('-----华丽分割线-----')
'''
python的字符串类型是str，在内存中以unicode表示，一个字符串对应若干个字节，如果
在网络上传输或者保存在磁盘上的时候就需要把str变为以字节为单位的bytes。
python对bytes类型的数据展示用b加上或双引号表示
要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
'''
x = b'ABC'
print(x)
print('-----华丽分割线-----')


'''
以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
纯英文的str可以用ASCII编码为bytes，内容是一样的，
含有中文的str可以用UTF-8编码为bytes。
'''
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))  含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

print('-----华丽分割线-----')

'''
如果我们从网络上或磁盘上读取数据，那么读到应该bytes，就要把bytes转换为str，需要用到decode（）方法
'''
x = b'ABC'.decode('ascii')
print(x)
y = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(y)

print('-----华丽分割线-----')

#计算字符个数，使用len()函数
print('计算字符个数，使用len()函数')
print(len('中文输入法'))
#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len(b'abc'))
print(len('中文'.encode('utf-8')))
#可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

'''
由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，
就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
    #!/usr/core/env python3
    # -*- coding: utf-8 -*-
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
'''

print('-----华丽分割线-----')

#输出格式化的字符串
#我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，
# 而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。

print( '亲爱的%s你好！你%d月的话费是%f，余额是%f元' % ('张三',5,328.88,0.32) )
