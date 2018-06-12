#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import struct
# 得出字符串的长度

str = 'sssssssssssssssss'
str1 = 'sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss'

res = struct.pack('i',len(str))
res1 = struct.pack('i',len(str1))

print(res)
print(res1)



res_decode = struct.unpack('i',res)
res_decode1 = struct.unpack('i',res1)
print(res_decode)
print(res_decode1[0])
