#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/15/015  14:48
# @Author  : ganliang
# @File    : error.py
# @Desc    : 报错处理机制

try:
    while True:
        record = input("please input:")  # 输入数字
        print("record=", record)
        if record == 0 or not record:
            break
except SyntaxError as error:
    print("keyError: %s" % error)
except EOFError as error:
    print("eoferror: %s" % error)
finally:
    print("finally...")
