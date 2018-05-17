import hashlib
password1 = input('please input your password:')

m5 = hashlib.md5()
m5.update(password1.encode('utf-8')) # 需要将字符串格式的password转换为二进制
pwd_md5 = m5.hexdigest()
print('your pwd_md5:',pwd_md5)

password2 = input('please input password: ').strip()
m6 = hashlib.md5()
m6.update('天王盖地虎'.encode('utf-8')) # 加盐部分
m6.update(password2.encode('utf-8')) # 密码加密部分
m6.update('宝塔镇河妖'.encode('utf-8')) # 加盐部分

pwd_md5 = m6.hexdigest()
print('your pwd_md5(add salt): ',pwd_md5)

'''
result：

please input your password:111
your pwd_md5: 698d51a19d8a121ce581499d7b701668

please input password: 111
your pwd_md5(add salt):  e9c93ab58426c59d88fb49a98d58cfd7
'''