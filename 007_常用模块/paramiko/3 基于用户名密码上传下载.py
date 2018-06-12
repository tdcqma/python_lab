#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import paramiko

# 一、文件上传
# 建立连接信息
# transport = paramiko.Transport(('172.27.137.16',22))
# transport.connect(username='pentester',password='123456')
#
# # 生成sftp对象
# sftp = paramiko.SFTPClient.from_transport(transport)
#
# # 将upload_testfile.txt上传至服务器的/home/pentester/temp目录下
# sftp.put('upload_testfile.txt','/home/pentester/temp/upload_testfile.txt')
# print('upload ok!')
#
# transport.close()


# 二、文件下载
# transport = paramiko.Transport(('172.27.137.16',22))
# transport.connect(username='pentester',password='123456')
#
# sftp = paramiko.SFTPClient.from_transport(transport)
# sftp.get('/home/pentester/temp/client_file.txt','./client_file.txt')
# print('download ok!')
#
# transport.close()