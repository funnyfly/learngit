#!/usr/bin/python
#-*-coding:utf-8-*-
'''
打印当前目录和子目录下所有包含特定字符的文件所在目录
'''

import os

def search(item,curdir=os.path.abspath('.')):
        for x in os.listdir(curdir):
            c_dir = os.path.join(curdir,x)
            if os.path.isdir(c_dir):
                return search(item,c_dir)
            if os.path.isfile(c_dir) and item in c_dir:
                print c_dir

if __name__ == '__main__':
    search('test','.')
