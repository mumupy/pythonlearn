#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 17:29
# @Author  : ganliang
# @File    : screenshot.py
# @Desc    : 屏幕截图
import time

import numpy as np


def window_capture():
    """
    window截屏 不跨平台
    :return:
    """

    def _window_capature(filename):
        import win32gui, win32ui, win32con, win32api

        hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
        # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
        hwndDC = win32gui.GetWindowDC(hwnd)
        # 根据窗口的DC获取mfcDC
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        # mfcDC创建可兼容的DC
        saveDC = mfcDC.CreateCompatibleDC()
        # 创建bigmap准备保存图片
        saveBitMap = win32ui.CreateBitmap()
        # 获取监控器信息
        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]
        # print w,h　　　#图片大小
        # 为bitmap开辟空间
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        # 高度saveDC，将截图保存到saveBitmap中
        saveDC.SelectObject(saveBitMap)
        # 截取从左上角（0，0）长宽为（w，h）的图片
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
        saveBitMap.SaveBitmapFile(saveDC, filename)

    beg = time.time()
    for i in range(10):
        _window_capature("haha{0}.jpg".format(time.time()))
    end = time.time()
    print(end - beg)
    print ((end - beg) / 10)


def selenium_capature():
    """
    selenium web页面截屏
    :return:
    """
    from selenium import webdriver
    import time
    def capture(url, filename="capture.png"):
        browser = webdriver.Chrome(r"C:\Program Files (x86)\Google Chrome\chromedriver.exe")
        browser.set_window_size(1200, 900)
        browser.get(url)  # Load page
        browser.execute_script("""
      (function () {
       var y = 0;
       var step = 100;
       window.scroll(0, 0);
       function f() {
        if (y < document.body.scrollHeight) {
         y += step;
         window.scroll(0, y);
         setTimeout(f, 50);
        } else {
         window.scroll(0, 0);
         document.title += "scroll-done";
        }
       }
       setTimeout(f, 1000);
      })();
     """)
        for i in range(30):
            if "scroll-done" in browser.title:
                break
            time.sleep(1)
        beg = time.time()
        for i in range(10):
            browser.save_screenshot(filename)
        end = time.time()
        print(end - beg)
        browser.close()

    capture("//www.jb51.net")


def pil_capature():
    """
    python pil模块截屏
    :return:
    """
    import time
    import numpy as np
    from PIL import ImageGrab
    # 每抓取一次屏幕需要的时间约为1s,如果图像尺寸小一些效率就会高一些
    beg = time.time()
    for i in range(10):
        img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
        img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
        img.save('{0}.png'.format(time.time()))
    end = time.time()
    print(end - beg)


def grap_capature():
    """
    pythonpil模块截屏
    :return:
    """
    from PIL import ImageGrab
    im = ImageGrab.grab()
    im.save('{0}.png'.format(time.time()))


def pyqt_capature():
    """
    pyqt截屏 指定程序抓屏 被指定的程序不能最小化 否则抓取不到屏幕
    :return:
    """
    from PyQt5.QtWidgets import QApplication
    import win32gui
    import sys

    # hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
    hwnd = win32gui.FindWindow(None, r'D:\Program Files\JetBrains\PyCharm Community Edition 2018.3.5\bin\pycharm64.exe')
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img.save("screenshot.jpg")


def pyautogui_capature():
    """
    pyautogui截屏
    :return:
    """
    import pyautogui
    import cv2

    # img = pyautogui.screenshot(region=[0, 0, 100, 100])  # x,y,w,h
    img = pyautogui.screenshot()  # x,y,w,h
    # img.save('screenshot.png')
    img.save("pyautogui_{0}.png".format(time.time()))
    cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


pyqt_capature()
