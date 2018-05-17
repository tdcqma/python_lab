import pickle
import json

# dic = {'name':'python','age':18,'is_beautiful':True}
#序列化
# 1.1 pickle序列化结果是二进制类型
#print(pickle.dumps(dic)) # -> b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x06\x00\x00\x00pythonq\x02X\x03\x00\x00\x00ageq\x03K\x12X\x0c\x00\x00\x00is_beautifulq\x04\x88u.'

# 1.2 对于集合，json无法序列化。但是pickle就可以。
# print(json.dumps({1,2,3})) # -》 报错：TypeError: Object of type 'set' is not JSON serializable
#print(pickle.dumps({1,2,3})) # -》 得到的是一个bytes类型的值，如下所示
'''
b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x06\x00\x00\x00pythonq\x02X\x03\x00\x00\x00ageq\x03K\x12X\x0c\x00\x00\x00is_beautifulq\x04\x88u.'
b'\x80\x03cbuiltins\nset\nq\x00]q\x01(K\x01K\x02K\x03e\x85q\x02Rq\x03.'
'''

# 1.3  简单方式序列化到文件,得到的序列化文件是一个二进制文件
# dic = {'name':'python','age':18,'is_beautiful':True}
# with open('hello_pic.json','wb') as f:
#     pickle.dump(dic,f)

# 1.4 简单方式反序列化读取到字典，如果能打印字典里的内容则说明pickle反序列化成功。
# with open('hello_pic.json',mode='rb') as f :
#     dic = pickle.load(f)
#
#     print(dic['name'])
#     print(dic['age'])
#     print(dic['is_beautiful'])

'''
result：
    python
    18
    True
'''

