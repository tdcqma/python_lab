'''
1、 什么是序列化
    序列化：把内存中的数据转成一种中间格式（json/pickle），然后保存到硬盘中，数据永久保存
    反序列化：从文件中读出json或pickle格式，然后反解成python的数据类型
2、为什么要序列化
    1、数据结构持久化
    2、跨平台数据交互

3、如何进行序列化、反序列化
    json：
        缺点：
            只能支持部分python的数据类型，不支持元组、集合
        优点：
            所有的语言都支持json格式，大部分都在用json
        应用：
            如果需要考虑到跨平台性，需要用json格式
    pickle：
        缺点：
            只有python支持pickle格式
        优点：
            pickle能够支持所有的python数据类型
        应用：
            如果不需要考虑到跨平台性，可以考虑使用pickle格式
'''
import json

#序列化
# 3.1 python的数据类型转换成json格式后大部分都相似，如单引号变成了双引号，python的True变成了json的true（小写）
# dic = {'name':'python','age':18,'is_beautiful':True}
# print(json.dumps(dic))  # -> {"name": "python", "age": 18, "is_beautiful": true}

# 3.2 将字符串序列化后写入文件,执行后在同级目录下生成hello.json文件，
# 内容为{"name": "python", "age": 18, "is_beautiful": true}
# dic = {'name':'python','age':18,'is_beautiful':True}
# res = json.dumps(dic) # 序列化后保存到变量res
# with open('hello.json','w',encoding='utf-8') as f:
#     f.write(res)

# 3.3 简单方式：json.dump(dic,f),执行后同级目录生成hello.json
# dic = {'name':'python','age':18,'is_beautiful':True}
# with open('hello.json','w',encoding='utf-8') as f:
#     json.dump(dic,f)

# 反序列化
# 3.4 从序列化生成的文件hello.json中读内容，反序列化操作，如果读出来的内容是字典类型，
# 并且可以打印出内容代表反序列化成功。
# with open('hello.json',mode='r',encoding='utf-8') as f:
#     res = f.read()
# dic=json.loads(res) # 反序列化
# print(dic['name'])
# print(dic['age'])
# print(dic['is_beautiful'])
'''
result：
    python
    18
    True
'''

# 3.5 简单实现方式json.load(f),执行结果与上面一样。
with open('hello.json','r',encoding='utf-8') as f:
    dic = json.load(f)
    print(dic['name'])
    print(dic['age'])
    print(dic['is_beautiful'])


