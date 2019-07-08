#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 21:35
# @Author  : ganliang
# @File    : wsgiref_simple.py
# @Desc    : wsgiref服务

from wsgiref.simple_server import make_server


def run_server(environ, start_response):
    """
    当有用户在浏览器上访问：http://127.0.0.1:8000/, 立即执行该函数并将函数的返回值返回给用户浏览器
    :param environ: 请求相关内容，比如浏览器类型、版本、来源地址、url等
    :param start_response: 响应相关
    :return:
    """

    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h1>我旁边的这个人长的真丑呀!!') ]


if __name__ == '__main__':
    httpd = make_server('localhost', 8001, run_server)
    httpd.serve_forever()
