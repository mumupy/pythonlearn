#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 21:55
# @Author  : ganliang
# @File    : wsgiref_image.py
# @Desc    : 使自行开发的web erver支持图片

import os
import re
from wsgiref.simple_server import make_server

BASE_DIR = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")


def img_handler(url):
    img_relative_path = re.sub("/static/", "imgs/", url, count=1)
    img_path = os.path.join(BASE_DIR, img_relative_path).replace("\\", "/")
    print('img', BASE_DIR, img_path)
    f = open(img_path, 'rb')
    data = f.read()
    f.close()
    return data


def western():
    data = '''
    <h1>欢迎来到欧美专区</h1>

    <img src='/static/test_america.jpg' width='800px'/>

    '''

    return data


def japan():
    data = '''
    <h1>欢迎来到日本人专区</h1>

    <img src='/static/testimg.gif' />

    '''

    return data


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
    content_type = 'text/html;charset=utf-8'

    url = environ.get("PATH_INFO")
    urlpatterns = routers()

    func = None
    if url.startswith('/static/'):  # 代表是张图片
        content_type = 'text/jpg;charset=utf-8'
        start_response('200 OK', [('Content-Type', content_type)])

        img_data = img_handler(url)
        return [img_data, ]

    for item in urlpatterns:

        if item[0] == url:
            func = item[1]
            break

    start_response('200 OK', [('Content-Type', content_type)])
    if func:
        return [bytes(func()), ]
    else:
        return [bytes('404 not found.'), ]


if __name__ == '__main__':
    httpd = make_server('localhost', 8001, run_server)
    httpd.serve_forever()
