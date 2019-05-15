'''
一、什么是hash

    hash本质是一种算法，该算法是用来校验文本内容。

    比喻的说法：
        可以把hash当成一个工厂
        我们给工厂提供原材料（python中的字符串）
        hash工厂为我们返回校验之后的一串字符

二、hash算法的用途，即三大特点
    1、 不管校验多少个文本内容，只要校验的文本内容一样(所有的字符均需要一样，哪怕多一个空格都不行)，
        那么得到的hash值就是相同的。通过这个特性可以校验文件的完整性。
        要理解校验文件完整性可以想象一个场景，我在某官网要下载一个软件，官网实现计算出
        这个软件的HASH值并公布出来，客户端在下载这个软件后对这个软件进行校验，得到的hash值
        如果与官网公布出来的hash值一致，那么就代表这个软件没有被改动过。

    2、 只要使用的hash算法固定，无论校验的内容有多大，得到的hash值长度都是固定的
        这个特性的用途：比如要下载一个文件，如果文件大小1M是hash值长度是1个字节大小，
        如果文件的大小是10个T的时候hash值可能会是几个G大小，而hash值是伴随报文一同传输的，
        本来报文没占多大传输资源而hash值却占用了大量的传输资源，严重影响了传输效率了。
        因此，无论校验的内容有多大，只要加密算法一样，最终得到的hash值的长度都是固定的。

        上述的1、2两个特性合在一起就起到了校验校验文件的完整性。

    3、 将明文转成密文进行传输，用在把明文密码变成密文。hash不可逆，说是无法反解，但其实已经被山东大学教授破解了算法。

'''

# 三、如何用hash模块

import hashlib

# 3.1 通过hashlib查看支持哪些算法，以下只是部分列举
hashlib.md5
hashlib.sha1
hashlib.sha256
hashlib.sha512
hashlib.sha3_256
hashlib.sha3_384

# 3.2 验证文件的内容一样，得到的hash值就一样
m = hashlib.md5()   # m是拿到了一个md5对象
m.update('hello'.encode('utf-8'))  # 传入的类型必须都是二进制bytes类型,等价于m.update(b'hello')
m.update(b'world')
m.update(b'python')
# 到目前为止总共传参3次，组合后值为"helloworldpython"
# print(m.hexdigest())    # 35cb3f29dee71040a0dc91b4af9d475e

m1 = hashlib.md5()
m1.update(b'hellowor')
m1.update(b'ldpython')
# 到目前为止总共传参2次，组合后值为"helloworldpython"
# print(m1.hexdigest())   # 35cb3f29dee71040a0dc91b4af9d475e

# 6CBA798D3C0EDD721C6C9A523DAC5192
# 3.3 校验视频等文件完整性，获取视频文件的hash值。以下两种方式逐行读取计算hash与一次性读取得到的hash值相同。
m2 = hashlib.md5() # test
with open('test_video.mp4',mode='rb') as f:
    # for line in f:    # => 45dedcf3a27fb861bfdbf0bb48cab7fd
    #     m2.update(line)

    m2.update(f.read())  # => 45dedcf3a27fb861bfdbf0bb48cab7fd
    print('test_video.mp4\'s hash value: ',m2.hexdigest())

# 3.4 hashlib.md5()括号内加的值也会与update()括号里的值叠加后进行hash运算，如下所示，m3与m4两次运算得到的结果相同
m3 = hashlib.md5(b'hello')
m3.update(b'world')
# print(m3.hexdigest())    # =>fc5e038d38a57032085441e7fe7010b0

m4 = hashlib.md5()
m4.update(b'helloworld')
# print(m4.hexdigest())   # =>fc5e038d38a57032085441e7fe7010b0

# 3.5 将字符串格式的密码进行md5加密
password = 'python123'
m5 = hashlib.md5()
m5.update(password.encode('utf-8')) # 需要将字符串格式的password转换为二进制
pwd_md5 = m5.hexdigest()
# print('pwd_md5:',pwd_md5)

# 3.6 密码加盐
# password = input('please input password: ').strip()
m6 = hashlib.md5()
m6.update('天王盖地虎'.encode('utf-8')) # 加盐部分
m6.update(password.encode('utf-8')) # 密码加密部分
m6.update('宝塔镇河妖'.encode('utf-8')) # 加盐部分

pwd_md5 = m6.hexdigest()
# print('your pwd_md5(add salt): ',pwd_md5)

# 3.7 hash的其他算法尝试，区别无非是复杂度不同
m8 = hashlib.md5()
m8.update('hello'.encode('utf-8'))
# print('hello\'s md5:',m8.hexdigest())

m7 = hashlib.sha256()
m7.update('hello'.encode('utf-8'))
# print('hello\'s sha256:',m7.hexdigest())

m9 = hashlib.sha512()
m9.update('hello'.encode('utf-8'))
# print('hello\'s sha512:',m9.hexdigest())

'''
result:
hello's md5: 5d41402abc4b2a76b9719d911017c592
hello's sha256: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
hello's sha512: 9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043
'''

# 3.8 hmac 加密，与hash的区别是hmac强制你要为加密内容加盐
import hmac
m10 = hmac.new('天王盖地虎'.encode('utf-8'))
m10.update('hello'.encode('utf-8'))
m10.update('world'.encode('utf-8'))
content_hmac = m10.hexdigest()
print('content_hmac:',content_hmac)
