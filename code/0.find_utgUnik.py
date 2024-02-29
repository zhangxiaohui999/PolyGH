from collections import defaultdict

##########根据find_utgNum.py的结果统计的行号  得到utg的unikmer个数##################
def write(filePath, content):
    with open(filePath, mode='a') as f:
        f.write(content)


def getUtgUnikDict1(filePath):  # 得到每个utg的unikmer个数
    utgDict1 = defaultdict(int)
    preUtg = None
    with open(filePath, mode='r', encoding='utf_8') as f:
        for line in f:
            line1 = line  # 整行读取数
            line2 = next(f,None)  # 读取下一行
            if line2 is not None:
                line1_line = line1.split()
                line2_line = line2.split()
                utgDict1[line1_line[0]] = int(line2_line[1]) - int(line1_line[1]) - 1
        return utgDict1


def getUtgUnikDict2(filePath):
    utgDict1, utgDict2 = defaultdict(int), defaultdict(int)
    preUtg = None
    with open(filePath, mode='r', encoding='utf_8') as f:
        line1 = f.readline()# 整行读取数
        for line in f:
            line2 = next(f,None)  # 读取下一行
            if line2 is not None:
                line1_line = line.split()
                line2_line = line2.split()
                utgDict2[line1_line[0]] = int(line2_line[1]) - int(line1_line[1]) - 1
        return utgDict2


if __name__ == '__main__':
    utgPath1, utgPath2, resultLogPath = 'utg_line.log', 'utg_line.log','utg_unik.log'
    utgDict1, utgDict2 = defaultdict(int), defaultdict(int)
    utgDict1 = getUtgUnikDict1(utgPath1)
    utgDict2 = getUtgUnikDict2(utgPath2)
    for k in utgDict1:
        write(resultLogPath, '{0} {1}\n'.format(k, utgDict1[k]))
    for k in utgDict2:
        write(resultLogPath, '{0} {1}\n'.format(k, utgDict2[k]))

