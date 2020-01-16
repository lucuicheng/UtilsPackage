# coding=utf-8

import os
import cv2

file_path = '/Users/cuichenglu/Desktop/Screen Recording 2020-01-16 at 1.14.33 PM.mov'

cap = cv2.VideoCapture(file_path)
# file_path是文件的绝对路径，防止路径中含有中文时报错，需要解码 .encode('utf-8')
if cap.isOpened():  # 当成功打开视频时cap.isOpened()返回True,否则返回False
    # get方法参数按顺序对应下表（从0开始编号)
    rate = cap.get(5)  # 帧速率
    FrameNumber = cap.get(7)  # 视频文件的帧数
    duration = FrameNumber / rate  # 帧速率/视频总帧数 是时间，默认为 s (秒)
    print("%.2f s" % duration)
    print("%.2f m" % (duration / 60))
