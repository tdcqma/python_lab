from datetime import datetime,date
from apscheduler.schedulers.background import BackgroundScheduler

def job_func(text):
    print(text)

# 在 2019-06-09 时刻运行一次 job_func 方法
# scheduler.add_job(job_func, 'date', run_date=date(2019, 6, 9), args=['text'])

# scheduler.add_job(job_func, 'date', run_date=datetime(2019, 6, 9, 17, 50, 0), args=['text'])


# 在 2017-12-13 14:00:01 时刻运行一次 job_func 方法



if __name__ == '__main__':
    # 创建后台执行的schedulers
    scheduler = BackgroundScheduler()

    # 添加调度任务
    # scheduler.add_job(timedTask,'interval',seconds=2)
    scheduler.add_job(job_func,trigger='date', run_date='2019-06-09 18:00:01', args=['text'])

    # 启动调度任务
    scheduler.start()