#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 13:36
# @Author  : ganliang
# @File    : __init__.py.py
# @Desc    : ini配置文件解析
import configparser


def write_ini_file():
    config = configparser.ConfigParser()
    config["default"] = {"name": "ganliang", "password": 12345}
    config["spring"] = {"web": {"server": "localhost", "port": 8080}}
    config["mybatis"] = {"database": "mysql", "user": "root", "password": "123456", "driver": "com.mysql.jdbc.Driver"}
    with open("demo.ini", "wb") as config_file:
        config.write(config_file)


def read_ini_file():
    config = configparser.ConfigParser()
    config.read("demo.ini")
    print (config["default"]["name"])


if __name__ == "__main__":
    # write_ini_file()
    read_ini_file()
