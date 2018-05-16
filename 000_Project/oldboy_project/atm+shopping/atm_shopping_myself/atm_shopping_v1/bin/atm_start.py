#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import os
import sys
from core import main

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将项目根目录将如syspath，便于后续各个目录中的文件调用
sys.path.append(BASE_DIR)


if __name__ == '__main__':
    main.run()