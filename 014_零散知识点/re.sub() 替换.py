import re
#　re.sub() 替换
phone = '18898537584 #这是我的电话号码'
print('我的电话号码:',re.sub('#.*','',phone)) #去掉注释
print(re.sub('\D','',phone))    # 在phone里找到非数字的部分，找到后全部替换为空，剩下的就是数字的部分。
print(re.sub('\d','',phone))    # 在phone里找到全是数字的部分，找到后替换为空，剩下的就是非数字的部分。

'''
输出结果：
    我的电话号码: 18898537584 
    18898537584
     #这是我的电话号码
'''