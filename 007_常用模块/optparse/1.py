#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

from optparse import OptionParser

# 生成对象
parser = OptionParser()

# 使用add_option来增加命令行参数
# parser.add_option('-f','--file',
#                   dest='filename',
#                   help='write report to file',
#                   metavar = 'FIFE')
#
# parser.add_option('-q','--quite',action='store_false',
#                   dest='verbose',
#                   default=True,
#                   help='dont\'t print status messages to stdout')

parser.add_option("-g", "--group", dest="group", help='group name', type="string")
parser.add_option("-c", "--commend", dest="cmd", help='commend', type="string")
parser.add_option("-m", "--module", dest="module", help='module', type="string")
parser.add_option("-s", "--src", dest="src", help='source file or path', type="string")
parser.add_option("-d", "--dst", dest="dst", help='destination file or path', type="string")
parser.add_option("-a", "--action", dest="action", help='action for module file, [get/put]', type="string")

# 使用parse_args()来解析程序对命令行参数
(opt,args) = parser.parse_args()

print(opt.group)
print(args)
