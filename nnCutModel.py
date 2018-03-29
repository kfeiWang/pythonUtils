'''
神经网络切词模型相关处理
'''

import codecs
import re

def replaceVoc(cuttedMonVoc, monVoc, nMonVoc):
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
                    cuttedWord = cuttedWord.replace('<unk>', '2') # 将unk替换为一个单一的字符，这里选择2
                    mword = mword.replace('\n', '')
                    nmword = [] # 新词
                    cuttedWordIndex = 0
                    for i in range(len(mword)):
                        if cuttedWordIndex < len(cuttedWord):
                            if(cuttedWord[cuttedWordIndex] == '/'):
                                nmword.append('/')
                                cuttedWordIndex += 1
                        nmword.append(mword[i])
                        cuttedWordIndex += 1
                    fout.write(mword)
                    fout.write(' ')
                    fout.write(''.join(nmword))
                    fout.write('\n')

                    cuttedWord = cmv.readline()
                    mword = mv.readline()
                
def replaceMonInFile(monFile, nmonFile, midVoc):
    '''
    monFile:蒙文语料文件
    midVoc:中间词典
    nmonFile:新蒙问语料文件
    '''
    midDict = {}
    with codecs.open(midVoc, 'r', 'utf8') as mdFin:
        line = mdFin.readline()
        while line:
            line = re.sub(r'\r|\n', '', line)
            line = mdFin.readline()
            lineArr = line.split()
            for i in range(len(lineArr)):
                midDict[lineArr[0]] = lineArr[1]
            line = mdFin.readline()
    with codecs.open(monFile, 'r', 'utf8') as fin:
        with codecs.open(nmonFile, 'w', 'utf8') as fout:
            line = fin.readline()
            while line:
                line = re.sub(r'\r|\n', '', line)
                lineArr = line.split()
                nline = []
                for i in range(len(lineArr)):
                    key = lineArr[i]
                    if key in midDict:
                        nline.append(midDict[key])
                    else:
                        nline.append(key)
                fout.write(' '.join(nline))
                fout.write('\n')
                line = fin.readline()

if __name__ == '__main__':
    fpath = 'C:\\Users\\stude\\Desktop\\DOCS\\中转\\v6Wchar'
    #replaceVoc(fpath+'/vocab.resu', fpath+'/vocab.mo', fpath+'/nvocab.mo')
    replaceMonInFile(fpath+'/train.clean.mo', fpath+'/ntrain.clean.mo', fpath+'/nvocab.mo')
    replaceMonInFile(fpath+'/valid.clean.mo', fpath+'/nvalid.clean.mo', fpath+'/nvocab.mo')
    replaceMonInFile(fpath+'/test.clean.mo', fpath+'/ntest.clean.mo', fpath+'/nvocab.mo')