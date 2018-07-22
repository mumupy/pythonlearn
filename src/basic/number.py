#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/14/014  21:32
# @Author  : ganliang
# @File    : number.py
# @Desc    : 数值类型 python提供三种类型数据类型 浮点、整数、虚数

print(type(1234))
print(type("slsll"))
print(type([]))
print(type(12.12))

# 虚数
print(type(12j))

# 整数
print("lovecws %d" % 5211314)

# 浮点数 取几位小数点
print("lovecws %f" % 12.4444999)
print("lovecws %.2f" % 12.4444999)
print("lovecws %0.f" % 12.4444999)
print("lovecws %.04f" % 12.4444999)
print("lovecws %.4f" % 12.4444999)

# 将十进制转化为八进制
print("lovecws %o" % 12)

# 将十进制转化为16进制
print("lovecws %x" % 12)
