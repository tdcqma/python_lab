#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
import os,sys
from core import main

BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    main.run()