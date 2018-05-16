#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma
import json
from core import auth
from core import logger
from core import accounts
from core import transaction
from core import payCheckShow
from core import goods
from conf import settings
from core import auth

# transaction logger
trans_logger = logger.logger('transaction')

# access_logger
access_logger = logger.logger('access')

user_data = {
    'account_id':None,  #account_id保存username
    'is_authenticated':False,   #is_authenticated保存登录状态
    'account_data':None #account_data保存所有用户的数据信息，也就是ATM/db/accounts/用户名.json里的信息
}

def auth():
    def auth2(func):
        def wrapper(*args,**kwargs):
            if not user_data['is_authenticated']:
                username = input('uname:').strip()
                password = input('upass:').strip()
                account_file_path = '%s/db/accounts/%s.json' % (settings.BASE_DIR,username)
                # print(account_file_path)

                with open(account_file_path,'r') as f:
                    userinfo = json.load(f)

                if username == userinfo['id'] and password == userinfo['password'] and userinfo['status'] == 0:
                    user_data['account_id'] = userinfo['id']
                    user_data['account_id'] = True
                    user_data['account_data'] = userinfo
                    res = func(*args, **kwargs)
                    return res
            else:
                print('hello world')
                res = func(*args, **kwargs)
                return res
        return wrapper
    return auth2

def account_info(acc_data):
    '''
    显示用户信息
    :param acc_data:
    :return:
    '''
    print('用户信息'.center(30,'-'))
    for k,v in user_data.items():
        if k == 'account_data':
            for x,y in v.items():
                if x not in ('password','admin'):   # 过滤掉密码与管理员状态
                    print('%12s : %s' %(x,y))
def register(acc_data):
    '''
    用户注册
    :return:
    '''

    register_msg = '''----------- 用户注册 -----------
    '''
    print(register_msg)
    user_id = input('Please input card id：').strip()
    user_passwd = input('Please input password:').strip()
    user_credit = float(input('Please input credit amount:').strip())
    balance = user_credit
    user_enroll_date = ''
    user_expire_date = input('Please input card\'s expire date: ').strip()
    user_pay_day = 22

    acc_dic = {
        "id":user_id,
        "password":user_passwd,
        "credit":user_credit,
        "balance":balance,
        "enroll_date":user_enroll_date,
        "expire_date":user_expire_date,
        "pay_day":user_pay_day,
        "status":0,  # 0 = normal, 1=locked, 2=disabled
        "admin":0,
    }

    # 确认用户输入的注册信息没有问题后调用accounts.user_register()进行用户注册
    user_reg = accounts.user_register(acc_dic)

    if user_reg:
        print('用户[%s]注册成功。' % acc_dic['id'])
    else:
        print('该用户已被注册，请重新确认。')

def lock_user(acc_data):
    '''
    冻结用户操作
    :param acc_data:
    :return:
    '''
    # print('冻结用户操作',acc_data)
    if acc_data['account_data']['admin'] == 1:

        # 获取所有用户ID让管理员选择需要冻结的用户
        users = accounts.get_allUser(acc_data)
        print('---------- 当前用户一览 ---------- ')
        for user in users:
            print(' 用户:',user)

        select_lockUser_id = input('请选择您要锁定的用户ID: ').strip()

        # 判断用户输入的待锁定用户ID是否存在

        if select_lockUser_id in users:
            # 调用accounts.lock_user()函数，读取该用户的数据文件，将status状态改为-1，即锁定用户的状态
            lock_res = accounts.lock_user(acc_data,select_lockUser_id)

            if lock_res:
                print('用户[%s]锁定成功！该用户已无法登录。' % select_lockUser_id)
            else:
                print('用户[%s]锁定失败。' % select_lockUser_id)
        else:
            print('您输入的用户不存在，请重新确认。\n')

    else:
        print('用户[%s]非管理员用户，无法冻结其他用户。\n' % acc_data['account_data']['id'])

