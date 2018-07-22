#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/15/015  16:14
# @Author  : ganliang
# @File    : modular.py
# @Desc    : 模块

import os
import sys
from src.modular.MyModular import MyModular

dir(sys)
dir(os)
dir(MyModular)

print(sys.path)
print("sys.argv=%s" % sys.argv)
print("os.path=%s" % os.path)
print("sys.modules=%s" % sys.modules)
