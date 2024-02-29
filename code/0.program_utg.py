from collections import defaultdict

def write(filePath, content):
    with open(filePath, mode='a') as f:
        f.write(content)

def getUtgDict(filePath):
    myDict = {}
    with open(filePath, mode='r') as f:
        for line in f:
            splits = line.split()
            if len(splits) == 1:
                preUtg = splits[0]
            else:
                myDict[splits[1]] = preUtg
    return myDict

def getUtg(readDict):
    utg, maxUtg = None, 0
    for k in readDict:
        (utg, maxUtg) = (k, readDict[k]) if readDict[k] > maxUtg else (utg, maxUtg)
    return utg

def deelPreItem(preRead, readDict, fileType, matchDict, resultDict):
    utg = getUtg(readDict)
    if fileType == 'reads1':
        matchDict[preRead] = utg
    else:
        r1 = preRead.replace('/2', '/1')
        if r1 in matchDict:  
            lstTmp = [matchDict[r1], utg]
            write(reads2LogPath, preRead + ' ' + utg + '\n')
            if lstTmp[0] != lstTmp[1]:
                lstTmp.sort()
                #write(reads2LogPath, preRead + ' ' + utg + '\n')
                resultDict[mySplit.join(lstTmp)] += 1

def deelReadFile(filePath, matchDict, fileType, resultDict=None):
    readDict = defaultdict(int)
    preRead = None
    with open(filePath, mode='r') as f:
        for line in f:
            splits = line.split()
            if len(splits) == 1:
                if preRead != None and len(readDict) != 0:
                    deelPreItem(preRead, readDict, fileType, matchDict, resultDict)
                preRead = splits[0]
                readDict.clear()
            else:
                if splits[1] in myDict:
                    theUtg = myDict[splits[1]]
                    readDict[theUtg] += 1
    if len(readDict) != 0:
        deelPreItem(preRead, readDict, fileType, matchDict, resultDict)
    readDict.clear()

if __name__ == '__main__':
    mySplit, utgPath, reads1Path, reads2Path, reads1LogPath, reads2LogPath, resultLogPath = '`?`', 'utg.pos', 'reads1.pos', 'reads2.pos', 'reads1.log', 'reads2.log', 'result.log'
    myDict,resultDict,matchDict = getUtgDict(utgPath),defaultdict(int),{}
    deelReadFile(reads1Path, matchDict, 'reads1', resultDict)
    for k in matchDict:
        write(reads1LogPath, '{0} {1}\n'.format(k, matchDict[k]))
    deelReadFile(reads2Path, matchDict, 'reads2', resultDict)
    for utgMapping, num in sorted(resultDict.items(), key=lambda kv: (-kv[1], kv[0])):
        write(resultLogPath, '{0} {1} {2} \n'.format(utgMapping.split(mySplit)[0], utgMapping.split(mySplit)[1], num))
