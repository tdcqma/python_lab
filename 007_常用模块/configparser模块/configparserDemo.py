import configparser

'''
分析配置文件用的模块
读取类似***.ini类型的文件

'''
config = configparser.ConfigParser()
config.read('my.ini')

# print(config.sections())
# print(config.options('python'))

# v1 = config.get('python','age')
# print(v1,type(v1))
# =>123 <class 'str'>

# v2 = config.getint('python','age')
# print(v2,type(v2))
# => 123 <class 'int'>

# v3 = config.getfloat('java','salary')
# print(v3,type(v3))
# => 6.1 <class 'float'>

# v4 = config.getboolean('java','is_good')
# print(v4,type(v4))
# => False <class 'bool'>
