#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

# 方式一：
# import paramiko
#
# # 括号内指定本地服务器的私钥，同时将公钥上传到要访问到服务器的.ssh目录里，重命名为authorized_keys
# private_key = paramiko.RSAKey.from_private_key_file('id_rsa')
#
# # 生成ssh对象
# ssh = paramiko.SSHClient()
#
# # 允许不再know-host里的主机也可以连接
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# # 使用私钥进行连接
# ssh.connect(hostname='172.27.137.16',port=22,username='pentester',pkey=private_key)
#
# # 执行命令
# stdin,stdout,stderr = ssh.exec_command('ls -l')
#
# # 输出执行结果
# result = stdout.read().decode('utf-8')
# print(result)



# 方式二
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa')

transport = paramiko.Transport(('172.27.137.16',22))
transport.connect(username='pentester',pkey=private_key)

ssh = paramiko.SSHClient()
ssh._transport = transport
stdin,stdout,stderr = ssh.exec_command('ls -l')
result = stdout.read().decode('utf-8')

print(result)

transport.close()






















