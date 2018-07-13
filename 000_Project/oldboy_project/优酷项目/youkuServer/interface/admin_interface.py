#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from db import models
from lib import common
import os
from conf import setting

@common.login_auth
def release_notice(user_dic,conn):
    notice = models.Notice(name=user_dic['notice_name'],content=user_dic['content'],user_id=user_dic['user_id'],create_time = common.get_nowtime())
    notice.save()

    back_dic = {'flag':True,'msg':'公告发布成功。'}
    common.send_back(back_dic,conn)

@common.login_auth
def upload_movie(user_dic,conn):
    recv_size = 0
    file_name = common.get_uuid(user_dic['file_name'])+user_dic['file_name']
    print('filename-->:',file_name)
    file_path = os.path.join(setting.BASE_MOVIE_DIR,file_name)
    print('file_path-->:',file_path)
    print('is_free-->:',user_dic['is_free'])
    print('create_time-->:',common.get_nowtime())
    print('user_id--->',user_dic['user_id'])
    print('file_md5-->',user_dic['file_md5'])

    with open(file_path, 'wb') as f:
        while recv_size < user_dic['filesize']:
            recv_date = conn.recv(1024)
            f.write(recv_date)
            recv_size += len(recv_date)
    print('%s:上传成功！' % file_name)

    movie = models.Movie(name=file_name,
                         path = file_path,
                         is_free = user_dic['is_free'],
                         is_delete = 0,
                         create_time=common.get_nowtime(),
                         user_id = user_dic['user_id'],
                         file_md5 = user_dic['file_md5']
                         )

    # movie = models.Movie(name=file_name,
    #                      path = file_path,
    #                      is_free = user_dic['is_free'],
    #                      user_id=user_dic['user_id'],
    #                      file_md5 = user_dic['file_md5']
    #                      )

    movie.save()
    print('%s:数据库保存成功！' % file_name)

    back_dic = {'flag':True,'msg':'上传成功！'}
    common.send_back(back_dic,conn)