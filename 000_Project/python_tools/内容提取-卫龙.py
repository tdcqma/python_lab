#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import re

with open(r'policy.txt',mode='r',encoding="utf-8") as f:
    date = f.read()

    s = ''
    lineNum = 0
    dateList = []

    for i in date.split("\n"):

        if 'A2-VPN-FW-5-6-slave' in i:
            continue

        if 'config firewall policy' in i:
            continue

        if lineNum < 10:
            s = s+ i + '\n'
            lineNum += 1

        if lineNum > 9:
            lineNum = 0
            dateList.append(s)
            # print(s)
            s = ''

    for i in dateList:
        '''
        set srcintf "TEST"
        set dstintf "PROD"
        '''
        if 'set srcintf "TEST"' in i and 'set dstintf "PROD"' in i:
            print(i)

            with open(r'policy_new.txt',mode='a',encoding='utf-8') as f_new:
            	f_new.write(i)
