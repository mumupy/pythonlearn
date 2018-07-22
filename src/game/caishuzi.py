#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 11:42
# @Author  : ganliang
# @File    : caishuzi.py
# @Desc    : 猜数字游戏
import random


def caishuzi(heaerNumber=10, maxRetry=3):
    """猜数字游戏
       heaerNumber 猜的数字 默认为10
       maxRetry 是最大尝试数字 默认为3
    """
    if isinstance(10, int) and isinstance(maxRetry, int):
        # if type(heaerNumber)==type(0) and type(maxRetry)==type(0):
        i = 0
        while i < maxRetry:
            mysecurt = input("please enter my security:")
            if (mysecurt == heaerNumber):
                if i == 0:
                    print("beautiiful! you got it!")
                elif i == 1:
                    print("very good you got it！")
                elif i == 2:
                    print("good you got it!")
                else:
                    print("ok you got it!")
                break
            else:
                if i == maxRetry - 1:
                    print("full error ")
                else:
                    if mysecurt > heaerNumber:
                        print("game over! please retry! you guse is bigger than ")
                    else:
                        print("game over! please retry! you guse is letter than")
            i += 1
    else:
        raise TypeError("heaerNumber、maxRetry 类型错误")

if __name__ == "__main__":
    caishuzi(int(random.uniform(0, 10)), 2)