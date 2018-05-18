'''
1、 什么是正则
    正则就是用一堆特殊符号组成的规则去一个字符串/文本中匹配出符合规则的内容

2、 正则表达式的使用
'''
import re

#2.1 \w 匹配一个字符，可以是数字、字母及下划线
# print(re.findall('\w','ab_123 4_c\n\t'))
# =>['a', 'b', '_', '1', '2', '3', '4', '_', 'c']

#print(re.findall('a','ab_12a3 4_c\n\t'))
# => ['a', 'a']

# print(re.findall('ab','ab_12aaab3 4_c\n\t'))
# => ['ab', 'ab']

#2.2 \W 匹配一个非数字、非字母非下划线的字符
#print(re.findall('\W','ab_12aaab3 4_c\n\t'))
# => [' ', '\n', '\t']

# 2.3 \s 匹配任意空白字符，等价于[\t\n\r\f]
# print(re.findall('\s','ab_123 4_t\t\nsl'))
# => [' ', '\t', '\n']
# print(re.findall('\s\s','ab  cdef 123 \t\n1111'))
# => ['  ', ' \t']

# 2.4 \S 匹配任意非空字符
# print(re.findall('\S\S\S','ab_1 23  4_c\n\t'))
# => ['ab_', '4_c']

# 2.5 \d 匹配数字，等价于[0-9]
# print(re.findall('\d','ab_123,asdf*(s2\''))
# => ['1', '2', '3', '2']

# 2.6 \D 匹配任意非数字
# print(re.findall('\D','ab_123,asdf*(s2\''))
# => ['a', 'b', '_', ',', 'a', 's', 'd', 'f', '*', '(', 's', "'"]

# 2.7 ^ (上尖号) 匹配以...开头对内容
# print(re.findall('^python','python is good.'))
# => ['python']
# print(re.findall('^python','hello python.'))
# => []

# 2.8 $ 匹配以...结尾对内容
# print(re.findall('good$','python is good'))
# =>['good']
# print(re.findall('python$','python is good'))
# =>[]

# 2.9 重复匹配 .

# . 代表任意一个除换行符之外的字符
# print(re.findall('a.c','123123a1c a2c aac somebodyissb aaaaaaac a-c a\nc a*c '))
# =》['a1c', 'a2c', 'aac', 'aac', 'a-c', 'a*c']
# . 虽然默认不匹配换行符，但是仍可以使用re.DOTALL指定使其匹配换行
# print(re.findall('a.c','123123a1c a2c aac somebodyissb aaaaaaac a-c a\nc a*c ',re.DOTALL))
# => ['a1c', 'a2c', 'aac', 'aac', 'a-c', 'a\nc', 'a*c']

# 2.10 重复匹配 ?
# ? 代表匹配左边的字符有0个或这1个
# print(re.findall('ab?','a ab abb abbb abbbbbbbb bbbbbaaa123'))
# => ['a', 'ab', 'ab', 'ab', 'ab', 'a', 'a', 'a']

# 2.11 匹配 *
# * 代表匹配左边字符有0个或任意个
# print(re.findall('ab*','a ab abb abbb abbbbbbbb bbbbbaaa123'))
# ['a', 'ab', 'abb', 'abbb', 'abbbbbbbb', 'a', 'a', 'a']

# 2.12 匹配 +
# + 号代表左边的左边的字符至少有1个，或者无穷个
# print(re.findall('ab+','a ab abb abbb abbbbbbbb bbbbbaaa123'))
# => ['ab', 'abb', 'abbb', 'abbbbbbbb']
































