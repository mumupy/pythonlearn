#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 21:00
# @Author  : ganliang
# @File    : unittest_test.py
# @Desc    : unittest
import unittest


class ABasicUnitTest(unittest.TestCase):

    def testF1(self):
        print("ABasicUnitTest")


class BBasicUnitTest(unittest.TestCase):

    def testF1(self):
        print("BBasicUnitTest")


if __name__ == "__main__":
    unittest.main()
