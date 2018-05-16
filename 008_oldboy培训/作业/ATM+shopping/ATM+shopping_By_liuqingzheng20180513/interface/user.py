
from db import db_handler
def register_interface(name,password,balance=1500):
    user_dic=db_handler.select(name)
    if user_dic:
        return False,'用户已经存在'
    else:
        user_dic={
            'name':name,
            'password':password,
            'lock':False,
            'balance':balance,
            'credit':balance,
            'bankflow':[],
            'shoppingcart':{}
        }

        db_handler.save(user_dic)
        return True,'注册成功'


def login_inteface(name,password):
    user_dic=db_handler.select(name)
    if user_dic:
        if password == user_dic['password'] and not user_dic['lock']:
            return True,'登录成功'
        else:
            return False,'密码错误或者已经锁定'

    else:
        return False,'用户不存在'
