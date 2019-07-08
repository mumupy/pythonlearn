#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 20:55
# @Author  : ganliang
# @File    : doctest_test.py
# @Desc    : doctest测试  执行模块测试

import doctest
import src.deco

if __name__ == "__main__":
    doctest.testmod(src.deco)
