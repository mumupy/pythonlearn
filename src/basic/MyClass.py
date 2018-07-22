#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/15/015  15:48
# @Author  : ganliang
# @File    : MyClass.py
# @Desc    : 自定义类
class MyClass:
    """自定义类 学习类的定义"""
    name = ""

    def __init__(self, name):
        """构造方法"""
        print("_init_ method")
        self.name = name

    def myMethod(self):
        """自定义方法 打印方法名称"""
        print("myMethod", self.__class__.__name__, self.name)
        return None


myobject = MyClass("lovecws")
myobject.myMethod()
print(myobject.name)
myobject.__init__("lovecws5211314")
print(myobject.name)
