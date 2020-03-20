# coding=utf-8
import PyPDF2
import os


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


def pdf_page_count(path):
    pdfReader = PyPDF2.PdfFileReader(path)
    return pdfReader.numPages

# TODO 添加 加密的解析和处理

for path in all_path('/Volumes/iboysoft_ntfs_disk2s1_/Courses/面试汇总2/java_interview', ['.pdf']):
    try:
        count = pdf_page_count(path)
        print('%s => %s' % (path, count))
    except TypeError:
        print('Error : ' + path)
        count = 0
        pass
