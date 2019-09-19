#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 22:06
# @Author  : ganliang
# @File    : __init__.py.py
# @Desc    : 装饰器
import time
from threading import RLock

lock = RLock()


def synchronized(function):
    def _synchronized(*args, **kwargs):
        try:
            time.sleep(1)
            lock.acquire()
            function(*args, **kwargs)
        finally:
            lock.release()

    return _synchronized


@synchronized
def hello_world():
    print ("babyMM")


if __name__ == "__main__":
    for i in range(10):
        thread.start_new_thread(hello_world, ())
