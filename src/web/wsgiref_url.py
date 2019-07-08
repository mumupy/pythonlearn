#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 21:40
# @Author  : ganliang
# @File    : wsgiref_url.py
# @Desc    : 使你的wsgi app1 server支持多url

from wsgiref.simple_server import make_server


def western():
    return "欢迎来到欧美专区"


def japan():
    return "欢迎来到日本人专区"


def routers():
    """负责把url与对应的方法关联起来"""
    urlpatterns = (
        ('/western/', western),
        ('/japan/', japan),
    )

    return urlpatterns


def run_server(environ, start_response):
    """
    当有用户在浏览器上访问：http://127.0.0.1:8000/, 立即执行该函数并将函数的返回值返回给用户浏览器
    :param environ: 请求相关内容，比如浏览器类型、版本、来源地址、url等
    :param start_response: 响应相关
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    url = environ.get("PATH_INFO")
    urlpatterns = routers()

    func = None

    for item in urlpatterns:
        if item[0] == url or item[0].startswith(url):
            func = item[1]
            break
    if func:
        return [bytes(func()), ]
    else:
        return [bytes('404 not found.'), ]


if __name__ == '__main__':
    httpd = make_server('localhost', 8001, run_server)
    httpd.serve_forever()
