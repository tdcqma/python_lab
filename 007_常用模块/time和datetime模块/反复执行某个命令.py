import time,os

# 每隔5秒钟执行一次pwd命令
def re_exc(cmd,inc = 60):
    while True:
        os.system(cmd)
        time.sleep(inc)

re_exc("pwd",5)

