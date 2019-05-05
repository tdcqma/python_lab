# hello

# 1.计算明天和昨天的日期

# 获取昨天、今天、明天的日期

import datetime

# 获取今天日期
today = datetime.date.today()
print(today)
# 输出 2019-05-05

# 获取昨天日期
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
# 输出 2019-05-04

# 获取明天日期
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)
#2019-05-06
