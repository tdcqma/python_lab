
num = input('please input a number: ').strip()

sum_num = 0
for i in range(0,int(num)):
    if i % 2 == 0:
        pass
    else:
        print(i)
        sum_num += i

print('0到%s之间的奇数和为%s' % (num,sum_num))
