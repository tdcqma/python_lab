#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from db import models
from lib import common
from tcpserver  import user_data

def login():
    pass

def register(message_dic,conn):
    '''
    注册功能
    :param user_dic:
    :param conn:
    :return:
    '''
    # 判断要注册的用户在当前数据库里是否有存在，如果存在提示用户已存在,
    name = message_dic['name']
    user = models.User.select_one(name=name)
    if user:
        back_dic = {'flag': False, 'msg': '用户已存在.'}
        common.send_back(back_dic, conn)
    else:
        # 如果用户不存在则进行注册
        password = message_dic['password']
        user_type = message_dic['user_type']

        # 调用数据库进行数据存储
        user = models.User(name=name, password=password, is_vip=0, locked=0, user_type=user_type)
        user.save()
        back_dic = {'flag': True, 'msg': '注册成功'}
        common.send_back(back_dic, conn)

def login(message_dic,conn):
    user = models.User.select_one(name=message_dic['name'])
    if user:
        if user.password == message_dic['password']:
            back_dic = {'flag': True, 'msg': '登录成功。'}

            # 身份验证信息成功，进行session生成，随机字符串
            session= common.get_uuid(message_dic['name'])
            back_dic['session'] = session

            #服务端存储众多客户端用户的形式例如以下所示：
            #alive_user = {addr: [session], addr: [session], addr: [session]}
            # 服务器端创建会话的过程需要加上锁

            user_data.mutex.acquire()
            user_data.alive_user[message_dic['addr']] = [session,user.id]
            user_data.mutex.release()




            common.send_back(back_dic, conn)
        else:
            back_dic = {'flag': False, 'msg': '密码错误！'}
            common.send_back(back_dic, conn)
    else:
        back_dic = {'flag': False, 'msg': '用户不存在'}
        common.send_back(back_dic, conn)

@common.login_auth
def check_movie_list(message_dic,conn):
    movie_list = models.Movie.select_all()
    if movie_list:
        back_movie = []
        for movie in movie_list:
            if not movie.is_delete:
                # 所有电影
                if message_dic['movie_type'] == 'all':
                    back_movie.append([movie.name,'免费' if movie.is_free else '收费',movie.id])
                elif message_dic['movie_type'] == 'free':
                    # 免费电影
                    if movie.is_free:
                        back_movie.append([movie.name,'免费',movie.id])
                else:
                    # 收费电影
                    if not movie.is_free:
                        back_movie.append([movie.name,'收费',movie.id])
        if back_movie:
            back_dic = {'flag':True,'msg':'查询成功','back_movie_list':back_movie}
        else:
            back_dic = {'flag': False, 'msg': '暂无电影'}
    else:
        back_dic = {'flag':False,'msg':'暂无电影'}

    common.send_back(back_dic,conn)

@common.login_auth
def delete_movie(message_dic,conn):
    movie = models.Movie.select_one(id = message_dic['movie_id'])
    movie.is_delete = 1
    movie.update()
    back_dic = {'flag':True,'msg':'删除成功。'}
    common.send_back(back_dic,conn)
