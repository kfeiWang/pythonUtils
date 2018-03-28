'''
mongolianProcess相关函数测试文件
'''
from mongolianProcess import *
def delNonMonWordTestCases():
    okCount = 0 # 测试用例成功计数器
    fatalCount = 0 # 测试用例失败计数器
    def case1():
        line = ''
        refLine = ''
        resu = delNonMonWord(line)
        if resu == refLine:
            print('OK')
            global okCount += 1
        else:
            print('fatal')
            global fatalCount += 1
    case1()
    print('success cases count is:', okCount)
    print('fail case count is:', fatalCount)