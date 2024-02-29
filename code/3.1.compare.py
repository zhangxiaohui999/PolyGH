import re


def write(filePath, content):
    with open(filePath, mode='a') as f:
        f.write(content)



# utg_group_310.txt
def format0(standardFile, standardFileFormat):
    with open(standardFile, 'r') as fr, \
            open(standardFileFormat, 'w') as fw:

        lines = fr.readlines()
        for line in lines:
            splits = line.strip().split()
            utgName = splits[0] + '_' + splits[1] + '_' + splits[2]
            fw.write(utgName + '\t' + splits[-3] + '\t' + splits[-2] + '\t' +
                     splits[-1] + '\n')


# utg_group_717.txt
def format1(standardFile, standardFileFormat):
    with open(standardFile, 'r') as fr, \
            open(standardFileFormat, 'w') as fw:

        lines = fr.readlines()
        for line in lines:
            splits = line.strip().split()
            utgName = splits[0] + '_' + splits[1] + '_' + splits[2]
            fw.write(utgName + '\t' + splits[-3] + '\t' + splits[-2] + '\t' +
                     splits[-1] + '\n')


def saveDict(addTwoFileFormat,standardFileFormat,compareFile,addTwoFile_diff,standardFile_diff):
    standardDict = {}
    addTwoDict = {}
    with open(addTwoFileFormat, 'r') as fr1, \
            open(standardFileFormat, 'r') as fr2:
        # addTwo
        lines = fr1.readlines()
        for line in lines:
            splits = line.strip().split('\t')
            utgName = splits[0]
            utgType = splits[1]
            utgGroup = splits[2]
            utgList = splits[3].split(',')
            utgList.sort()
            addTwoDict[utgName] = {utgType: {utgGroup: utgList}}

        # standard
        lines = fr2.readlines()
        for line in lines:
            splits = line.strip().split('\t')
            utgName = splits[0]
            utgType = splits[1]
            utgGroup = splits[2]
            utgList = splits[3].split(',')
            utgList.sort()
            standardDict[utgName] = {utgType: {utgGroup: utgList}}

        with open(compareFile, 'w') as fw1,\
                open(addTwoFile_diff, 'w') as fw2,\
                    open(standardFile_diff, 'w') as fw3:
            # 遍历两个字典，比较字典内容
            for key in addTwoDict:
                if key in standardDict:
                    if addTwoDict[key] != standardDict[key]:
                        fw1.write("{}: {} is different from {}\n".format(key, addTwoDict[key], standardDict[key]))
                        for key_type in addTwoDict[key]:
                            for key_Group in addTwoDict[key][key_type]:
                                fw2.write("{}\t{}\t{}\t{}\n".format(key,key_type,key_Group,','.join(addTwoDict[key][key_type][key_Group])))
                            for key_Group in standardDict[key][key_type]:
                                fw3.write("{}\t{}\t{}\t{}\n".format(key, key_type, key_Group, ','.join(standardDict[key][key_type][key_Group])))
                else:
                    fw1.write("{} is not in standardDict".format(key))

            for key in standardDict:
                if key not in addTwoDict:
                    fw1.write("{} is not in addTwoDict".format(key))


