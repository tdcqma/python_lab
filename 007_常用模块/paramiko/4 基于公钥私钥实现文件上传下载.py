#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa')

transport = paramiko.Transport(('172.27.137.16',22))
transport.connect(username='pentester',pkey=private_key)

sftp = paramiko.SFTPClient.from_transport(transport)

# 将upload_testfile.txt文件上传至服务器的/home/pentester/temp/upload_testfile.txt文件里
#sftp.put('upload_testfile.txt','/home/pentester/temp/upload_testfile.txt')

# 将远程服务器上的/home/pentester/temp/client_file.txt文件保存到本地当前目录，命名文件名为new_client_file.txt
#sftp.get('/home/pentester/temp/client_file.txt','./new_client_file.txt')

print('transfer ok!')
transport.close()