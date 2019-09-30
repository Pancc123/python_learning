# -*- coding:utf-8 -*-
import os

def findDirFile(dirName, keyword):
    for x in os.listdir(dirName):
        if os.path.isdir(x):
            nextDirName = os.path.realpath(x)
            findDirFile(nextDirName, keyword)
        if os.path.isfile(dirName + '/' + x) and (keyword in x):
            print('找到以下文件：%s' % os.path.realpath(x))


t = findDirFile('D:/python_test','test')
