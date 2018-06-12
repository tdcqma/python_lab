'''使用get()方法获取字典中某个key对应的value'''

dict = {'name':'alex','age':18}

print(dict.get('name'))
print(dict.get('age'))
print(dict.get('salary','无'))

'''
输出结果：
    alex
    18
    无
'''