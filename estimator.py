# -*- coding:utf8 -*-

from __future__ import print_function

import codecs

def caluPAndRAndF1(file1, file2):
    '''
    计算准确率p和召回率r,f1值
    file1: 参考文件
    file2: 处理后文件
    '''
    with codecs.open(file1, 'r', 'utf8') as fin1:
        with codecs.open(file2, 'r', 'utf8') as fin2:
            line1 = fin1.readline()
            line2 = fin2.readline()
            totalWordCount = 0
            rightWordCount = 0
            splitWordCount = 0
            while line1 and line2:
                line1Arr = line1.strip().split(' ')
                line2Arr = line2.strip().split(' ')
                if len(line1Arr) != len(line2Arr):
                    raise Exception('句子词数量不一致')
                for w1, w2 in zip(line1Arr, line2Arr): # 循环对应句子中每个词
                    set1 = packSet(w1) # 将word以/切分后放入集合
                    set2 = packSet(w2) # 将word以/切分后放入集合
                    #print('w1:', w1, len(set1), 'set1:', set1, 'w2', w2, len(set2), 'set2:', set2)
                    totalWordCount += len(set1) # 参考文件中全部词片段数量
                    splitWordCount += len(set2) # 切分后全部词片段数量
                    rightWordCount += len(set1.intersection(set2)) # 参考文件词片段和切分后全部词片段交集
                line1 = fin1.readline()
                line2 = fin2.readline()
    p = rightWordCount*1.0/totalWordCount # 计算准确率
    r = rightWordCount*1.0/splitWordCount # 计算召回率
    f1 = p*r*2/(p+r) # 计算f1值
    return p,r,f1

def packSet(word):
    '''
    word:以/划分
    '''
    setR = set()
    wArr = word.split('/')
    for w in wArr:
        setR.add(w)
    return setR

def testCaseCaluPAndRAndF1():
    p,r,f1 = caluPAndRAndF1('testData/srcFile', 'testData/splitFile')
    print('p:', p, 'r:', r, 'f1:', f1)

if __name__=='__main__':
    testCaseCaluPAndRAndF1()