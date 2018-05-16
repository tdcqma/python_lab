#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DB = os.path.join(BASE_DIR,'db')
BASE_LOG = os.path.join(BASE_DIR,'log')

# 创建日志格式

standard_format = '[%(asctime)s][%(threadName)s][%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s] %(message)s'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志目录，如果不存在就创建一个
if not os.path.isdir(BASE_LOG):
    os.mkdir(BASE_LOG)

# log文件的全路径
logfile_path = os.path.join(BASE_LOG,'log.log')
logfile_another = os.path.join(BASE_LOG,'another.log')

# log配置字典
LOGGING_DIC = {
    'version':1,
    'disable_existing_loggers':False,
    'formatters':{
        'standard':{
            'format':standard_format,
        },
        'simple':{
            'format':simple_format
        },
    },
    'filters':{},
    'handlers':{
        # 打印到终端的日志
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'simple'
        },
        # 打印到文件到日志
        'default':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'formatter':'standard',
            'filename':logfile_path,    # 日志文件
            'maxBytes':1024 * 1024 * 5, # 日志大小 5M
            'backupCount':5,
            'encoding':'utf-8',
        },
    },
    'loggers':{
        # logging.getLoger(__name__)拿到到logger配置
        '':{
            'handlers':['default','console'],
            'level':'INFO',
            'propagate':True    # 向上，更高level的logger的传递
        },
    },
}