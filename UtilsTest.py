'''
测试用
'''

import re

def split2Space():
    text = 'ab中过'
    pattern = re.compile('.{1,1}')
    textp = ' '.join(pattern.findall(text))
    print(text)
    print(textp)

if __name__=='__main__':
    split2Space()