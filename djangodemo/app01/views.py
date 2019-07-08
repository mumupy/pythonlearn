# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views.decorators.http import require_http_methods

from app01.models import Test


def test_view(request):
    print("test_view")
    return render(request, "test.html", {"name": "lovecws", "datas": range(100)})


def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def getdbs(request):
    response = ""
    list = Test.objects.all()
    for var in list:
        response += var.name + " "
    return HttpResponse("<p>" + response + "</p>")


@require_http_methods(["GET"])
def base(request):
    return render(request, "base.html")


@require_http_methods(["GET"])
def main(request):
    return render(request, "main.html")


@require_http_methods(["POST"])
def menu(request):
    return render(request, "menu.html", {"name": "lovecws", "datas": range(10)})
