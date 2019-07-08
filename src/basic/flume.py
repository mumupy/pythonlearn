#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/1 20:54
# @Author  : ganliang
# @File    : flume.py
# @Desc    : flume文件生成器

import time


def record():
    file = open("1.txt", "w")
    for i in range(100000):
        line = "%s lovecws %s" % (time.time(),i)
        print(line)
        file.write(line + "\n")
        time.sleep(1)
        file.flush()


if __name__ == "__main__":
    record()
