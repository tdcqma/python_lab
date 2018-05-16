from db import db_handler
from interface import bank

def check_shoppingcart_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['shoppingcart']

def shopping_interface(username,cost,shoppingcart):
    '''

    :param username:
    :param cost:
    :param shoppingcart:
    :return:
    '''
    flag = bank.consume_interface(username,cost)
    if flag:
        user_dic = db_handler.select(username)
        user_dic['shoppingcart'] = shoppingcart
        db_handler.save(user_dic)
        return True,'buy successfully.'
    else:
        return False,'buy failture.'