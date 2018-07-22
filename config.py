#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 9:36
# @Author  : ganliang
# @File    : config.py
# @Desc    : kfaka配置文件

import os


def init():
    """初始化组件 如果组件没有安装 则安装组件"""
    os.system("pip install kafka")
    # os.system("python -m pip install --upgrade pip")
    os.system("pip install redis")


if __name__ == "__main__":
    init()
