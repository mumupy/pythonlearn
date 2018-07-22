#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/14/014  22:20
# @Author  : ganliang
# @File    : map.py
# @Desc    : 字典 java、scala中的map

mymap = {"name": "ganliang", "lover": "cws"}
print(mymap["name"])
print(mymap.get("name"))

mapkeys = mymap.keys()
print(mapkeys)

mapvalues = mymap.values()
print(mapvalues)

mymap["son"]="ganzimu"
print(mymap)
