#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/15/015  20:52
# @Author  : ganliang
# @File    : file.py
# @Desc    : 文件目录

import glob
import os
import sys


def readFile(filePath):
    """文件io操作符"""
    file = open(filePath)
    lines = file.readlines(100)
    for line in lines:
        print(line)

    file.seek(0)
    filcontent = file.read()
    print(filcontent)


def writeFile(filePath):
    """文件写入"""
    file = open(filePath, "a")
    file.write("first line\n")
    file.close()


def detaillist(filePath):
    """详细打印文件夹下的所有文件"""
    if os.path.exists(filePath):
        if os.path.isfile(filePath):
            print(filePath)
        elif os.path.isdir(filePath):
            files = os.listdir(filePath)
            for file in files:
                detaillist(os.path.join(filePath, file))
    else:
        print("filePath:%s 不存在" % filePath)


def isFile(filePath):
    """判断文件是否为文件"""
    # os.path.exists(filePath)
    return os.path.isfile(filePath)


def globMatch(filePath):
    files = glob.glob(filePath)
    for file in files:
        print(os.path.join(filePath, file))


def main():
    filename = "file.txt"
    writeFile(filename)
    readFile(filename)


# main()
detaillist("D:\data\webmagic\\finance")
# globMatch("D:\data\webmagic\\finance\\*.json")
