# 在函数内部可以调用其他函数，如果在函数内部调用自身函数就是递归函数。

def fact (n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(100))