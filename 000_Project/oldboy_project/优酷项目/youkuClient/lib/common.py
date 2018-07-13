#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import json
import struct
import hashlib
import os
from conf import setting


def send_data(client,send_dic,file=None):

    # 将要cong 客户端发送的字典转换为json格式，再转换为字典格式。
    send_json = json.dumps(send_dic)
    send_bytes = send_json.encode('utf-8')

    # 客户端发送数据到服务端
    client.send(struct.pack('i',len(send_bytes)))
    client.send(send_bytes)

    if file:    # 如果文件存在，把文件打开一行一行的发送
        with open(file,'rb') as f:
            for line in f:
                client.send(line)

    # 从服务端接收数据，并将bytes格式转换为json，再转换为字典格式
    # 最后返回字典
    head = client.recv(4)
    head_len = struct.unpack('i',head)[0]
    back_bytes = client.recv(head_len)
    back_dict = json.loads(back_bytes.decode('utf-8'))
    return back_dict

def make_md5(password):
    '''
    transfer password to md5.
    :param password:
    :return:
    '''

    md = hashlib.md5()
    md.update(password.encode('utf-8'))
    return md.hexdigest()


def get_upload_movie_list():
    movie_list = os.listdir(setting.BASE_UPLOAD_MOVIE)
    return movie_list

def get_file_md5(file_path):
    if os.path.exists(file_path):
        md = hashlib.md5()

        file_size = os.path.getsize(file_path)
        file_list = [0,file_size // 3,(file_size // 3) * 2, file_size -10]

        with open(file_path,'rb') as f:
            for li in file_list:
                f.seek(li)
                md.update(f.read(10))
            return md.hexdigest()


# if __name__ == '__main__':
#     x = get_file_md5(r'/Users/mahaibin/PycharmProjects/youkuClient/upload_movie/testVideo.mp4')
#     print(x)
