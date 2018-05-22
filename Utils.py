'''
基本工具方法
'''
import os
import codecs
import re

def restoreFromMid(fileName, midFileName):
    with codecs.open(fileName, 'r', 'utf8') as fin:
        with codecs.open(midFileName, 'r', 'utf8') as mfin:
            with codecs.open(fileName+'.rs', 'w', 'utf8') as rsfout:
                li = mfin.readline()
                preLi = li
                line = fin.readline()
                while line and li:
                    li = li.strip()
                    line = line.strip()

                    li = int(li)
                    preLi = int(preLi)

                    if li != preLi:
                        rsfout.write('\n')
                    rsfout.write(line)
                    
                    preLi = li
                    li = mfin.readline()
                    line = fin.readline()


def splitSensSearch(fileName):
    '''
    @param fileName 拆分句子
    '''
    sepDict = {' ᠂':1, ' ᠃':1, ' ︖':1}
    with codecs.open(fileName, 'r', 'utf8') as fin:
        with codecs.open(fileName+'.mid', 'w', 'utf8') as mfout:
            with codecs.open(fileName+'.resu', 'w', 'utf8') as rfout:
                line = fin.readline()
                lineIndex = 1
                while line:
                    line = line.strip()
                    subLine = []
                    for a in line:
                        subLine.append(a)
                        if a in sepDict.keys():
                            mfout.write(str(lineIndex))
                            mfout.write('\n')
                            rfout.write(''.join(subLine))
                            rfout.write('\n')
                            subLine.clear()
                    if len(subLine) > 0:
                        mfout.write(str(lineIndex))
                        mfout.write('\n')
                        rfout.write(''.join(subLine))
                        rfout.write('\n')
                        subLine.clear()
                    lineIndex += 1
                    line = fin.readline()

def splitSensRE(fileName):
    '''
    @param fileName 拆分句子
    '''

    with codecs.open(fileName, 'r', 'utf8') as fin:
        with codecs.open(fileName+'.mid', 'w', 'utf8') as mfout:
            with codecs.open(fileName+'.resu', 'w', 'utf8') as rfout:
                line = fin.readline()
                lineIndex = 1
                while line:
                    line = line.strip()
                    lineArr = re.split(r'[;.?]', line)
                    for subLine in lineArr:
                        mfout.write(str(lineIndex))
                        mfout.write('\n')
                        rfout.write(subLine)
                        rfout.write('\n')
                    lineIndex += 1
                    line = fin.readline()

def split2Char(fileName, separator=' '):
    '''
    将文件中内容按照字符分割
    :param fileName:
    :param separator: 分割符, default=' '
    :return:
    '''
    with codecs.open(fileName+'.char', 'w', 'utf8') as fout:
        with codecs.open(fileName, 'r', 'utf8') as fin:
            line = fin.readline()
            while line:
                line = line.strip()
                lineArr = list(line)
                outline = separator.join(lineArr)
                outline = re.sub(r' {2,}', ' ', outline)
                fout.write(outline)
                fout.write('\n')
                line = fin.readline()

if __name__ == '__main__':
    #split2Char('G:/labotratory/cwmt2017/valid.clean.mo')
    splitSensSearch('splitSens.txt')
    restoreFromMid('splitSens.txt.resu', 'splitSens.txt.mid')