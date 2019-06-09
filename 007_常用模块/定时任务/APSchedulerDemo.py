# APScheduler的安装：pip install apscheduler
# refer:https://www.cnblogs.com/qq1207501666/p/9195186.html

from apscheduler.schedulers.blocking import BlockingScheduler
import time,datetime

sched = BlockingScheduler()

def my_job():
    print(datetime.datetime.now())

sched.add_job(my_job,trigger='date',run_date='2019-06-09 18:01:00')
sched.start()



# def print_args(*args):
#     """
#     要定时执行的函数
#     :param args: 参数
#     :return: None
#     """
#     for arg in args:
#         print(arg)


# sched.add_job(func=print_args, args=['a', 'b', 'c'], trigger='cron', day_of_week='0-6', hour=17, minute=23,start_date='2019-06-09',end_date='2019-06-10')  # 表示周一到周五的5点半执行,有效日期是2016-06-06 00:00:00 至 2018-08-08 00:00:00
# sched.add_job(func=print_args, args=['a', 'b', 'c'], trigger='cron', day='9,11', hour=17, minute=26,start_date='2019-06-09',end_date='2019-06-10')  # 表示周一到周五的5点半执行,有效日期是2016-06-06 00:00:00 至 2018-08-08 00:00:00
# sched.add_job(func=print_args, args=['a', 'b', 'c'], trigger='cron', day='9,11', hour=17, minute=26,start_date='2019-06-09',end_date='2019-06-10')  # 表示周一到周五的5点半执行,有效日期是2016-06-06 00:00:00 至 2018-08-08 00:00:00



# sched.start()