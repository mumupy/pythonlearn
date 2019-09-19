#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 22:50
# @Author  : ganliang
# @File    : ndarray.py
# @Desc    : numpy数组

import numpy as np

print (np.array([1, 2, 3], dtype=int))
print (np.array([[[1, 2, 3], [1, 3, 2], [3, 4, 2]], [[1, 3, 2], [1, 3, 2], [3, 5, 2]]], dtype=complex, ndmin=3))

# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
print(np.dtype("i4"))
print(np.dtype("int32"))
print(np.dtype([("qianqian", np.int8)]))

student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)

print (np.array([], dtype=student, ndmin=2))
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a["name"])
print (a[0])

a = np.arange(24, dtype=np.int64)
print (a)

# 维度 行数  列数
shape = a.reshape((4, 2, 3))
print (shape)
print (shape.shape)
print (shape.itemsize)
print (shape.flags)

a = np.empty([1, 2, 3, 3], dtype=np.int64)
print(a)

x = np.zeros(5)
print(x)

y = np.zeros((5,), dtype = np.int)
print(y)

z = np.zeros((3,3,4), dtype = [('x', 'i4'), ('y', 'i4')])
print(z)

x = np.ones([2,3], dtype = int)
print(x)

x =  [1,2,3]
a = np.asarray(x)
print (a)
print (np.array(x))

s =  b'Hello World'
a = np.frombuffer(s, dtype = "S1")
print (a)

it=iter(range(5))
# 使用迭代器创建 ndarray
x=np.fromiter(it, dtype=np.int64)
print(x)

a = np.linspace(1,1,10)
print(a)

a = np.logspace(1.0,  2.0, num =  10)
print (a)