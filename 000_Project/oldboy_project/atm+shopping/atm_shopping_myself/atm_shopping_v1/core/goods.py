#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from conf import settings
import json
import os
# 获取商品数据信息路径，即：ATM/db/goods/goods.json文件
goods_file_path = '%s/db/goods/goods.json' % settings.BASE_DIR

# 从goods.json文件中获取商品列表，返回字典格式
def show_goods_list():
    with open(goods_file_path) as f:
        goods_data = json.load(f)
        return goods_data


def dump_goods(account_data,select_goods_dic):
    '''
    将商品信息加入购物车
    将更新后的数据写入用户db文件内
    :param account_data:
    :return:
    '''

    # db_path 指向项目根目录，即ATM
    db_path = settings.BASE_DIR
    # shopping_path最后指向用户自己的购物车路径，即：ATM/db/shopping_car/用户ID.json
    shopping_path = '%s/db/shopping_car/%s.json' % (db_path,account_data['id'])

    # 通过json.dump()写入数据
    with open(shopping_path,'w') as f:
        acc_data = json.dump(select_goods_dic,f)

    # 写入成功后返回True
    return True

# 接收用户输入的商品编号，确认价格与数量是否有效，无误后调用加入购物车函数
def add_to_shoppingCar(acc_data,goods_list):
    # 获取用户想要购买商品的编号
    select_goodID = input('please select goods\'s id:').strip()

    # print('您选择商品编号：',select_goodID)
    # print('您的账户信息：',acc_data)

    goods_res = goods_list[select_goodID]   # => {'Iphone': {'price': 8800, 'remaining_no': 10}}

    # 判断依据：1. 用户剩余金额大于（购买数量X商品单价） 2. 商品仍有剩余
    # k:商品名称
    # v['price']:商品价格
    # v['remaining_no']：商品剩余个数
    select_goods_dic = {
        "goods_no":0,
        "goods_name":"",
        "goods_num":0,
        "goods_amount":0,
        "buy_status":0  # 0:未购买，1，已购买
    }
    select_goods_dic["goods_no"] = select_goodID
    buy_flag = False
    for k,v in goods_res.items():
        select_goods_dic["goods_name"] = k

        # goods_quantity接收用户输入的商品数量
        goods_quantity = int(input('please input quantity of %s: ' % (k)).strip())
        select_goods_dic["goods_num"] = goods_quantity

        if v['remaining_no'] >= goods_quantity : # 如果库存大于用户选择的商品数量
            select_goods_dic["goods_amount"] = goods_quantity * float(v['price'])
        else:
            buy_flag = True

    print('\n用户信息acc_data：',acc_data)

    # 获取当前用户的可用余额
    cur_balance = acc_data["account_data"]['balance']

    # 判断用户余额是否大于购买金额，如果大于允许加入购物车
    if cur_balance >= select_goods_dic["goods_amount"] and not buy_flag:

        shop_car_info = ' 待加入购物车的信息：\n  商品名称:%s\n  购买数量:%s\n  商品总价：%s' % (select_goods_dic["goods_name"], select_goods_dic["goods_num"], select_goods_dic["goods_amount"])
        print(shop_car_info)
        is_add_to_shopcar = input('Please confirem add to the shoppingCar?(y/n): ').strip()

        if is_add_to_shopcar == 'y':
            # print('调用加入购物车函数，加入购物车操作中')
            # print('select_goods_dic',select_goods_dic)
            add_shopCar_res = dump_goods(acc_data['account_data'],select_goods_dic)

            if add_shopCar_res:
                print('成功加入购物车！')
            else:
                print('加入购物车失败！')

        # print('cur_balance',cur_balance)
        # print('goods_amount',goods_amount)
    else:
        print('余额或商品数量不足，无法购买！请重新确认。')

def load_myself_shoppingCar(acc_data):
    '''
    读取自己购物车的信息,返回值为购物车列表shoppingCar_data
    :param acc_data: 用户所有的数据，即ATM/db/accounts/用户id.json
    :return:
    '''

    # db_path 路径指向ATM/db/accounts目录
    shoppingCar_path = '%s/db/shopping_car/%s.json' % (settings.BASE_DIR,acc_data['account_data']['id'])
    # print('acc_data~~~~~~~~~~~~~~~~>',acc_data)
    #找到了用户购物车数据文件的路径，就可以通过文件的读操作来获取用户的所有购物车信息，保存在shoppingCar_data中并作为函数的返回值返回。

    if os.path.isfile(shoppingCar_path):
        with open(shoppingCar_path) as f :
            shoppingCar_data = json.load(f)
            return shoppingCar_data
    else:
        return None