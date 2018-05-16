from db import db_handler

def register_interface(username,password,balance=15000):
    '''
    用户注册
    :param username: 用户名
    :param password: 密码
    :param balance: 用户余额
    :return:
    '''
    user_dic = db_handler.select(username)
    if user_dic:
        return False,'The user [%s] is already exists and cannot be registered.' % user_dic['username']
    else:
        user_dic = {
            'username':username,
            'password':password,
            'lock':False,
            'balance':balance,
            'credit':balance,
            'bankflow':[],
            'shoppingcart':{},
        }
        db_handler.save(user_dic)
        return True,'user [%s] registered successfully.' % user_dic['username']

def login_interface(username,password):
    '''
    用户登录
    :param username:
    :param password:
    :return:
    '''
    user_dic = db_handler.select(username)
    if user_dic:
        if password == user_dic['password'] and not user_dic['lock']:
            return True,'[%s] login successfully.' % username
    else:
        return False,'user [%s] doesn\'t exist.' % username
