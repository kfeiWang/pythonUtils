'''
基本工具方法
'''
import os
import codecs
import codecs

def split2Char(fileName, separator=' '):
    '''
    将文件中内容按照字符分割
    :param fileName:
    :param separator: 分割符, default=' '
    :return:
    '''
    outFileName = os.path.join(fileName, '.char')
    with codecs.open(outFileName, 'w', 'utf8') as fout:
        with codecs.open(fileName, 'r', 'utf8') as fin:
            line = fin.readline()
            while line:
                line = fin.readline()