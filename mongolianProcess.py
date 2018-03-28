'''
author: hongbinWang
date:2018年3月28日08:34:09
功能蒙古文文本简单处理
'''

import re
import codecs

def delNonMonWord(line):
    '''
    删除一行中的含有非蒙古文word
    '''
    if line and len(line) > 0:
        wordArr = line.split()
        newLine = []
        for i in range(len(wordArr)):
            word = wordArr[i]
            searchObj = re.search(r'[\u4e00-\u9fa5]', word) # 剔除汉字
            if searchObj:
                continue
            searchObj = re.search(r'[0-9a-zA-Z]', word) # 剔除数字英文字母
            if searchObj:
                continue
            newLine.append(word)
        return newLine
    return None

def cutWordNNModel(cuttedMonVoc, monVoc, nMonVoc)
    '''
    cuttedMonVoc: 切分后的蒙古文词典
    monVoc: 蒙古文词典
    nMonVoc: 新文件保存位置
    为了消除神经网络切词模型翻译时造成的错误，这里通过比较切词标志
    符合“\”的位置来加入到原词典中对应的位置
    '''
    with codecs.open(cuttedMonVoc, 'r', 'utf8') as cmv:
        with codecs.open(monVoc, 'r', 'utf8') as mv:
            with codecs.open(nMonVoc, 'w', 'utf8') as fout:
                cuttedWord = cmv.readline()
                mword = mv.readline()
                while mword:
                    cuttedWord = cuttedWord.replace('\n', '')
                    mword = mword.replace('\n', '')
                    nmword = [] # 新词
                    cuttedWordIndex = 0
                    for i in range(len(mword))
                        if(cuttedWord[cuttedWordIndex] == '/'):
                            nmword.append('/')
                            cuttedWordIndex += 1
                        nmword.append(mword[i])
                        cuttedWordIndex += 1
                    cuttedWord = cmv.readline()
                    mword = mv.readline()
                    fout.write(''.join(nmword))
                    fout.write('\n')
