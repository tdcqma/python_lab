#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from conf import settings
from core import accounts

def make_transaction(log_obj,account_data,tran_type,amount,**others):
    '''

    :param log_obj:
    :param account_data:
    :param tran_type:
    :param amount:
    :param others:
    :return:
    '''
    amount = float(amount)  # 将转账金额转为浮点型

    # conf/settings.py中TRANSACTION_TYPE保存了4中交易类型，分别是repay、withdraw、transfer、consume
    # 如果用户进行的操作类型在上面四种类型之内则进行处理报错
    if tran_type in settings.TRANSACTION_TYPE:

        # interest 代表用户操作类型所需要支付的利息，
        # 如还款0利息，转账与提现需要0.05的利息，那么利息就是交易金额*利息值
        interest = amount*settings.TRANSACTION_TYPE[tran_type]['interest']

        # 获取用户当前的账户余额
        old_balance = account_data['balance']

        # 逻辑判断，settings.TRANSACTION_TYPE[tran_type]['action']的值一共就有两种类型:plus和minus，但却涵盖了4中交易类型（repay、withdraw,transfer,consume）
        # plus的情况下：最后金额 = 原始金额+交易金额+利息
        # minus的情况下：最后金额 = 原始金额 - 交易金额 - 利息
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest

            if new_balance < 0: # 最后得到但金额如果是小于0则证明原始金额不足，报错
                print('Your credit [%s] is not enough for this transaction [-%s]，your current balance is [%s]' % (account_data['credit'],(amount+interest),old_balance))
                return

        account_data['balance'] = new_balance   # 将得到的最新金额更新到account_data里（account_data是保存用户所有信息的字典变量）
        accounts.dump_account(account_data) # 保存更新金额后的account_data 到用户数据文件里
        log_obj.info("account:%s action:%s amount:%s interest:%s " % (account_data['id'],tran_type,amount,interest)) # 记录交易日记
        return account_data
    else:
        print("\033[03;1mTransaction type [%s] is not exist!" % tran_type)