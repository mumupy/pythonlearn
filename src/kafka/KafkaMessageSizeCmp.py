#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 16:29
# @Author  : ganliang
# @File    : KafkaMessageSizeCmp.py
# @Desc    : kafka消息量对比
import time

from KafkaUtil import KafkaUtil

MESSAGE_1M = " " * 1024 * 512
MESSAGE_1K = " " * 1024


def messageSizeCmp(message, count=100):
    """
      测试工具
    """
    beginTime = time.time()
    kafkaUtil = KafkaUtil("192.168.0.51:9092", "kafkaProcedureGroupId", "babymm")
    messages = [message] * count
    kafkaUtil.procedure(*messages)
    endTime = time.time()
    print("speed time : %s" % (endTime - beginTime))


# speed time : 10.4809999466 (MESSAGE_1K,10000)
messageSizeCmp(MESSAGE_1K, 10000)

# speed time : 519.098999977 (MESSAGE_1M,10000)
# messageSizeCmp(MESSAGE_1M,10000)