def compareDict(addTwoFileFormat, standardFileFormat, compareFile,
                addTwoFile_diff, standardFile_diff):
    addTwoDict = {}
    standardDict = {}
    standard_SizeDict = {}
    with open(addTwoFileFormat, 'r') as fr1, \
            open(standardFileFormat, 'r') as fr2:
        # addTwo
        lines = fr1.readlines()
        for line in lines:
            splits = line.strip().split('\t')
            utgName = splits[0]
            utgType = splits[1]
            utgGroup = splits[2]
            utgList = splits[3].split(',')
            utgList.sort()
            addTwoDict[utgName] = {utgType: {utgGroup: utgList}}

        # standard
        lines = fr2.readlines()
        for line in lines:
            splits = line.strip().split('\t')
            utgName = splits[0]
            utgType = splits[1]
            utgGroup = splits[2]
            utgList = splits[3].split(',')
            utgList.sort()
            standardDict[utgName] = {utgType: {utgGroup: utgList}}

            splits_utgName = utgName.split('_')
            utgSize = int(splits_utgName[3]) - int(splits_utgName[2]) + 1
            standard_SizeDict[utgName] = utgSize

    with open(compareFile, 'w') as fw1,\
                open(addTwoFile_diff, 'w') as fw2,\
                    open(standardFile_diff, 'w') as fw3:
        # 11-addTwoDict 22-standardDict

        sum = 0
        hapNum = 1
        dipNum = 2
        tripNum = 3
        tetrapNum = 4
        for key_utg in addTwoDict:
            if key_utg in standardDict:
                if addTwoDict[key_utg] != standardDict[key_utg]:
                    fw1.write("{}: {} is different from {}\n".format(
                            key_utg, addTwoDict[key_utg], standardDict[key_utg]))
                    for key_type in addTwoDict[key_utg].keys():
                        for key_Group1 in addTwoDict[key_utg][key_type]:
                            for key_Group2 in standardDict[key_utg][key_type]:
                                if key_Group1 != key_Group2:
                                    if key_type == 'hap':
                                        sum += standard_SizeDict[key_utg]
                                    elif key_type == 'dip':
                                        sum += (standard_SizeDict[key_utg]) * 2
                                    elif key_type == 'trip':
                                        sum += (standard_SizeDict[key_utg]) * 3
                                    elif key_type == 'tetrap':
                                        sum += (standard_SizeDict[key_utg]) * 4
                                elif key_Group1 == key_Group2:
                                    inter_List = set(
                                        addTwoDict[key_utg][key_type]
                                        [key_Group1]).intersection(
                                            set(standardDict[key_utg][key_type]
                                                [key_Group2]))
                                    if key_type == 'hap':
                                        sum += (standard_SizeDict[key_utg] *
                                                (hapNum - len(inter_List)))
                                    elif key_type == 'dip':
                                        sum += (standard_SizeDict[key_utg] *
                                                (dipNum - len(inter_List)))
                                    elif key_type == 'trip':
                                        sum += (standard_SizeDict[key_utg] *
                                                (tripNum - len(inter_List)))
                                    elif key_type == 'tetrap':
                                        sum += (standard_SizeDict[key_utg] *
                                                (tetrapNum - len(inter_List)))

                            for key_Group1 in addTwoDict[key_utg][key_type]:
                                fw2.write("{}\t{}\t{}\t{}\t{}\n".format(
                                    key_utg, key_type, key_Group1,
                                    ','.join(addTwoDict[key_utg][key_type]
                                             [key_Group1]), sum))
                            for key_Group2 in standardDict[key_utg][key_type]:
                                fw3.write("{}\t{}\t{}\t{}\t{}\n".format(
                                    key_utg, key_type, key_Group2,
                                    ','.join(standardDict[key_utg][key_type]
                                             [key_Group2]), sum))
                sum = 0

            else:
                    fw1.write("{} is not in standardDict\n".format(key_utg))

        for key_utg in standardDict:
            if key_utg not in addTwoDict:
                fw1.write("{} is not in addTwoDict\n".format(key_utg))

    
if __name__ == '__main__':
    standard310File, standard310FileFormat = 'utg_group_260.txt', 'utg_group_260_format.txt'
    standardFile, standardFileFormat = 'utg_group_717.txt', 'utg_group_717_format.txt'
    compareFile,addTwoFile_diff,standardFile_diff='diff1.compare.260.txt','diff1.addTwo.260.txt','diff1.standard.260.txt'
    
    format0(standard310File,standard310FileFormat)
    # format1(standardFile,standardFileFormat)
    compareDict(standard310FileFormat, standardFileFormat, compareFile,
                addTwoFile_diff, standardFile_diff)