#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/15/015  14:57
# @Author  : ganliang
# @File    : function.py
# @Desc    : 函数功能

def printPerson(name="ganliang", password="12345"):  # 参数设置默认值
    """打印名称和密码"""
    print("name:%s,password:%s" % (name, password))

    def print_person():
        """嵌套方法 只能对printPerson方法可见"""
        print("netst function")

    print_person()


def maxNumber(n1, n2):
    """求出两个数字最大的数字"""
    if n1 == None or n2 == None:
        raise TypeError("n1 or n2 must not None")
    if n1 > n2:
        return n1
    else:
        return n2


print(printPerson.__doc__)
print(printPerson())

print("maxNumber(10,100):%d" % maxNumber(10, 200))

# 将数字转化为字符串
print(type(str(123)))


def sum(m):
    """递归函数 计算前多少数字相加 m参数太大会造成栈空间溢出"""
    try:
        if (m == 0):
            return 1
        else:
            return m + sum(m - 1)
    except TypeError as error:
        print("m=%d太大栈空间溢出，%s" % (m, error))


print("sum(100, 0)=%d" % sum(100))
