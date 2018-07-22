#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 16:11
# @Author  : ganliang
# @File    : KafkaUtil.py
# @Desc    : kafka工具类

from kafka import KafkaConsumer
from kafka import KafkaProducer


class KafkaUtil:
    """kafka工具类 发送消息kafka消息"""

    def __init__(self, bootstrapServers, groupId, topic):
        self.bootstrapServers = bootstrapServers
        self.groupId = groupId
        self.topic = topic

    def consumer(self):
        """
            消费者消费消息
            topic 主题名称
            bootstrapServers kafka服务器地址信息
        """
        kafkaConsumerConfig = {"group_id": self.groupId,
                               "bootstrap_servers": self.bootstrapServers
                               }
        consumer = KafkaConsumer(self.topic, **kafkaConsumerConfig)
        for record in consumer:
            print(record)

    def procedure(self, *messages):
        """
            生产者生产消息
            messages 发送的消息集合
        """
        kafkaConsumerConfig = {"client_id": self.groupId,
                               "bootstrap_servers": self.bootstrapServers,
                               "max_request_size": 20 * 1024 * 1024
                               }
        producer = KafkaProducer(**kafkaConsumerConfig)
        for message in messages:
            result = producer.send(self.topic, message)
            print(result.get())


if __name__ == "__main__":
    util = KafkaUtil("192.168.0.51:9092", "kafkaConsumerGroupId", "babymm")
    util.procedure("lovecws")
    util.consumer()
