import random

# 1.1 random.random()
# 大于0且小于1之间的小数
res = random.random()
# print(res)
# 取任意N位整数，N代表1后边0的个数
# print(int(res*100))

# 1.2 random.randint(m,n), 大于等于m且小于等于n之间的整数
# print(random.randint(1,3))

# 1.3 random.randrange(m,n), 大于等于m且小于n之间的整数
# print(random.randrange(1,3))

# 1.4 random.choice([元素1，元素2，元素3....]) 选择括号内列表里的任意一个元素出来
# print(random.choice(['1','ab','测试','**']))

#1.5 random.sample([元素1，元素2，元素3....],m)列表元素任意m个组合
# print(random.sample(['1','ab','测试','**'],2))
# => ['**', 'ab']
# => ['测试', '1']
# => ['1', '**']

# 1.6 random.uniform(m,n) 获取大于m小于n之间的小数
# print(random.uniform(1,3))
# => 1.6461568960284345
# => 2.6216900041752416

# 1.7 洗牌（打乱顺序）
# l = [1,2,3,4,5]
# random.shuffle(l)
# print(l)
# => [5, 1, 2, 3, 4]
# => [5, 3, 1, 4, 2]