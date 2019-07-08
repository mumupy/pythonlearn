#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 23:00
# @Author  : ganliang
# @File    : urls.py.py
# @Desc    : app的url分发规则
from django.conf.urls import url

from app01 import views

urlpatterns = [
    url(r'test/', views.test_view),
    url(r'testdb/', views.testdb),
    url(r'getdbs/', views.getdbs),
    url(r'base/', views.base),
    url(r'main/', views.main),
    url(r'menu/', views.menu),
]
