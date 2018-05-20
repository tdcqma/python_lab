import time
import datetime


'''
时间戳，代表从1970年到当前时间所经历过到所有的秒数
    作用：用于做时间之间的加减法，程序运行的时间（结束时间戳-开始时间戳）
    
    两种时间：
        time
        datetime
    
'''
# 一、time模块
# 1.1 时间戳，代表从1970年到当前时间所经历过到所有的秒数
# print(time.time())
# => 1526694376.616259 代表从1970年到当前时间所经历过到所有到秒数

# 2.2 结构化时间输出
# print(time.strftime('%Y-%m-%d %H-%M-%S' ))
# =》 2018-05-19 09-55-35


# 3.3 时间拆分，将本地时间（当前时区，中国的中八区）的每一部分拆分，可以单独调用年、月、日、时分秒等。
# print(time.localtime())
# => time.struct_time(tm_year=2018, tm_mon=5, tm_mday=19, tm_hour=9, tm_min=48, tm_sec=44, tm_wday=5, tm_yday=139, tm_isdst=0)
# 调用.tm_hour得到当前是几点
# print(time.localtime().tm_hour)
# => 9

# 3.4 世界标准时间 tm_hour=9 与 tm_hour=1
# print(time.gmtime())
# => time.struct_time(tm_year=2018, tm_mon=5, tm_mday=19, tm_hour=1, tm_min=51, tm_sec=43, tm_wday=5, tm_yday=139, tm_isdst=0)

# 3.5 将一个结构化struct_time转换为时间戳
# print(time.mktime(time.localtime()))
#=> 1526696000.0

#3.6 将结构化时间转换为格式化的字符串时间
# print(time.strftime('%Y-%m-%d %X',time.localtime()))
# => 2018-05-19 10:15:10

# 3.7 将格式化时间字符串转换为结构化的时间，与strftime相反
# print(time.strptime('2011-05-05 16:37:23','%Y-%m-%d %X'))
# => time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37, tm_sec=23, tm_wday=3, tm_yday=125, tm_isdst=-1)




