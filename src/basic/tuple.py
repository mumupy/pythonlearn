#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/14/014  22:08
# @Author  : ganliang
# @File    : tuple.py
# @Desc    : 元组 不可变 元组内容初始化之后不可以更改 但是可以重新赋值

mytuple = (1, "lovecw", 5211314, 13j, 12.56789)
print(mytuple)
# tuple[1]="aals"  TypeError: 'type' object does not support item assignment

# 使用count方法 找到字符所在的索引位置
print(mytuple[1])
print(mytuple.count("lovecw"))
print(mytuple.index("lovecw"))
print(len(mytuple))

mytuple=(1,23,4)
print(mytuple)