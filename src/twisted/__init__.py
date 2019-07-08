#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 21:10
# @Author  : ganliang
# @File    : __init__.py.py
# @Desc    : twiset异步线程服务器
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver


class SimpleLogger(LineReceiver):
    def lineReceived(self, line):
        print(line)
        self.sendLine("hello world!")

    def connectionLost(self, reason=None):
        print(self.transport.client + "connectionLost",)

    def connectionMade(self):
        print("got connection from ", self.transport.client)


factory = Factory()
factory.protocol = SimpleLogger
reactor.listenTCP(1234, factory)
reactor.run()
