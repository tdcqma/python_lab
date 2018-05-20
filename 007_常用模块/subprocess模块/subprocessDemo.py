import subprocess
import time
import os

# subprocess 模块,执行操作系统的命令用，功能类似os.system(command)，但是功能强于os
obj = subprocess.Popen('ifconfig',
                 shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE
                 )

print(obj.stdout.read().decode('utf-8'))    # 从管道符中读出标准正确输出内容或标准错误，解码显示
print('父进程代码继续执行...')
print('父进程代码继续执行...')

# =>
'''
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000 
	inet6 ::1 prefixlen 128 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
XHC20: flags=0<> mtu 0
父进程代码继续执行...
父进程代码继续执行...
'''