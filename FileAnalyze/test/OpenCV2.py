# coding=utf-8

import os
import cv2

filePathGroup = list()
filePathGroup.append('/Users/cuichenglu/Desktop/Screen Recording 2020-01-16 at 1.14.33 PM.mov')


def videoTime(filePath):
    cap = cv2.VideoCapture(filePath)
    # file_path是文件的绝对路径，防止路径中含有中文时报错，需要解码 .encode('utf-8')
    if cap.isOpened():  # 当成功打开视频时cap.isOpened()返回True,否则返回False
        rate = cap.get(5)  # 帧速率
        frameNumber = cap.get(7)  # 视频文件的帧数
        duration = frameNumber / rate  # 帧速率/视频总帧数 是时间，默认为 s (秒)
        return {filePath: duration}
    else:
        return {filePath: '文件损坏 或 不存在'}


for path in filePathGroup:
    data = videoTime(path)
    print('%s => %.2fs => %.2fm' % (path, data.get(path), data.get(path) / 60))
