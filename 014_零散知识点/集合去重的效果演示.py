#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

set_1 = {2,4,5,9,8}
list_1 = [1,2,3,4,5,6,7,3,2,5,2,1]
print('set_1:',set_1)
print('list_1:',list_1)

set_2 = set_1.union(list_1)
print('----------')
print('set_2',set_2)

# 将集合转列表
print('----------')
list_2 = list(set_2)
print(list_2,type(list_2))