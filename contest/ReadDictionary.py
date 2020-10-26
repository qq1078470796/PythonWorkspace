# -*- coding: UTF-8 -*-

"""
1、读取指定目录下的所有文件
2、读取指定文件，输出文件内容
3、创建一个文件并保存到指定目录
"""
import os
from contest.BaseData import BaseData

baseDataList = []

# 获取所有数据点和其属性
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        filename = os.path.join('%s%s' % (filepath, allDir))
        hobbyList = readFile(filename)
        basedata = BaseData(allDir.split(".")[0], hobbyList)
        baseDataList.append(basedata)

# 读取文件内容
def readFile(filename):
    fopen = open(filename, 'r', encoding='utf-8')  # r 代表read
    list = []
    for eachLine in fopen:
        list.append(eachLine)
    fopen.close()
    return list

# 输入多行文字，写入指定文件并保存到指定文件夹
def writeFile(filename):
    with open(filename, 'w') as file_obj:
        for data in baseDataList:
            hobbys = " "
            for hobby in data.hobbys:
                hobbys =hobbys +" "+hobby
                print(hobbys)
            file_obj.write(data.id," ",hobbys )



if __name__ == '__main__':
    filePathC = "E:\\Data\\ContestData\\attributes\\"
    eachFile(filePathC)
    filePath = "E:\\Data\\ContestData\\1.txt"
    writeFile(filePath)
