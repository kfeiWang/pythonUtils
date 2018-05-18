'''
处理Unicode字符相关
'''
import re
import os

def delUserPriverateCode(text, repCode = ' '):
    '''
    text: 待处理字符串
    repCode: 将私有字符串替换为的字符，默认为空格
    将text中unicode中用户私有区域字符替换
    删除区域目前包括如下：\uE000-\uF8FF
    后续可能会添加其它区域处理
    '''
    if text:
        text = re.sub(r'[\uE000-\uF0FF]+', repCode, text)
    return text

def delSymbol(text):
    '''
    删除标点符号
    '''
    if text:
        text = re.sub(r'', ' ', text)
    return text

def delSpace2EndMulSpace(text):
    '''
    删除text两端空白字符，替换文本中多个空格为1个
    '''
    if text:
        text = text.strip()
        text = re.sub(r'\s+', ' ', text)
    return text

if __name__=='__main__':
    delUserPriverateCode('')
