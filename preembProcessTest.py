'''
测试
'''
import codecs
import re

def preembtestCase1(vocab_file, embed_file):
    embDict = {}
    with codecs.open(embed_file, 'r', 'utf8') as embFin:
        line = embFin.readline()
        while line:
            line = re.sub(r'\r|\n', '', line)
            lineArr = line.split()
            key = lineArr[0]
            embDict[key] = lineArr[1:]
            line = embFin.readline()
    print('预训练词典大小：', len(embDict))
    with codecs.open(vocab_file, 'r', 'utf8') as vocabFin:
        line = vocabFin.readline()
        lineIndex = 1
        while line:
            line = re.sub(r'\r|\n', '', line)
            if line == '\u180e':
                print('180e in vocab:', lineIndex)
            if line not in embDict:
                print('not in emb:', lineIndex)
                break
            line = vocabFin.readline()
            lineIndex += 1

if __name__=='__main__':
    vocab_file = 'C:\\Users\\stude\\Desktop\\DOCS\\中转\\v6WcharCut\\vocab.mo'
    embed_file = 'C:\\Users\\stude\\Desktop\\DOCS\\中转\\v6WcharCut\\vocab.emb.mo'
    preembtestCase1(vocab_file, embed_file)