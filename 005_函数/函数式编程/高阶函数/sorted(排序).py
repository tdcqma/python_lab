# python内置的sorted()函数可以对list进行排序

a = sorted([35,2,6,23,-3,26,-123])
print(a)

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现
# 自定义的排序，例如按绝对值大小排序：

a = sorted([36,5,-12,9,-21],key=abs)
print('按绝对值大小排序：',a)

# key指定的函数将作用域list的每一个元素上，并根据key函数返回的结果进行
# 排序，对比原始的list和经过key=abs处理的list
# 按绝对值大小排序： [5, 9, -12, -21, 36]

# 对字符串惊醒排序是按着ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在
# 小写字母a的前面。

a = sorted(['bob','about','Zoo','Credit'])
print(a)

print('将ASCII字符转换为对应的数值:C =',ord('C'))
print('将ASCII字符转换为对应的数值:Z =',ord('Z'))
print('将ASCII字符转换为对应的数值:a =',ord('a'))
print('将ASCII字符转换为对应的数值:b =',ord('b'))

# 现在，我们提出排序应该忽略大小写，按照字母排序。要实现这个算法，不必对现有代码
# 大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来
# 来比较两个字符串，实际上就是先把字符串变成大写（或者都变成小写），再比较。
# 这样，我们给sorted传入key函数，即可实现忽略大小写的排序：
a = sorted(['bob','about','Zoo','Credit'],key=str.lower)
print('忽略大小写，正向排序：',a)

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
a = sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True)
print('忽略大小写，反向排序：',a)