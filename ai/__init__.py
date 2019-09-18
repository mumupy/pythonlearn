#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 22:26
# @Author  : ganliang
# @File    : __init__.py.py
# @Desc    : 图片识别

import os

# 导入 ImageAI 目标检测类
from imageai.Detection import ObjectDetection

execution_path = os.getcwd()
# 定义目标检测类
detector = ObjectDetection()

# 将模型的类型设置为 RetinaNet
detector.setModelTypeAsRetinaNet()

# 将模型路径设置为 RetinaNet 模型的路径
detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))

# 将模型加载到的目标检测类
detector.loadModel()

# 调用目标检测函数，解析输入的和输出的图像路径
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "image.jpg"),
                                             output_image_path=os.path.join(execution_path,
                                                                            "imagenew.jpg"))

# 迭代执行 detector.detectObjectsFromImage 函数并返回所有的结果
for eachObject in detections:
    print(eachObject["name"] + " : " + eachObject["percentage_probability"])
