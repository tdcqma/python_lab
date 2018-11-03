'''使用get()方法获取字典中某个key对应的value'''

abc = {'name':'alex','age':18}

print('--->',abc.get('name'))
print(abc.get('age'))
print(abc.get('salary','无'))
print(abc.get('pysec','派森'))    # 如果没有pysec这个key，就打印后面的派森

'''
输出结果：
---> alex
18
无
派森
'''