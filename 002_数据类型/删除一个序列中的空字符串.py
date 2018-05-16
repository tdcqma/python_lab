# 把一个序列中的空字符串删除，可以这么写：
def not_empty (s):
    return s and s.strip()

a = list(filter(not_empty,['A','','B',None,'C',' ']))
print(a)