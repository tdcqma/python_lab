#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from lib import common
from tcpclient import tcpClient
from conf import setting
import os


user_data = {
    'session':None
}

def admin_register(client):
    print('管理员注册')
    while True:
        name = input('请输入手机号：').strip()
        if name == 'q':break
        password = input('请输入密码：').strip()
        conf_password = input('请确认密码：').strip()
        if password == conf_password:

            # 将用户注册信息装到字典里，用于转换成json->bytes,然后发送到服务端
            send_dic = {'type':'register','user_type':'admin','name':name,'password':common.make_md5(password)}

            # 调用common里的发送数据模块send_data，back_dic为接收服务端返回的数据
            back_dic = common.send_data(client,send_dic,None)

            # 判断服务端返回的字典中flag是true还是false，True为执行成功打印true对应的message
            # flag为false则打印false对应的message
            if back_dic['flag']:
                print(back_dic['msg'])
                break
            else:
                print(back_dic['msg'])
        else:
            print('两次密码不一致')

def admin_login(client):

    while True:
        name = input('请输入用户名：').strip()
        password = input('请输入密码: ').strip()

        # 登录时也需要将密码进行md5加密后传输
        send_dic = {'type':'login','name':name,'password':common.make_md5(password)}
        back_dic = common.send_data(client,send_dic,None)
        if back_dic['flag']:
            # 如果用户登录成功，将服务端发来的session保存至本地的user_data['session']里。
            user_data['session'] = back_dic['session']
            print(back_dic['msg'])
            break
        else:
            print(back_dic['msg'])

def upload_movie(client):
    # 先要把本地的某个文件夹里的视频先打印出来
    # 选择要上传的视频的序号
    movie_list = common.get_upload_movie_list()

    if not movie_list:
        print('暂无可上传影片')
        return

    for i,movie in enumerate(movie_list):
        print('%s : %s' % (i,movie))

    choice = input('请输入要上传的影片：').strip()

    if choice.isdigit():
        choice = int(choice)
        # 收费、免费
        is_free = input('是否免费（y/n)').strip()

        if is_free == 'y':
            movie_is_free = 1
        else:
            movie_is_free = 0

        # 文件大小
        file_path = os.path.join(setting.BASE_UPLOAD_MOVIE,movie_list[choice])
        filesize = os.path.getsize(file_path)

        send_dic = {'type':'upload_movie',
                    'session':user_data['session'],
                    'is_free':movie_is_free,
                    'file_md5':common.get_file_md5(file_path),
                    'file_name':movie_list[choice],
                    'filesize':filesize
                    }

        back_dic = common.send_data(client,send_dic,file_path)
        if back_dic['flag']:
            print(back_dic['msg'])
        else:
            print(back_dic['msg'])
    else:
        print('请输入数字！')


def delete_movie(client):
    if not user_data['session']:
        print('请先登录')
        return

    while True:
        send_dic = {'type':'check_movie_list','session':user_data['session'],'movie_type':'all'}
        back_dic = common.send_data(client,send_dic,None)

        if not back_dic['flag']:
            print(back_dic['msg'])
            break

        movie_list = back_dic['back_movie_list']
        if not movie_list:
            print('暂无电影')
            break

        for i,movie in enumerate(movie_list):
            print('%s : 电影名:%s 是否免费:%s' % (i,movie[0],movie[1]))
        choice  = input('请选择要删除的电影数字：').strip()

        if choice.isdigit():
            choice = int(choice)
            movie_id = movie_list[choice][2]
            send_dic = {'type':'delete_movie','session':user_data['session'],'movie_id':movie_id}
            back_dic = common.send_data(client,send_dic,None)

            if back_dic['flag']:
                print(back_dic['msg'])
                break
            else:
                print(back_dic['msg'])
        else:
            print('必须输入数字。')

send_dic = {'type': None, 'user_type': 'admin', 'session': None}
def release_notice(client):

    if not user_data['session']:
        print('请先登录。')
        return
    print('发布公告')

    while True:
        notice_name = input('请输入公告标题：').strip()
        notice_content = input('请输入公告内容: ').strip()

        if notice_name == 'q':break
        send_dic['type'] = 'release_notice'
        send_dic['session'] = user_data['session']
        send_dic['notice_name'] = notice_name
        send_dic['content'] = notice_content
        back_dic = common.send_data(client, send_dic, None)

        if back_dic:
            print(back_dic['msg'])
            break
        else:
            print(back_dic['msg'])

func_dic = {
    '1':admin_register,
    '2':admin_login,
    '3':upload_movie,
    '4':delete_movie,
    '5':release_notice,
}

def admin_view():
    client = tcpClient.get_client()
    while True:
        print(
            '''
            1 注册
            2 登录
            3 上传视频
            4 删除视频
            5 发布公告
            '''
        )

        choose = input('please choose>>:').strip()
        if 'q' == choose:break
        if choose not in func_dic:continue
        func_dic[choose](client)

    client.close()