# 需要引入三个模块
# 参考链接：https://www.cnblogs.com/alan-babyblog/p/5165579.html

import time,os,sched

schedule = sched.scheduler(time.time,time.sleep)

def perform_command(cmd,inc):
    # 安排inc秒后再次运行自己，即周期运行
    schedule.enter(inc,0,perform_command,(cmd,inc))
    os.system(cmd)

def timming_exe(cmd,inc = 60):
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(inc,0,perform_command,(cmd,inc))

    # 持续运行，直到计划时间队列变成空为止
    schedule.run()

print("show time after 10 seconds:")
timming_exe("pwd", 3)