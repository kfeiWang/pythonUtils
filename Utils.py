'''
基本工具方法
'''
import os
import codecs
import re

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
    split2Char('ch.txt')