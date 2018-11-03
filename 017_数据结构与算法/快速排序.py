#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma

import random


import random
total = 10000
li = [i for i in range(total)]
res = []
num = 9999
for i in range(num):
  t = random.randint(i,total-1)
  res.append(li[t])
  li[t], li[i] = li[i], li[t]

res = li


def partition(li,left,right):
    tmp = li[left]
    while left < right:
            while left < right and li[right] >= tmp:
                right = right-1
            li[left] = li[right]

            while left < right and li[left] <= tmp:
                left = left +1
            li[right] = li[left]

    li[left] = tmp
    return left

def quickSort(li,left,right):
    if left < right:
        mid = partition(li,left,right)
        quickSort(li,left,mid-1)
        quickSort(li,mid+1,right)

import time
start_time = time.time()
quickSort(li,1,len(li)-1)
print('排序后：',li)
print('所花时间：',time.time() - start_time)