@auth()
def repay(acc_data):
    '''
    还款操作
    :param acc_data:
    :return:
    '''

    # account_data获取当前用户的所有信息，即db/accounts/用户名.json里的全部数据
    account_data = accounts.load_current_balance(acc_data['account_id'])

    current_balance = '''---------- BALANCE INFO ----------
    Credit:     %s
    Balance:    %s''' % (account_data['credit'],account_data['balance'])

    print(current_balance)  # 显示用户总金额与可用金额
    back_flag = False

    while not back_flag:
        repay_ammount = input('Input repay amount: ').strip()

        # 如果用户输入的金额有效的话，调用transaction.make_transaction进行金额调整，make_transaction()需要传入相应的参数
        if len(repay_ammount) > 0 and repay_ammount.isdigit():

            # transaction.make_transaction函数是转账交易的核心部分，如果成功返回了值将付给new_balance
            # new_balance得到的就是对金额处理后的用户最新数据信息
            new_balance = transaction.make_transaction(trans_logger,account_data,'repay',repay_ammount)
            if new_balance:     #还款成功的话打印最新的余额信息
                print('New balance:%s' % (new_balance['balance']))
        else:
            print('[%s] is not a valid amount,only accept integer!' % repay_ammount)

        if repay_ammount == 'b':    # 输入'b'返回menu主页面
            back_flag = True

@auth()
def withdraw(acc_data):
    '''
    提现操作
    :param acc_data:
    :return:
    '''

    # 获取用户的所有信息，即ATM/db/accounts/用户名.json的文件
    account_data = accounts.load_current_balance(acc_data['account_id'])

    # 打印显示信息
    current_balance = '''---------- BALANCE INFO ----------
    Credit:     %s
    Balance:    %s''' % (account_data['credit'],account_data['balance'])

    print(current_balance)
    back_flag = False

    while not back_flag:
        withdraw_amount = input('Input withdraw amount: ').strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():

            new_balance = transaction.make_transaction(trans_logger,account_data,'withdraw',withdraw_amount)
            if new_balance:
                print('New Balance: %s' % (new_balance['balance']))
        else:
            print('[%s] is not a valid amount,only accept integer!' % withdraw_amount)

        if withdraw_amount == 'b':
            back_flag = True

@auth()
def transfer(acc_data):
    '''
    转账操作
    :param acc_data:
    :return:
    '''

    # cur_account_data保存了转出用户(当前用户)的所有信息，即db/accounts/转出用户.json里的全部信息
    cur_account_data = accounts.load_current_balance(acc_data['account_id'])
    # print('~~cur_account_data~~',cur_account_data)

    # 打印显示信息
    current_balance = '''---------- BALANCE INFO ----------
        Credit:     %s
        Balance:    %s''' % (cur_account_data['credit'], cur_account_data['balance'])
    print(current_balance)

    # 获取收款用户的数据库信息，rec_account_data保存了转入用户(收款方)的所有信息，
    # 即ATM/db/account/收款用户.json里的信息
    rec_account_data = ''
    # print('~~rec_account_data~~',rec_account_data)

    back_flag = False
    transfer_flag = False
    while not back_flag:
        # 收款用户ID,与转账金额
        rec_userId = input('Please input account id for receiving.').strip()

        if rec_userId == 'b':
            back_flag = True
            break

        # 判断用户输入的收款方ID是否存在
        user_isexist = accounts.transfer_existUser(rec_userId)

        # 当收款方用户存在时继续输入转入金额等操作，否则提示用户不存在
        if user_isexist:
            transfer_amount = input('Please input transfer amount: ').strip()
            rec_account_data = accounts.load_current_balance(int(rec_userId))    #收款用户的数据库信息

            # 转出方扣款，即执行withdraw操作
            if len(transfer_amount) > 0 and transfer_amount.isdigit():
                cur_new_balance = transaction.make_transaction(trans_logger,cur_account_data,'withdraw',transfer_amount)
                if cur_new_balance:
                    transfer_flag = True
                    print('转出成功，New Balance:[%s]' % (cur_new_balance['balance']))
            else:
                print('[%s] is not a valid amount,only accept integer!' % transfer_amount)

            # 如果转出成功了，那么继续向转入方加款，即执行repay操作
            if transfer_flag:
                if len(transfer_amount) > 0 and transfer_amount.isdigit():
                    rec_new_balance = transaction.make_transaction(trans_logger,rec_account_data,'repay',transfer_amount)
                    if rec_new_balance:
                        print('转入成功,New Balance:[%s]' % (rec_new_balance['balance']))
                else:
                    print('[%s] is not a valid amount,only accept integer' % transfer_amount)
            else:
                print('金额不足，无法转账。')
        else:
            print('用户不存在，无法进行转账！')
            break

