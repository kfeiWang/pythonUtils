'''
预训练词向量生成新词向量
'''
import codecs
import re
import numpy as np

def packageNewEmb(preEmbFileName, vocabFileName):
    '''
    preEmbFileName: 预训练的词向量
    vocabFileName: 词典文件
    '''
    with codecs.open(preEmbFileName, 'r', 'utf8') as preFin:
        with codecs.open(vocabFileName, 'r', 'utf8') as vocFin:
            with codecs.open(vocabFileName+'.emb', 'w', 'utf8') as fout:
                # 1. 读入预训练的词向量
                preEmb = {} # key:wordPiece value:[embedding value]
                line = preFin.readline()
                while line:
                    line = re.sub(r'\r|\n', '', line)
                    lineArr = line.split()
                    preEmb[lineArr[0]] = np.array(lineArr[1:], dtype='float32')
                    line = preFin.readline()

                # 2. 用预训练的词向量组装新词向量
                word = vocFin.readline()
                while word:
                    word = word.split('\t')[0]
                    word = re.sub(r'\r|\n', '', word)
                    # wordEmb = np.zeros((512,) dtype='float32')
                    wordEmb = [preEmb[char] for char in word]
                    wordEmb = np.array(wordEmb, dtype='float32')
                    wordEmb = np.mean(wordEmb, axis=0)
                    fout.write(word)
                    fout.write(' ')
                    fout.write(' '.join([str(emb) for emb in wordEmb]))
                    fout.write('\n')
                    word = vocFin.readline() 

if __name__=='__main__':
    embFileName = 'C:\\Users\\stude\\Desktop\\DOCS\\中转\\v6WcharCut\\v6WcharCutVocab\\mo.char.emb'
    newEmbFileName = 'C:\\Users\\stude\\Desktop\\DOCS\\中转\\v6WcharCut\\vocab.mo'
    packageNewEmb(embFileName, newEmbFileName)