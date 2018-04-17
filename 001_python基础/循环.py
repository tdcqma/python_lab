#python的循环有两种，一种是for循环，另一种是while循环。

# 一、for循环

# 定义一个list列表classmates，然后打印出来
classmates = ['harry','natasha','sarah']
for i in classmates :   #for循环打印出该列表内容
    print(i)

# 通过使用for循环打印0-10之间的数字只和
sum = 0
for i in [0,1,2,3,4,5,6,7,8,10] :
    sum += i
print('0-10之间的和为：',sum)

#python提供了一个range（）函数，可以打印一个整数序列，如：
print('打印range(11)：',range(11))
#如果想要打印出每个元素，可以借助list函数打印
print('通过list函数打印range()里面的内容：',list(range(11)))


#使用for循环打印0-10之间的和。
sum = 0
for i in list(range(101)) :
    sum +=i
print('使用for循环+list+range函数打印0-100之间的和：',sum)

#使用for循环+range（）函数打印0-100之间的和
sum = 0
for i in range(101) :
    sum += i
print('使用for循环+range（）函数打印0-100之间的和:',sum)


# 二、while循环

#只要条件满足就一直循环，条件不满足时就退出
#例如，计算0-100之间的所有奇数之和

sum = 0
n = 99

while n > 0 :
    sum = sum + n
    n = n - 2
print('使用while循环计算0-100之间的奇数之和：',sum)

# break语句：在整个循环语句中遇到break即跳出整个循环，如：
#循环打印1-100之间的数字
n = 1
while n <=100 :
    print(n)
    n += 1
print('END')
#对于以上语句，如果想要提前结束就使用break
n = 1
while n <=100 :
    if n > 10 : #添加判断语句，如果n > 10 ,即n=11的时候自动执行后边的break跳出整个循环。
        break
    print(n)
    n += 1
print('END')

# continue语句：循环中遇到continue语句的时候会跳过当前这一次的循环，进入到下一次循环。
n = 0
while n < 10 :
    n = n+1
    print(n)
#上面的程序可以打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：
n = 0
while n < 10:
    n = n + 1
    if n%2 == 0 :
        continue
    print(n)

