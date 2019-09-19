#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 22:18
# @Author  : ganliang
# @File    : __init__.py.py
# @Desc    : 上下文管理器
from contextlib import contextmanager


class ContextIllustration(object):

    def __enter__(self):
        print ("enter ContextIllustration")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print ("exit ContextIllustration")
        if exc_type != None:
            print ("throw error %s" % exc_type)


@contextmanager
def contextlib():
    print("enter contextlib")
    try:
        yield
    except Exception as ex:
        print ("occor error")
        raise ex
    else:
        print ("no error")
    finally:
        print ("exit contextlib")


if __name__ == "__main__":
    contextIllustration = ContextIllustration()
    with ContextIllustration():
        pass

    cl = contextlib()
    cl.send("")
