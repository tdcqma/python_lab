from interface import user,bank
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


menu_dic = {
    '1':[register,'register'],
    '2':[login,'login'],
    '3':[check_balance,'balance'],
    '4':[transfer,'transfer'],
    '5':[withdraw,'withdraw'],
    '6':[check_records,'check records'],
    '7':[repay,'repay']
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