import schedule
import time

def job():
    print("i'm working...")

# schedule.every().day.at("13:26").do(job)    # 每天13:26分执行
schedule.every(1).minutes.do(job)   # 每分钟执行一次

while True:
    schedule.run_pending()
    time.sleep(1)