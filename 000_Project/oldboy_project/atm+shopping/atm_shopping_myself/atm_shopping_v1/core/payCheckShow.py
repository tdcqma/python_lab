#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from conf import settings

log_path = settings.BASE_DIR
file_Abspath = '%s/log/transactions.log' % log_path # ATM/log/transactions.log

show_loglist = []
def pay_check(user_id):
    user_logFlag = 'account:%s' % user_id   # 标示用户，用于区分不同用户的不通日志

    with open(file_Abspath,'r') as f:
        data = f.read()

    # 将日志文件转换成列表，每行为一条记录也是一个元素
    log_list = data.split('\n')

    for log_line in log_list:
        if user_logFlag in log_line:
            show_loglist.append(log_line)

    print('用户[%s]的交易日志：' % user_id)
    for s_line in show_loglist:
        print(s_line)