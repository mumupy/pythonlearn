#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18/018  21:11
# @Author  : ganliang
# @File    : path.py
# @Desc    : 设置项目的环境变量
import os
import sys

currentProjectPath = os.path.split(os.path.split(os.getcwd())[0])[0]
print(currentProjectPath)
sys.path.append(currentProjectPath)
print("sys.path=%s" % (sys.path))


def mypath():
    print(sys.path)
