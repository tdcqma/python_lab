# -*- coding: utf-8 -*-
import paramiko
'''
注意：通过python实现SSH公钥登录的前提是要把本地主机的公钥发送到要访问主机的~/.ssh/authorized_keys文件里。
具体存放方式可参考【链接】SSH公钥认证登录：
http://www.cnblogs.com/tdcqma/p/5685090.html
'''
while True:
    user_cmd = input('please input remote server\'s cmd(quit:q): '.strip())

    if user_cmd == 'q':
        break
    pkey='/Users/mahaibin/.ssh/id_rsa'  #本地密钥文件路径
    key=paramiko.RSAKey.from_private_key_file(pkey) #获取本地的key到变量
    paramiko.util.log_to_file('paramiko.log')
    ssh = paramiko.SSHClient()  # 创建SSH对象
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #忽略不在known_hosts 文件中存在的主机
    ssh.connect('192.168.12.1',username = 'pentest',pkey=key) #指定主机、用户名后即可登录
    stdin,stdout,stderr=ssh.exec_command(user_cmd) # 执行命令
    print(stdout.read().strip().decode('utf-8'))    # 查看结果