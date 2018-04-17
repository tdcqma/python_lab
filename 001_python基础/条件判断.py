age = int( input('please input your age:') )

if age >= 18 :
    print('your age is ' , age)
    print('adult')  #如果年龄大于18岁输出'已成年'

elif age >= 6 :
    print('your age is ', age)
    print('teenager')
else :
    print('You are a kid')

#if 语句有个特点，就是从上往下以此执行，遇到True并执行后，之后的所有elif或else就不执行了。
#所以在设计if逻辑的时候一定要想好先后顺序

# if条件判断语句还可以简写成以下方式：
if 2 > 1 : print('true')

