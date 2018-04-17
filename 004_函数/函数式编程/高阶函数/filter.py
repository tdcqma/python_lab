# python内建的filter()函数用于过滤序列。

# 和map()类似，filter()函数也是接收一个函数和一个序列，但是和map()不同的是，filter()把传入的
# 函数依次作用域每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 例如：在一个list中，删除偶数，只保留奇数，可以这么写：

def is_odd(n):
    return n%2==1

# is_odd()函数返回是True或者False

a = list(filter(is_odd,[1,2,4,5,6,9,10,15]))
print(a)

# 把一个序列中的空字符串删除，可以这么写：
def not_empty (s):
    return s and s.strip()

a = list(filter(not_empty,['A','','B',None,'C',' ']))
print(a)

# 可见，用filter这个函数的高阶函数，关键在于正确实现一个'筛选'函数。
# 注意，filter返回的是一个Iterator，也是一个惰性序列，所以强迫filter()完成
# 计算结果，需要用list()函数获得所有结果并返回list。