def consume(acc_data,shoppingCar_data):
    '''
    购物交易
    :param acc_data:
    :return:
    '''

    # 获取用户的所有信息，即ATM/db/accounts/用户名.json的文件
    account_data = accounts.load_current_balance(acc_data,acc_data['account_id'])

    # 获取此次购物需要的费用与被购买的数量
    goods_amount = shoppingCar_data['goods_amount']
    goods_num = shoppingCar_data['goods_num']
    goods_no = shoppingCar_data['goods_no']

    # 用户金额扣除
    goods_status_flag = False
    new_balance = transaction.make_transaction(trans_logger,account_data,'consume',goods_amount)
    if new_balance:
        goods_status_flag = True
        # print('New Balance: %s' % (new_balance['balance']))

    # 如果扣款成功，则进行购物车内商品购买状态的调整，由0->1
    if goods_status_flag:
        shoppingCar_data['buy_status'] = 1

        goods_path = settings.BASE_DIR

        shopping_goods_file = "%s/db/shopping_car/%s.json" % (goods_path,acc_data['account_id'])
        with open(shopping_goods_file, 'w') as f:  # 打开account_file,通过json.dump（)将用户注册信息的字典文件写入
            acc_data = json.dump(shoppingCar_data, f)

    # 如果扣款成功，则进行被购买商品库存的相应数量缩减
    if goods_status_flag:
        goods_file_path = '%s/goods.json' % (settings.DB_GOODS_DIR)

        goods_data = ''
        with open(goods_file_path,'r') as f:
            goods_data = json.load(f)

        # print('lalalala',goods_num,goods_data)
        for line in goods_data.items():
            if line[0] == goods_no:
                print(line[0],line[1],type(line[1]))
                for i in line[1].items():
                    i[1]['remaining_no'] = i[1]['remaining_no'] - int(goods_num)    # 此处的运算后得到的i[1]['remaining_no'] 为用户购买商品数量后剩余的库存

        print('新库存：', goods_data)
        # 将新的商品信息更新到数据库中
        with open(goods_file_path,'w') as f:
            json.dump(goods_data,f)



    return True,new_balance

    # 购物车商品购买状态由0变更为1

@auth()
def pay_check(acc_data):
    '''
    账单确认
    :param acc_data:
    :return:
    '''

    # 获取当前用户的所有信息，***.json
    account_data = accounts.load_current_balance(acc_data['account_id'])

    # 调用payCheckShow.pay_check输出交易记录
    payCheckShow.pay_check(account_data['id'])

