from db import db_handler

from lib import  common

bank_logger=common.get_logger('bank')

def check_balance_interface(name):
    user_dic=db_handler.select(name)
    return user_dic['balance']


def transfer_interface(from_name,to_name,account):
    to_user_dic=db_handler.select(to_name)
    if to_user_dic:
        from_user_dic=db_handler.select(from_name)
        if from_user_dic['balance']>=account:
            from_user_dic['balance']-=account
            to_user_dic['balance']+=account
            from_user_dic['bankflow'].append('%s 向 %s 转账 %s'%(from_name,to_name,account))
            to_user_dic['bankflow'].append('%s 收到 %s 转账 %s' % (to_name,from_name,account))
            db_handler.save(from_user_dic)
            db_handler.save(to_user_dic)
        else:
            return False,'您的额度不够'
    else:
        return False,'对方账户不存在'



def repay_interface(name,account):
    user_dic=db_handler.select(name)
    user_dic['balance']+=account
    user_dic['bankflow'].append('还款 %s' % ( account))
    db_handler.save(user_dic)
    bank_logger.info('还款成功')
    return True,'还款成功'

def withdraw_interface(name,account):
    user_dic=db_handler.select(name)
    account=account*1.05
    if user_dic['balance']>=account:
        user_dic['balance']-=account
        user_dic['bankflow'].append('取款 %s' % (account))
        db_handler.save(user_dic)
        return True,'取款成功'
    else:
        return False,'余额不足'


def check_records_interface(name):
    user_dic=db_handler.select(name)
    return user_dic['bankflow']


def consume_interface(name,account):
    user_dic=db_handler.select(name)
    if user_dic['balance']>=account:
        user_dic['balance']-=account
        user_dic['bankflow'].append('消费 %s' % (account))
        db_handler.save(user_dic)
        return True
    else:
        return False