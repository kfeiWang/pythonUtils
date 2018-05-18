'''
author: hongbinWang
date:2018年3月28日08:34:09
功能蒙古文文本简单处理
'''

import re
import codecs
import os

path = 'C:\\Users\\stude\\Desktop\\DOCS\\中转\\20w+\\'

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

def statisticalSenLen(fileName):
    '''
    统计fileName句子的字符数量
    '''
    with codecs.open(fileName+'.statis', 'w', 'utf8') as fout:
        with codecs.open(fileName, 'r' ,'utf8') as fin:
            line = fin.readline()
            lineTotalLen = 0 # 记录句子总的字符数量
            lineCount = 0 # 句子数量
            lineIndex = 1
            wordCount = 0 # word数量
            while line:
                wordCount += len(line.split(' '))
                line = re.sub(r'\s+', '', line) # 删除句子中的空白符
                lineLen = len(line)
                fout.write('%d'%lineIndex)
                fout.write(' ')
                fout.write('%d'%lineLen)
                fout.write('\n')
                lineTotalLen += lineLen
                lineCount += 1
                line = fin.readline()
                lineIndex += 1
            print('句子总数：%d' %(lineCount))
            print('平均每句字符数：', lineTotalLen/lineCount)
            print('平均字数量：', wordCount/lineCount)

def extractUNKSens(vocFileName, moFileName, chFileName):
    '''
    给定词典和语料，统计语料中UNK数量，即语料中词不在词典中的数量
    '''
    voc = {} # 词典
    with codecs.open(vocFileName, 'r', 'utf8') as vfin:
        line = vfin.readline()
        while line:
            line = re.sub(r'\s+', '', line)
            voc[line] = 1
            line = vfin.readline()
    
    totalToken = 0 # 总字符数
    unkToken = 0 # unk字符数
    unkSens = 0 # 输出句子数
    with codecs.open(path+'unkTest.clean.ch', 'w', 'utf8') as cfout:
        with codecs.open(path+'unkTest.clean.mo', 'w', 'utf8') as mfout:
            with codecs.open(chFileName, 'r', 'utf8') as cfin:
                with codecs.open(moFileName, 'r', 'utf8') as mfin:
                    mline = mfin.readline()
                    cline = cfin.readline()
                    while mline:
                        mlineArr = mline.split()
                        hasUNK = False
                        senUNK = 0
                        if len(mlineArr) < 30:
                            for word in mlineArr:
                                word = re.sub(r'\s+', '', word)
                                if len(word) <= 0:
                                    continue
                                if word not in voc:
                                    unkToken += 1
                                    senUNK += 1
                                    hasUNK = True
                            if senUNK >= 2 and senUNK <= 5:
                                totalToken += len(mlineArr)
                                cfout.write(cline)
                                #cfout.write('\n')
                                mfout.write(mline)
                                #mfout.write('\n')
                                unkSens += 1
                            if unkSens >= 1000:
                                break
                        mline = mfin.readline()
                        cline = cfin.readline()

    print('总token数量：', totalToken)
    print('unk token数量：', unkToken)
    print('unk Percent%:', unkToken/totalToken)

def statisUNKNum(vocFileName, moFileName):
    '''
    给定词典和语料，统计语料中UNK数量，即语料中词不在词典中的数量
    '''
    voc = {} # 词典
    with codecs.open(vocFileName, 'r', 'utf8') as vfin:
        line = vfin.readline()
        while line:
            line = re.sub(r'\s+', '', line)
            voc[line] = 1
            line = vfin.readline()
    
    totalToken = 0 # 总字符数
    unkToken = 0 # unk字符数
    with codecs.open(moFileName, 'r', 'utf8') as fin:
        line = fin.readline()
        while line:
            lineArr = line.split()
            for word in lineArr:
                word = re.sub(r'\s+', '', word)
                if len(word) <= 0:
                    continue
                totalToken += 1
                if word not in voc:
                    unkToken += 1
            line = fin.readline()
    print('总token数量：', totalToken)
    print('unk token数量：', unkToken)
    print('unk Percent%:', unkToken/totalToken)

if __name__=='__main__':
    #statisticalSenLen('C:\\Users\\stude\\Desktop\\DOCS\\中转\\6Wword\\train.clean.mo')
    #statisUNKNum(os.path.join(path, 'vocab.mozh-mo.35000'), os.path.join(path, 'test.clean.mo'))
    extractUNKSens(os.path.join(path, 'vocab.mozh-mo.35000'), os.path.join(path, 'newTest3.clean.mo.bpe'), os.path.join(path, 'train.clean.ch'))