def show_goods(acc_data):
    '''

    :return:
    '''

    # 显示商品清单， goods_list 为字典格式，保存当前全部的商品清单
    goods_list = goods.show_goods_list()
    shopmsg = '''---------- GOODS LIST ----------'''
    print(shopmsg)
    for k,v in goods_list.items():
        for x,y in v.items():
            goods_msg = '编号：%s 名称:%s 单价:%s 剩余:%s' % (k,x,y['price'],y['remaining_no'])
            print(goods_msg)
    print(shopmsg)

    goods.add_to_shoppingCar(acc_data, goods_list)

    # # 获取用户想要购买商品的编号
    # select_goodID = input('please select goods\'s id:').strip()
    #
    # # print('您选择商品编号：',select_goodID)
    # # print('您的账户信息：',acc_data)
    #
    # goods_res = goods_list[select_goodID]   # => {'Iphone': {'price': 8800, 'remaining_no': 10}}
    #
    # # 判断依据：1. 用户剩余金额大于（购买数量X商品单价） 2. 商品仍有剩余
    # # k:商品名称
    # # v['price']:商品价格
    # # v['remaining_no']：商品剩余个数
    # goods_name= ''
    # goods_num = 0
    # goods_amount = 0
    # for k,v in goods_res.items():
    #     goods_name = k
    #     # goods_quantity接收用户输入的商品数量
    #     goods_quantity = int(input('please input quantity of %s: ' % (k)).strip())
    #     goods_num = goods_quantity
    #
    #     if v['remaining_no'] > goods_quantity : # 如果库存大于用户选择的商品数量
    #         goods_amount = goods_quantity * int(v['price'])
    #
    # # print('\n用户信息：',acc_data)
    #
    # # 获取当前用户的可用余额
    # cur_balance = acc_data['account_data']['balance']
    #
    # # 判断用户余额是否大于购买金额，如果大于允许加入购物车
    # if cur_balance >= goods_amount:
    #
    #     shop_car_info = ' 待加入购物车的信息：\n  商品名称:%s\n  购买数量:%s\n  商品总价：%s' % (goods_name, goods_num, goods_amount)
    #     print(shop_car_info)
    #     is_add_to_shopcar = input('Please confirem add to the shoppingCar?(y/n)').strip()
    #
    #     if is_add_to_shopcar == 'y':
    #         print('加入购物车操作中....')
    #
    #     # print('cur_balance',cur_balance)
    #     # print('goods_amount',goods_amount)
    # else:
    #     print('余额不足，无法购买！')

def shopping_car(acc_data):
    '''
    # 显示自己的购物车内容,支付购买
    :param acc_data: 用户所有的信息，即db/accounts/用户id.json
    :return:
    '''

    # 拿到自己购物车的信息goods_num
    shoppingCar_data = goods.load_myself_shoppingCar(acc_data)

    if shoppingCar_data:

        print('自己的购物车信息：',shoppingCar_data)
        # 打印显示信息
        pay_msg = '''---------- 购物车信息 ----------
            商品名称:   %s
            购买数量:   %s
            需付金额:   %s
            当前金额:   %s''' % (shoppingCar_data['goods_name'],shoppingCar_data['goods_num'],shoppingCar_data['goods_amount'],acc_data['account_data']['balance'])
        print(pay_msg)

        confirm_buy = input('\n确认付款请按\'y\',返回上一层请按\'b\':').strip()
        if shoppingCar_data['buy_status'] == 0:
            if confirm_buy == 'y':
                buy_res,new_balance = consume(acc_data, shoppingCar_data)   # 调用结算接口，返回结算结果与最新的剩余金额
                if buy_res:
                    print('商品[%s]购买成功！,剩余金额:%s' % (shoppingCar_data['goods_name'],new_balance['balance']))
                else:
                    print('购买失败！')
            elif confirm_buy == 'b':
                pass
            else:
                print('输入不合法')
        else:
            if confirm_buy == 'b':
                pass
            else:
                print('该商品已付款，请勿重复付款。\n')
    else:
        print('您还没有加入任何商品到购物车，您的购物车为空。^_^')

