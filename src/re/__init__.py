#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 14:57
0  # @Author  : ganliang
# @File    : __init__.py.py
# @Desc    : re正则表达式

import re

print(re.match("[a-z]+", "a123bc").group())
print(re.findall("[a-z]+", "a123bc"))
print(re.search("[a-z]+", "a123bc").group())
print(re.split("[0-9]+", "a123bc"))
print(re.sub("[0-9]", "", "a123bc"))

