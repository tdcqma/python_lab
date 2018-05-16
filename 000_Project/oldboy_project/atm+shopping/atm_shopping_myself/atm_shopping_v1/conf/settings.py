#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import os
import sys
import logging

# 获取项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取保存用户数据的根目录
DB_ACCOUNTS_DIR = '%s/db/accounts' % BASE_DIR
print(BASE_DIR)

# 获取保存商品信息的目录
DB_GOODS_DIR = '%s/db/goods' % BASE_DIR

# 数据库字典，涵盖用户的数据认证方式、用户认证对象与数据存储路径
# 该数据会在core/db_handler.py中被调用
DATABASE = {
    'engine':'file_storage',    # 用户是以mysql形式还是以文件形式认证，在这里已经写死了。。。
    'name':'accounts',  # 存储所有用户的上一层的目录名称被定义成了accounts,在这里也被写死了。。。
    'path':"%s/db" % BASE_DIR
}

LOG_LEVEL = logging.INFO
LOG_TYPE = {
    'transaction':'transactions.log',
    'access':'access.log'
}

# 逻辑判断，settings.TRANSACTION_TYPE[tran_type]['action']的值一共就有两种类型:plus和minus，但却涵盖了4中交易类型（repay、withdraw,transfer,consume）

TRANSACTION_TYPE = {
    'repay':{'action':'plus','interest':0},     # interest类似于利息，0代表还款不需要支付手续费
    'withdraw':{'action':'minus','interest':0.05},  # interest类似于利息，0.05代表提现需付0.05手续费
    'transfer':{'action':'minus','interest':0.05},
    'consume':{'action':'minus','interest':0}
}