# -*- coding:utf8 -*-
from __future__ import division
import codecs

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
        while line:
            line = line.strip() # 删除两端空白符
            wArr = line.split('\t')
            if len(wArr) != 2:
                continue
            key = wArr[0] # 源语言词
            val = wArr[1] # 目标语言词
            if key in wordDic:
                wordDic[key].append(val)
            else:
                valList = []
                valList.append(val)
                wordDic[key] = valList
            line = fin.readline()
    with codecs.open(outfile, 'w', 'utf8') as fout:
        for key in wordDic.keys():
            valList = wordDic[key]
            valLen = len(valList)
            for val in valList:
                fout.write(key)
                fout.write('\t')
                fout.write(val)
                fout.write('\t')
                fout.write(str(1/valLen))
                fout.write('\n')

if __name__ == '__main__':
    calWordProbability('E:/laboratory/ljt/dict.txt', 'E:/laboratory/ljt/dictProb.txt')                
