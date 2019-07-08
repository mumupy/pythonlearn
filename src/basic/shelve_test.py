#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 14:11
# @Author  : ganliang
# @File    : shelve_test.py
# @Desc    : shelve数据库
import shelve
import sys

data=shelve.open("a.data",writeback=True)
print(data['x'])
data['x']=['a','b','c']
data['x'].append("d")
print(data['x'])

import getopt
getopt.getopt(sys.argv,"")

