import configparser

'''
分析配置文件用的模块
读取类似***.ini类型的文件

'''

# 创建对象与读取文件
config = configparser.ConfigParser()
config.read('my.ini')

# 获取my.ini里面所有中括号内容，即分组的组名内容
print(config.sections())

# 取出'java'组的所有key，保存至列表
print(config.options('java'))

# 取出java组的所有key-value值
print('-->',config.items('java'))

# 取出不同数据类型的值
print(config.get('python','name'))
print(config.getint('java','age'))
print(config.getfloat('java','salary'))
print(config.getboolean('python','is_good'))
print(config.get('java','is_good'))