# coding=utf-8

import os
import cv2

# 提取抽象方法

def all_path(dirname, filtered):  # 设置过滤后的文件类型 当然可以设置多个类型
    result = []  # 所有的文件

    for maindir, subdir, file_name_list in os.walk(dirname):

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容

            if ext in filtered:
                result.append(apath)

    return result


def all_type(dirname):  # 设置过滤后的文件类型 当然可以设置多个类型
    result = {}  # 所有的文件

    for maindir, subdir, file_name_list in os.walk(dirname):

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
            if ext in result.keys():
                result[ext] = result.get(ext) + 1
            else:
                result[ext] = 1

    return result


def video_time(filePath):
    cap = cv2.VideoCapture(filePath)
    # file_path是文件的绝对路径，防止路径中含有中文时报错，需要解码 .encode('utf-8')
    if cap.isOpened():  # 当成功打开视频时cap.isOpened()返回True,否则返回False
        rate = cap.get(5)  # 帧速率
        frameNumber = cap.get(7)  # 视频文件的帧数
        duration = frameNumber / rate  # 帧速率/视频总帧数 是时间，默认为 s (秒)
        return {filePath: duration}
    else:
        return {filePath: '文件损坏 或 不存在'}


# for type, count in all_type('/Users/cuichenglu/IdeaProjects/').items():
#     print(type, count)

for path in all_path('/Volumes/iboysoft_ntfs_disk2s1_/Courses/88G小马哥全新JAVA架构师实战课程 九大阶段轻松成就合格JAVA架构师 视频+源码+面试', ['.mp4']):
    try:
        data = video_time(path)
        print('%s => %.2fs => %.2fm' % (path, data.get(path), data.get(path) / 60))
    except TypeError:
        pass
    # continue
