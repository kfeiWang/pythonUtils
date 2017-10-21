# -*- coding:utf8 -*-
from __future__ import division
import codecs
import re

def calWordProbability(infile, outfile):
    '''
    计算词概率，源语言词翻译成目标语言词的概率
    一个源语言可能对应多个目标语言，这里计算平均值
    infile: 输入文件 格式：source word \t  target word
    outfile: source word \t  target word \t probability
    '''
    with codecs.open(infile, 'r', 'utf8') as fin:
        # 用于存储数据结构
        wordDic = {}
        line = fin.readline()
        linNum = 1
        while line:
            linNum += 1
            if linNum % 10001 == 1:
                print(linNum, line.encode('utf8'))
            line = line.strip() # 删除两端空白符
            wArr = re.split('[ |\t]', line)

            if len(wArr) >= 2:
                key = wArr[0] # 源语言词
                val = wArr[1] # 目标语言词
                if key in wordDic:
                    wordDic[key][val] = 1
                else:
                    valMap = dict()
                    valMap[val] = 1
                    wordDic[key] = valMap
            line = fin.readline()
    with codecs.open(outfile, 'w', 'utf8') as fout:
        print('start write')
        wCount = 0
        for key in wordDic.keys():
            wCount += 1
            if(wCount % 1001 == 0):
                print('writing', wCount)
            if len(key.split(' ')) > 1:
                continue
            valMap = wordDic[key]
            valLen = len(valMap)
            for val in valMap.keys():
                fout.write(key)
                fout.write('\t')
                fout.write(val)
                fout.write('\t')
                fout.write(str(1/valLen))
                fout.write('\n')
                
