#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/14/014  22:15
# @Author  : ganliang
# @File    : list.py
# @Desc    : 列表 可变序列

myarray = [12, 34, 1, 3, 2, 9, 4, 3, 5, 9, 6, 2, 6]
print("myarray=%s\n" % myarray)
# 列表分片
print("myarray[1]=%s" % myarray[1])
print("myarray[-1]=%s" % myarray[-1])
print("myarray[2:4]=%s\n" % myarray[2:4])

# 添加元素
myarray.append(12)
print("myarray.append(12)=%s\n" % myarray)

# 插入元素
myarray.insert(0, 0)
print("myarray.insert(0,0)=%s\n" % myarray)

# 将集合添加到集合中
myarray.extend([12, 345])
print("myarray.extend([12, 345])=%s\n" % myarray)

# 删除最后一个元素
print("pop element=%s,extra elements=%s" % (myarray.pop(), myarray))

# 删除第一个元素
print("pop element=%s,extra elements=%s\n" % (myarray.pop(0), myarray))

# 移除元素 移除第一次出现的元素
myarray.remove(1)
print("myarray.remove(1)=%s\n" % myarray)

# 数组索引 如果索引不存在 则报异常
try:
    indexElement = myarray.index("12")
    print("myarray.index(\"12\")=%s" % indexElement)
except:
    print("myarray.index(\"12\") not exists")
finally:
    print("clean up...\n")

# 集合计算元素出现的次数
print("myarray.count(1)=%s\n" % myarray.count(1))

# sort 排序
myarray.sort()
print("myarray.sort()=%s" % myarray)
myarray.reverse()
print("myarray.reverse()=%s\n" % myarray)
print("cmp(1,1)=%s" % cmp(1, 1))
print("cmp(2, 1)=%s" % cmp(2, 1))
print("cmp(2, 4)=%s" % cmp(2, 4))

## 转化为list列表
print("list(myarray)=%s\n" % list(myarray))

# set去除重复数据
print("set(myarray)=%s\n" % set(myarray))
