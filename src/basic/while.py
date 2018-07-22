#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/15/015  13:19
# @Author  : ganliang
# @File    : while.py
# @Desc    : 循环

i = 0
while i < 10:
    print(i)
    i = i + 1

for i in range(1, 100, 10):
    print(i)

try:
    while True:
        record = input("please input:")  # 输入数字
        print("record=", record)
        if record == 0 or not record :
            break
except KeyError:
    print("keyError")

for i in  range(100):
    print(i)
else:
    print("not in i")