# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

def fib (max) :
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1
    return 'done'
print(fib(11))