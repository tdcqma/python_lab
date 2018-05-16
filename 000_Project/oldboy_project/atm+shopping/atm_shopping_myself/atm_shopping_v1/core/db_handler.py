#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

# 文件认证方式处理
def file_db_handle(conn_params):
    '''
    获取用户DB文件的路径，被db_handler(conn_parms)调用
    :param conn_params:保存的是数据库连接信息，DATABASE = {
                                            'engine':'file_storage'
                                            'name':'accounts',
                                            'path':"%s/db" % BASE_DIR
                                        }
    :return:
    '''

    # 得到用户数据文件所保存的目录名称，这里指向ATM/db/accounts
    print('file db:',conn_params)
    db_path = "%s/%s" % (conn_params['path'],conn_params['name'])
    return db_path

# 数据库认证方式处理
def mysql_db_handle(conn_params):
    pass

# 判断用户所选择的认证方式，是文件认证或是数据库认证
def db_handler(conn_parms):

    if conn_parms['engine'] == 'file_storage':  # 如果用户采用file_storage方式认证，则返回file_db_handle(conn_parms)
        return file_db_handle(conn_parms)

    if conn_parms['engine'] == 'mysql': # 如果用户采用mysql认证则返回mysql_db_handle()
        return mysql_db_handle()