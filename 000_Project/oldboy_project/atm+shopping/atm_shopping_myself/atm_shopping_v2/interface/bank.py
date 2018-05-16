from db import db_handler
from lib import common

bank_logger = common.get_logger('bank')

def check_balance_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['balance']

def transfer_interface(from_name,to_name,amount):
    to_user_dic = db_handler.select(to_name)
    if to_user_dic:
        from_user_dic = db_handler.select(from_name)
        if from_user_dic['balance'] >= amount:
            from_user_dic['balance'] -= amount
            to_user_dic['balance'] += amount
            from_user_dic['bankflow'].append('%s向%s转账%s元' % (from_name, to_name, amount))
            to_user_dic['bankflow'].append('%s收到%s转账的%s元' % (to_name, from_name, amount))
            db_handler.save(from_user_dic)
            db_handler.save(to_user_dic)
            bank_logger.info('%s向%s转账%s元'% (from_name,to_name,amount))
            return True,'Transfer successfully.'
        else:
            return False,'The balance is not enough to complete the transaction.'
    else:
        return False,'transfer account doesn\'t exist.'

def withdraw_interface(username,amount):
    '''
    提现
    :param username:
    :param amount:
    :return:
    '''
    user_dic = db_handler.select(username)
    amount = amount * 1.05 # 提现手续费0.05

    if user_dic['balance'] >= amount:
        user_dic['balance'] -= amount
        db_handler.save(user_dic)
        return True,'withdraw successfully.'
    else:
        return False,'the balance is not enough to withdraw.'

def check_records_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['bankflow']

def repay_interface(username,amount):
    user_dic = db_handler.select(username)
    user_dic['balance'] += amount
    user_dic['bankflow'].append('%s 还款 %s元。' % (username,amount))
    db_handler.save(user_dic)
    bank_logger.info('%s 还款 %s 元，还款成功。' % (username,amount))
    return True,'repay successfully.'

def consume_interface(username,amount):
    user_dic = db_handler.select(username)
    if user_dic['balance'] >= amount:
        user_dic['balance'] -= amount
        user_dic['bankflow'].append('cost :%s' % (amount))
        db_handler.save(user_dic)
        return True
    else:
        return False