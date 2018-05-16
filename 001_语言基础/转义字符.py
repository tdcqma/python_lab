'''
转义字符
  （1）使用反斜杠 \ 来表示
  （2）使用r''来表示
'''

# \n  ->换行
print('natasha:hello harry \nharry: hello natasha')

# \t  ->制表符
print(1234)
print('1\t2\t3\t4')

# \   ->本身也需要转义,即\\
print('请把反斜杠\\打印出来')


print(r'\t123\n321')
print(r'\\')