#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import logging

from conf import settings

def logger(log_type):

    # create logger
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    log_file = "%s/log/%s" % (settings.BASE_DIR,settings.LOG_TYPE[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    # 日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 添加格式到ch和fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger