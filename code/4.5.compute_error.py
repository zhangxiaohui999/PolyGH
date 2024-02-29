import re


def write(filePath, content):
    with open(filePath, mode='a') as f:
        f.write(content)


# utg_group_310_hic.txt
def data_list(addTwoFile, addTwoFileFormat):
    with open(addTwoFile, 'r') as fr, \
            open(addTwoFileFormat, 'w') as fw:
        lines = fr.readlines()
        for line in lines:
            splits = line.strip().split()
            utgName = splits[0]
            utgType = splits[1][3:]
            x1 = splits[2].find('(')
            x2 = splits[2].find(')')
            utgGroup = splits[2][2:x1]
            # utgList = splits[2][x1 + 1:x2].split(',')[:]
            utgList = splits[2][x1 + 1:x2]
            List = re.findall(r"\d+\.?\d*", utgList)  # ['7','21']
            List_new = ','.join(List)
            fw.write(utgName + '\t' + utgType + '\t' + utgGroup + '\t' +
                     List_new + '\n')


# utg_group_717.txt
def format(standardFile, standardFileFormat):
    with open(standardFile, 'r') as fr, \
            open(standardFileFormat, 'w') as fw:

        lines = fr.readlines()
        for line in lines:
            splits = line.strip().split()
            utgName = splits[0] + '_' + splits[1] + '_' + splits[2]
            fw.write(utgName + '\t' + splits[-3] + '\t' + splits[-2] + '\t' +
                     splits[-1] + '\n')


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


def group_error(diff_addTwo,result,result1):
    utg_SizeDict = {}
    utg_G_SizeDict = {}
    G_ErrorSizeDict = {}
    Group_SizeDict = {}
    with open(diff_addTwo, 'r') as fr1,open(result, 'w') as fw1,open(result1, 'w') as fw2:
        lines = fr1.readlines()
        for line in lines:
            splits = line.strip().split('\t')
            utgName = splits[0]
            utgType = splits[1]
            utgGroup = splits[2]
            utgErrorSize = splits[-1]
            utg_G_SizeDict[utgName] = {utgType: {utgGroup: utgErrorSize}}

            splits_utgName = utgName.split('_')
            utgSize = int(splits_utgName[3]) - int(splits_utgName[2]) + 1
            utg_SizeDict[utgName] = utgSize

            if utgGroup not in G_ErrorSizeDict.keys():
                G_ErrorSizeDict[utgGroup] = [utgErrorSize]
            else:
                G_ErrorSizeDict[utgGroup].append(utgErrorSize)

        groupSize = 0
        for utgGroup in G_ErrorSizeDict.keys():
            for size in G_ErrorSizeDict[utgGroup]:
                groupSize += int(size)
            Group_SizeDict[utgGroup] = groupSize
            groupSize = 0

        for key in G_ErrorSizeDict.keys():
            fw1.write(key+'\t'+str(Group_SizeDict[key])+'\n')


        groupSize = 0
        for utgGroup in G_ErrorSizeDict.keys():
            for size in G_ErrorSizeDict[utgGroup]:
                groupSize += int(size)
            Group_SizeDict[utgGroup] = groupSize
            #groupSize = 0

        for key in G_ErrorSizeDict.keys():
            fw2.write(key+'\t'+str(Group_SizeDict[key])+'\n')

            
if __name__ == '__main__':
    addTwoFile, addTwoFileFormat = 'utg_group_350_add.txt', 'utg_group_350_add.format.txt'
    standardFile, standardFileFormat = 'utg_group_717.txt', 'utg_group_717_format.txt'
    compareFile,addTwoFile_diff,standardFile_diff='diff1.compare.txt','diff1.addTwo.txt','diff1.standard.txt'
    result_1, result_2 = 'result_0.txt', 'result_1.txt'
    data_list(addTwoFile,addTwoFileFormat)
    format(standardFile,standardFileFormat)
    compareDict(addTwoFileFormat, standardFileFormat, compareFile,
                addTwoFile_diff, standardFile_diff)
    
    group_error(addTwoFile_diff,result_1,result_2)