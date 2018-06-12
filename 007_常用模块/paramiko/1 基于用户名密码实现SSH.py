#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()

# 允许连接不再Know_hosts里的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname='192.168.23.127',port=22,username='root',password='123456')

# 执行命令
stdin,stdout,stderr = ssh.exec_command('ls -l')

# 获取命令结果
result = stdout.read().decode('utf-8')

print(result)