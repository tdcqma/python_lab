#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma
#
#
# a = input('a>>>>').strip()
# exit()
# b = input('b>>>>').strip()

import json
from conf import settings

goods_dic = {

    1:{
        "Iphone":{
            "price":8800,
            "remaining_no":10
        }
    },

    2:{
        "Tesla":{
            "price":1000000,
            "remaining_no":5
        }
    },

    3:{
        "Rolex":{
            "price":600000,
            "remaining_no":30
        }
    },

    4:{
        "uniqlo":{
            "price":120,
            "remaining_no":200
        }
    },

    5:{
        "Kangshifu":{
            "price":8.5,
            "remaining_no":832,
        }
    },
}

db_path = settings.BASE_DIR

shopping_dbPath = "%s/db/goods" % db_path
# print(shopping_dbPath)


shopping_goods_file = "%s/%s.json" % (shopping_dbPath, 'goods')

with open(shopping_goods_file, 'w') as f:  # 打开account_file,通过json.dump（)将用户注册信息的字典文件写入
    acc_data = json.dump(goods_dic, f)



# print(goods_dic)


# for k,v in goods_dic.items():
#     for x,y in v.items():
#         print(k,x,y['price'],y['remaining_no'])





# import os
#
# db_path = 'db/accounts'
# cur_id = '22'
# user_names = []
# for root,dirs,files in os.walk(db_path):
#     for line in files:
#         user_names.append(line.split('.')[0])
#
# print(user_names)
# for line in user_names:
#     if cur_id == line:
#         print('存在该用户')
#     else:
#         print('不存在')

        # if cur_id not in line.split('.')[0]:
        #     pass
        # else:
        #     print('用户已存在，')