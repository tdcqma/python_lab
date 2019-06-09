import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler

def timedTask():
    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

if __name__ == '__main__':
    # 创建后台执行的schedulers
    scheduler = BackgroundScheduler()

    # 添加调度任务
    scheduler.add_job(timedTask,'interval',seconds=2)

    # 启动调度任务
    scheduler.start()

    while True:
        print(time.time())
        time.sleep(5)