@auth()
def account_manage(acc_data):
    '''
    用户管理接口，实现对用户的管理，包括显示账户信息、用户注册、用户锁定、冻结账户
    :param acc_data:
    :return:
    '''
    account_manage_dic = {
        '1-1':[account_info, '账户信息'],
        '1-2':[register, '用户注册'],
        '1-3':[lock_user,'用户冻结'],
    }

    back_flag = False

    while not back_flag:
        # 显示管理用户的全部选项
        for i in account_manage_dic:
            print(i, account_manage_dic[i][1])

        user_option = input('请选择您的操作:').strip()

        if user_option in account_manage_dic:
            account_manage_dic[user_option][0](acc_data)
        elif user_option == 'b':
            back_flag = True
        else:
            print('[%s]操作不存在，请重新确认' % user_option)

@auth()
def shopping(acc_data):
    # 定义购物车操作，包括查看全部商品,查看购物车等
    shopping_dic = {
        '2-1': [show_goods, '查看商品列表'],
        '2-2': [shopping_car, '查看购物车'],
    }

    # # 显示购物全部选项
    # for i in shopping_dic:
    #     print(i,shopping_dic[i][1])

    back_flag = False
    while not back_flag:
        # 显示购物全部选项
        for i in shopping_dic:
            print(i, shopping_dic[i][1])

        user_option = input('>>Please select:').strip()
        if user_option in shopping_dic:
            shopping_dic[user_option][0](acc_data)
        elif user_option == 'b':
            back_flag = True
        else:
            print("\033[31;1mOption does not exist!\033[0m")

@auth()
def logout(acc_data):
    '''
    退出程序
    :param acc_data:
    :return:
    '''
    print('ByeBye.')
    return exit()


# 认证装饰器,如果用户已认证则略，
# 否则输入用户名密码进行认证。
'''
user_data = {
    'account_id':None,  #account_id保存username
    'is_authenticated':False,   #is_authenticated保存登录状态
    'account_data':None #account_data保存所有用户的数据信息，也就是ATM/db/accounts/用户名.json里的信息
}
'''


def interactive(acc_data):
    '''
    与用户交互的入口
    :param acc_data:
    :return:
    '''
    # menu显示方式一
    # menu = u'''
    # \033[32;1m1.  账户信息
    # 2.  还款
    # 3.  取款
    # 4.  转账
    # 5.  账单
    # 6.  退出
    # \033[0m'''
    #
    # menu_dic = {
    #     '1':account_info,
    #     '2':repay,
    #     '3':withdraw,
    #     '4':transfer,
    #     '5':pay_check,
    #     '6':logout
    # }
    #
    # exit_flag = False
    #
    # while not exit_flag:
    #     print(menu)
    #     user_option = input('>>:').strip()
    #     if user_option in menu_dic:
    #         menu_dic[user_option](acc_data)
    #     else:
    #         print("\033[31;1mOption does not exist!\033[0m")

    # menu显示方式二
    # menu_dic = {
    #     '1':[account_info,'账户信息'],
    #     '2':[register,'用户注册'],
    #     '3':[repay,'还款'],
    #     '4':[withdraw,'提现'],
    #     '5':[transfer,'转账'],
    #     '6':[pay_check,'账单'],
    #     '7':[shopping,'购物'],
    # }

    menu_dic = {
        '1':[account_manage,'用户管理'],
        '2':[shopping, '用户购物'],
        '3':[repay,'还款'],
        '4':[withdraw,'提现'],
        '5':[transfer,'转账'],
        '6':[pay_check,'账单'],
        '7':[logout,'退出']
    }

    while True:
        for i in menu_dic:  # 循环打印menu
            print(i,menu_dic[i][1])

        user_option = input('>>:').strip()

        if user_option == 'q':
            print('您已退出，欢迎再次使用。')
            break

        if user_option in menu_dic:
            menu_dic[user_option][0](acc_data)  # 如果用户输入合法，则调用用户输入内容所对应的函数
        else:
            print("\033[31;1mOption does not exist!\033[0m")

# interactive(user_data)

def run():
    '''
    程序主入口
    :return:
    '''

    # print('hello world')
    # auth()(shopping)()
    interactive(user_data)
