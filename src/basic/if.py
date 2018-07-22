#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/15/015  13:05
# @Author  : ganliangWW
# @File    : if.py
# @Desc    : if判断
myint = 2
if myint > 1:
    print("2>1")
    if 1 == True:
        print("1==True")
elif myint == 1:
    print("3>1")
else:
    print("else")

if 1 in [1, 2, 3]:
    print("1 in [1, 2, 3]=%s" % (1 in [1, 2, 3]))
