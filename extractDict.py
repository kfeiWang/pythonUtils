# -*- coding:utf8 -*-
import codecs

def genDict(sf, dicf, splitf):
    '''从测试集中提取出
        sf:源文件
        dicf:词典文件
        splitf:词典文件 字母之间以空格分开
    '''
    wordDict = {}
    with codecs.open(sf, 'r', 'utf8') as fin:
        with codecs.open(dicf, 'w', 'utf8') as dicOut:
            with codecs.open(splitf, 'w', 'utf8') as tOut:
                line = fin.readline()
                while(line):
                    line = line.strip()
                    arr = line.split(' ')
                    for word in arr:
                        wordDict[word]=1
                    line = fin.readline()
                for key in wordDict:
                    dicOut.write(key)
                    dicOut.write('\n')
                    tOut.write(' '.join(key))
                    tOut.write('\n')

                    
def replaceMN(source, saveto, nonsplitdict,splitdict):
    '''
    替换蒙古文
    source: 源文件
    saveto: 保存至文件
    nonsplitdict: 没有切词的词典
    splitdict: 切分后的词典
    '''
    wordDict = {}
    with codecs.open(saveto, 'w', 'utf8') as fout:
        with codecs.open(source, 'r', 'utf8') as mnfin:
            with codecs.open(nonsplitdict, 'r', 'utf8') as dicfin:
                with codecs.open(splitdict, 'r','utf8') as trfin:
                    line1 = dicfin.readline()
                    line2 = trfin.readline()
                    while line1 and line2:
                        line1 = line1.strip()
                        line2 = line2.strip()
                        wordDict[line1] = line2
                        line1 = dicfin.readline()
                        line2 = trfin.readline()
                    line = mnfin.readline()
                    while line:
                        line = line.strip()
                        arr = line.split(' ')
                        newline = [];
                        for word in arr:
                            newline.append(wordDict[word.strip()])
                        fout.write(' '.join(newline))
                        fout.write('\n')
                        line = mnfin.readline()
                        
def retainSuffix(splitDict, suffixNum):
    '''
    处理切词后的蒙古文，保留指定个数的词缀
    splitDict: 以空格为分隔符的词
    suffixNum: 保留的后缀数量
    '''
    if suffixNum < 0: # 异常值
        raise Exception('suffixNum:'+suffixNum+' 必须大于等于0')
    with codecs.open(splitDict, 'r', 'utf8') as sdin:
        with codecs.open(splitDict+str(suffixNum), 'w', 'utf8') as stout:
            sw = sdin.readline()
            while sw:
                sw = sw.strip() # 删除两端空白符
                swArr = sw.split() # 按照空格分开
                if len(swArr) == 0:
                    pass
                elif(len(swArr) == 1):
                    stout.write(sw)
                else:
                    snOfw = len(swArr) - 1 # 词缀的数量
                    if suffixNum >= snOfw: # 保留的词缀数量和当前词的词缀数量相等
                        stout.write(sw)
                    else:
                        stout.write(' '.join(swArr[0:suffixNum+1]))
                stout.write('\n')
                sw = sdin.readline()
    
                        
if __name__=='__main__':
    #genDict('6W/test/test.mo', '6W/test/dicf', '6W/test/splitf')
    replaceMN('6W/test/test.mo', '6W/test/test.mo0', '6W/test/dicf', '6W/test/resuDic0')
    #retainSuffix('6W/test/resuDic', 2)
