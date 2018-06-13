#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import configparser
import paramiko
from optparse import OptionParser

def get_host_info(host):
    '''
    将多个字符串格式主机转化为列表并返回
    :param hostname: 字符串格式，h1,h2 <class 'str'>
    :return:
    '''
    return host.split(',')

def paramiko_connect(host_ip,port,username,password,cmd):
    # 创建SSH对象
    ssh = paramiko.SSHClient()

    # 允许连接不再Know_hosts里的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    ssh.connect(hostname=host_ip, port=port, username=username, password=password)

    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(cmd)

    # 获取命令结果
    result = stdout.read().decode('utf-8')

    return result

if __name__ == '__main__':

    #通过OptionParser获取用户输入的参数
    parser = OptionParser()
    parser.add_option("-H","--host",dest="host",help="hose name",type="string")
    parser.add_option("-g", "--group", dest="group", help='group name', type="string")
    parser.add_option("-c", "--commend", dest="cmd", help='commend', type="string")
    parser.add_option("-m", "--module", dest="module", help='module', type="string")
    parser.add_option("-s", "--src", dest="src", help='source file or path', type="string")
    parser.add_option("-d", "--dst", dest="dst", help='destination file or path', type="string")
    parser.add_option("-a", "--action", dest="action", help='action for module file, [get/put]', type="string")

    # 获取参数列表
    (option,args) = parser.parse_args()

    # 拿到主机名、shell标示，以及要执行的命令
    target_host = option.host
    target_group = option.group
    module = option.module
    uesr_cmd = option.cmd

    target_host_list = []


    # （一）如果是执行shell命令，则进入以下分支
    if module == 'shell':
        config = configparser.ConfigParser()
        config.read('host_info')

        # 判断用户输入的主机是否在配置文件的主机列表里
        # 1. 将配置文件的选项都读出来，得到['h1', 'h2', 'h3','group1']
        config = configparser.ConfigParser()
        config.read('host_info')
        conf_host_list = config.sections()
        # print('conf_host_list:',conf_host_list)

        # 2. 判断用户输入的单独主机是否在配置文件列表里,如果存在则记录到conf_host_list
        if target_host != None:
            # 用户可能输入多个不同主机，将连在一起的字符串格式的主机名分开，存储在列表里。
            user_hostname_list = get_host_info(target_host)

            for host in user_hostname_list:
                if host in conf_host_list:
                    target_host_list.append(host)
                else:
                    print('主机(%s)不存在，请添加信息到配置文件后进行使用。' %(host))

        # 3. 判断用户输入到组主机是否存在于配置文件列表里，如果存在则记录到conf_host_list
        if target_group != None:
            # 3. 获取用户输入的群组主机信息
            # print('user_group--->',target_group)
            user_group_list = get_host_info(target_group)
            # print(user_group_list)

            # 获取配置文件中的群组信息
            for group in user_group_list:
                if group in conf_host_list:
                    # print(group)
                    group_item_list = config.options(group)
                    for host in group_item_list:
                        group_item = config.get(group, host)    # h1,h2...
                        # print('~~~~~',group_item)
                        target_host_list.append(group_item)
                        # print('~~~~', config.options(group_item))
                        # print(config.get(group_item,'hostname'))
                    # 用户输入的组信息在配置文件主机组里存在，继续执行
                else:
                    print('no')

        # 4. 收集由 -H 与 -g组合得来的所有host主机，并利用集合去重
        target_host_list = set(target_host_list)

        # 5. 调用paramiko模块依次对target_host_list里对主机执行命令。
        for host in target_host_list:
            # 获取主机的主机名、端口、用户名、密码
            host_ip = config.get(host,'hostname')
            host_port = int(config.get(host,'port'))
            host_uname = config.get(host,'username')
            host_pwd = config.get(host,'password')
            # print(host,'-->',host_ip,host_port,host_uname,host_pwd)

            # 如果在配置文件主机列表里，调用paramiko进行连接
            result = paramiko_connect(host_ip,host_port,host_uname,host_pwd,uesr_cmd)
            print('主机(%s)IP:%s \n返回结果:%s' % (host,host_ip,result))

    # （二）如果进行文件上传或下载，则执行以下分支
    elif module == 'file':
        pass

    # （三）执行其他操作则报错
    else:
        print('目前仅支持shell命令与上传下载文件。')