#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 20:37
# @Author  : ganliang
# @File    : deco.py
# @Desc    : 装饰器

def deco(func):
    def f1(type):
        print(type)
        func("f1 {0}".format(type))
        print("func")

    return f1


@deco
def d1(type):
    print("d1")
    print("d1" + type)


d1(123)


def deco1(type=""):
    def dd1(func):
        def ddd1():
            print("f1 {0}".format(type))
            func()
            print("func")

        return ddd1

    return dd1


@deco1(type="dd1")
def dd1():
    print("dd1")


@deco1(type="dd1")
def dd2():
    print("dd2")


dd1()
dd2()


