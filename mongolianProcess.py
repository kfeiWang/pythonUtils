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


