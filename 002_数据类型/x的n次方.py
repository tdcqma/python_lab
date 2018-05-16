def power_yh (x,n):
    s = 1
    while n > 0 :
        n = n -1
        s = s * x
    return s

print( power_yh(4,3) )