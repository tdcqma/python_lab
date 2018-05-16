
from interface import bank,shop,user
from lib import common
user_dic={
    'name':None
}

def register():
    if user_dic['name']:
        print('已经登录,不能注册')
        return
    print('注册')
    while True:
        name = input('请输入名字:').strip()
        password = input('请输入密码:').strip()
        conf_password= input('请确认密码:').strip()
        if password == conf_password:
            flag,msg=user.register_interface(name,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')

def login():
     if user_dic['name']:
         print('已经登录')
         return
     print('登录')
     while True:
         name=input('请输入用户名').strip()
         password =input('请输入密码').strip()
         flag,msg=user.login_inteface(name,password)
         if flag:
             user_dic['name']=name

             print(msg)
             break
         else:
             print(msg)

@common.login_auth
def check_balance():
    print('查看余额')
    balance= bank.check_balance_interface(user_dic['name'])
    print(balance)
@common.login_auth
def transfer():

    print('转账')
    while True:
        to_user= input('请输入对方账户：').strip()
        account= input('请输入转账金额:').strip()
        if account.isdigit():
            account =int(account)
            flag,msg=bank.transfer_interface(user_dic['name'],to_user,account)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('请输入数字')

@common.login_auth
def repay():
    print('还款')
    while True:
        account=input('请输入还款金额').strip()
        if account.isdigit():
            account=int(account)
            flag,msg=bank.repay_interface(user_dic['name'],account)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('请输入数字')
@common.login_auth
def withdraw():
    print('取款')
    while True:
        account= input('请输入取款金额').strip()
        if account.isdigit():
            account=int(account)
            flag,msg=bank.withdraw_interface(user_dic['name'],account)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('请输数字')

@common.login_auth
def check_records():
    print('查看流水')
    records=bank.check_records_interface(user_dic['name'])
    if records:

        for record in records:
            print(record)
    else:
        print('暂无流水')


@common.login_auth
def shopping():
    print('购物车')
    goods_list=[
        ['coffee',10],
        ['chicken',20],
        ['car',100000]
    ]
    user_balance=bank.check_balance_interface(user_dic['name'])
    cost=0
    shoppingcart={}
    # {name:{'price':10,count:1}}
    while True:
        for i,goods in enumerate(goods_list):
            print('%s : %s'%(i,goods))
        buy = input('请输入要购买的商品（数字）(q 退出并购买):')
        if buy.isdigit():
            buy =int(buy)
            if buy<len(goods_list):
                goods_name=goods_list[buy][0]
                goods_price=goods_list[buy][1]
                if user_balance>=goods_price:
                    if goods_name not in shoppingcart:
                        shoppingcart[goods_name]={'price':goods_price,'count':1}
                    else:
                        shoppingcart[goods_name]['count']+=1

                    user_balance-=goods_price
                    cost+=goods_price
                    print('添加到购物车成功')
                else:
                    print('余额不足')
            else:
                print('请选择存在的商品')
        elif buy == 'q':
            if shoppingcart:
                flag,msg=shop.shoping_interface(user_dic['name'],cost,shoppingcart )
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
                    break

        else:
            print('请输入数字')

@common.login_auth
def check_shoppingcard():
    print('查看购物车')
    shoppingcart=shop.check_shopingcart_interface(user_dic['name'])
    print(shoppingcart)


func_dic={
    '1':register,
    '2':login,
    '3':check_balance,
    '4':transfer,
    '5':withdraw,
    '6':repay,
    '7':check_records,
    '8':shopping,
    '9':check_shoppingcard
}

def run():

    while True:
        print('''
        　  1 注册
            2 登录
            3 查看余额
            4 转账
            5 取款
            6 还款
            7 查看流水
            8 购物
            9 查看购买商品
        ''')

        choice = input('请选择')
        if choice not in func_dic:continue
        func_dic[choice]()