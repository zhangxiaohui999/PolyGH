from collections import defaultdict

#######################得到utg.pos文件中utg的行号#######################################
def write(filePath, content):
    with open(filePath, mode='a') as f:
        f.write(content)


def getUtgDict(filePath, substr):
    utgDict = defaultdict(int)
    preUtg = None
    with open(filePath, mode='r') as f:
        for n, line in enumerate(f, start=1):
            if line.startswith(substr):
                preUtg = line[:-1]
                # return n
                utgDict[preUtg] = n
            else:
                pass
        return utgDict


if __name__ == '__main__':
    utgPath, resultLogPath = 'utg.pos', 'utg_line.log'
    findstr = '@'
    utgDict = getUtgDict(utgPath, findstr)
    print(utgDict)
    for k in utgDict:
        write(resultLogPath, '{0} {1}\n'.format(k, utgDict[k]))

