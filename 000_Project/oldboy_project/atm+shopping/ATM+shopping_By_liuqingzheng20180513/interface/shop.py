

from db import db_handler
from interface import bank

def check_shopingcart_interface(name):
    user_dic=db_handler.select(name)
    return user_dic['shoppingcart']


def shoping_interface(name,cost,shoppingcart):
    flag =bank.consume_interface(name,cost)
    if flag:
        user_dic=db_handler.select(name)
        user_dic['shoppingcart']=shoppingcart
        db_handler.save(user_dic)
        return True,'购买成功'
    else:
        return False,'购买失败'

