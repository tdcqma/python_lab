from interface import user,bank,shop
from lib import common

# 跟踪用户状态
user_dic = {
    'username':None
}

def register():

    if user_dic['username']:
        print('You are logged in and cannot be register.')
        return

    while True:
        username = input('Please input username: ').strip()
        password = input('Please input password: ').strip()
        conf_password = input('please input password again: ').strip()

        if password == conf_password:
            flag,msg = user.register_interface(username,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('# Two password is not consistent.please retype.\n')


def login():
    '''
    login function
    :return:
    '''
    if user_dic['username']:
        print('you are already login.')
        return
    while True:
        username = input('Please input username: ').strip()
        password = input('Please input password: ').strip()

        flag,msg = user.login_interface(username,password)

        if flag:
            user_dic['username'] = username
            print(msg)
            break
        else:
            print(msg)

@common.login_auth
def check_balance():
    '''
    query balance function
    :return:
    '''
    balance = bank.check_balance_interface(user_dic['username'])
    print('the current balance is %s yuan.' % balance)

@common.login_auth
def transfer():
    '''
    transfer
    :return:
    '''
    while True:
        to_user = input('Please input transfer user: ').strip()
        amount = input('Please input transfer amount：').strip()

        if amount.isdigit():
            amount = int(amount)
            flag,msg = bank.transfer_interface(user_dic['username'],to_user,amount)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('Please enter the correct amount.')

@common.login_auth
def withdraw():
    while True:
        amount = input('Please input withdraw amount: ').strip()
        if amount.isdigit():
            amount = int(amount)
            flag,msg = bank.withdraw_interface(user_dic['username'],amount)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('Please enter the correct amount again.')
@common.login_auth
def check_records():
    records = bank.check_records_interface(user_dic['username'])
    if records:
        for record in records:
            print(record)
    else:
        print('there is no bankflow list')

@common.login_auth
def repay():
    while True:
        amount = input('please input repay amount: ').strip()
        if amount.isdigit():
            amount = int(amount)
            flag,msg = bank.repay_interface(user_dic['username'],amount)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('please input a correct amount')

@common.login_auth
def shopping():
    print('shopping...')
    '''
    购物车
    :return:
    '''
    goods_list = [
        ['coffee',10],
        ['chicken',20],
        ['car',100000],
    ]

    user_balance = bank.check_balance_interface(user_dic['username'])
    cost = 0
    shoppingcart = {}
    # {name:{'price':10,count:1}}

    while True:
        for i,goods in enumerate(goods_list,start=1): # enumerate用于将列表下标也打印出，设置从1开始
            print('%s:%s' % (i,goods))
        choice_buy = input('please input goods No that you want to buy (press \'q\' to exit.): ').strip()
        if choice_buy.isdigit():
            choice_buy = int(choice_buy)

            if choice_buy <len(goods_list):
                goods_name = goods_list[choice_buy-1][0]
                goods_price = goods_list[choice_buy-1][1]

                if user_balance >= goods_price:
                    if goods_name not in shoppingcart:
                        shoppingcart[goods_name] = {'price':goods_price,'count':1}
                    else:
                        shoppingcart[goods_name]['count'] += 1

                    user_balance -= goods_price
                    cost += goods_price
                    print('add goods to shopping_cart successfully.')
                else:
                    print('the balance is not enough to buy this goods.')
            else:
                print('please choice goods that in the shop.')
        elif choice_buy == 'q':
            if shoppingcart:
                flag,msg = shop.shopping_interface(user_dic['username'],cost,shoppingcart)
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
                    break
        else:
            print('please input a correct goods No.')

@common.login_auth
def check_shoppingcart():
    '''
    查看购物车
    :return:
    '''

    shoppingcart = shop.check_shoppingcart_interface(user_dic['username'])
    print(shoppingcart)


menu_dic = {
    '1':[register,'register'],
    '2':[login,'login'],
    '3':[check_balance,'balance'],
    '4':[transfer,'transfer'],
    '5':[withdraw,'withdraw'],
    '6':[check_records,'check records'],
    '7':[repay,'repay'],
    '8':[shopping,'shopping'],
    '9':[check_shoppingcart,'check shoppingcart']
}

def run():
    while True:
        for k,v in menu_dic.items():    # 打印菜单选项
            print(k,v[1])

        choice = input('please input: ').strip()

        if choice == 'q':
            print(' Bye.')
            break

        for k,v in menu_dic.items():
            if choice == k:
                menu_dic[choice][0]()