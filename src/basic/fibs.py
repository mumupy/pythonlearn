#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 14:17
# @Author  : ganliang
# @File    : fibs.py
# @Desc    : 斐波那函数

def fibs(count):
    """
    斐波那函数 后一个数字是前两个数字之和
    count 求前count的列表
    """
    if isinstance(count, int) and count >= 0:
        fibsList = [0, 1]
        if (count <= 2):
            return fibsList[count]
        else:
            for i in range(count - 2):
                num = fibsList[-2] + fibsList[-1]
                fibsList.append(num)
            return fibsList
    else:
        raise TypeError("类型错误")


if __name__ == '__main__':
    print(fibs(0))
    print(fibs(1))
    print(fibs(1000))

    keys = [x for x in range(10) if x > 5]
    print(keys)
    values = filter(lambda x: x % 2 == 0, range(10))
    print(values)
