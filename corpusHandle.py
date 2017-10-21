# -*- coding:utf8 -*-
from __future__ import division
import codecs
import re

def setASubSetB(file1, file2, outFile):
    '''
    求两个文件的差集，属于file1，并且不属于file2
    原理：将两个文件中内容均读入到内存中，利用python set 数据结构进行集合减法运算
    缺点：不适合大文件处理
    file1: 文件1
    file2: 文件2
    outFile: 结果输出文件
    '''
    with codecs.open(file1, 'r', 'utf8') as fin1:
        with codecs.open(file2, 'r', 'utf8') as fin2:
            with codecs.open(outFile, 'w', 'utf8') as fout:
                set1 = set()
                set2 = set()
                line1 = fin1.readline()
                while line1:
                    set1.add(line1)
                    line1 = fin1.readline()
                line2 = fin2.readline()
                while line2:
                    set2.add(line2)
                    line2 = fin2.readline()
                s3 = set1 - set2
                for val in s3:
                    fout.write(val)

if __name__ == '__main__':
    setASubSetB('testData/src.txt', 'testData/test.txt', 'testData/resu.txt')