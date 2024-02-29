from collections import defaultdict
import re
import pandas


def write(filePath, content):
    with open(filePath, mode='a') as f:
        f.write(content)


# ————1————
# utg000005l_pilon_1_10000  in  list1 的single关系:  utg000005l_pilon_1_10000 utg000001l_pilon 0.5649326828660307
# 定义一个函数，用于读取文件内容并返回一个字典,对于每个字典，按键从大到小排序并输出第一个键和值
def findList_one(fr, fw):
    utglist_dict = {}
    with open(fr, 'r') as fr, \
            open(fw, 'w') as fw:
        lines = fr.readlines()
        for line in lines:
            splits = line.strip().split()
            willUtgName = splits[0]
            listName = splits[2]
            suppUtg = splits[-2]
            utgRelation_line = '  '.join(splits[-3:]) + '\n'
            utgWeight = round(float(splits[-1]), 16)

            # if willUtgName not in utglist_dict.keys():
            #     utglist_dict[willUtgName] = {
            #     }
            # else:
            #     if listName not in utglist_dict[willUtgName].keys():
            #         utglist_dict[willUtgName][listName] = {}
            #     else:
            #         utglist_dict[willUtgName][listName].update({utgRelation_line: utgWeight})
            # print(utglist_dict)
            
            if willUtgName not in utglist_dict.keys():
                utglist_dict[willUtgName] = {listName: {utgRelation_line: utgWeight}}
            else:
                if listName not in utglist_dict[willUtgName].keys():
                    utglist_dict[willUtgName][listName] = {utgRelation_line: utgWeight}
                else:
                    utglist_dict[willUtgName][listName].update({utgRelation_line: utgWeight})
        # print(utglist_dict)
        # {'utg000005l_pilon_1_10000': {'list1': {'utg000005l_pilon_1_10000  utg000070l_pilon  0.5248186678958373\n': 0.5248186678958373,...
        # 对于每个字典，按键从大到小排序并输出第一个键和值
        for willUtgName in utglist_dict.keys():
            for utgList in utglist_dict[willUtgName].keys():
                # sorted_keys = sorted(utglist_dict[willUtgName][utgList],
                #                     key=lambda x: utglist_dict[willUtgName][utgList][x], reverse=True)
                # utgRelation_line = sorted_keys[0]
                # utgWeight = utglist_dict[willUtgName][utgList][utgRelation_line]

                utgRelation_line = list(utglist_dict[willUtgName][utgList])[0]
                # print(utgRelation_line)
                fw.write(f'{willUtgName} in {utgList} : {utgRelation_line}')


# ————3————
# 归一化
# 这个函数最后输出文件需要处理
def normalized(single_List_file, single_tmpList_file, single_lastList_file):
    group_size = 48

    with open(single_List_file, 'r', encoding='utf-8') as f, \
            open(single_tmpList_file, 'w', encoding='utf-8') as fw:
        lines = f.readlines()

        data_list = []
        weight_list = []
        normalized_weight = []

        for i, line in enumerate(lines):
            data, weight = line.strip().split()[:-1], float(
                line.strip().split()[-1])
            data_list.append([x for x in data])
            weight_list.append(weight)

            # print(data_list)
            # print(weight_list)

            if (i + 1) % group_size == 0:
                if weight_list[0] != 0:
                    normalized_weight = [round(float(weight) / float(weight_list[0]),16) for weight in weight_list]
                else:
                    normalized_weight = [float(weight) for weight in weight_list]

                for j, weight in enumerate(normalized_weight):
                    row = []
                    row.append(data_list[j])

                    row.append(weight)
                    row_str = ' '.join([str(x) for x in row]) + '\n'
                    fw.write(row_str)

                data_list = []
                weight_list = []

    with open(single_tmpList_file, 'r', encoding='utf-8') as f, \
            open(single_lastList_file, 'w', encoding='utf-8') as fw:
        lines = f.readlines()
        for line in lines:
            # 去除不需要的字符
            line = line.replace("[","").replace("]","").replace(",","").replace("'", "")
            line_new = line.strip().split()
            fw.write(line_new[0] + ' ' + line_new[1] + ' ' +  line_new[2] + ' : ' + line_new[-1] + '\n')


# 这个函数很慢很慢很慢很慢... ...
def data_normal_48_new(filePath1, filePath2):
    with open(filePath1, 'r') as fr, \
            open(filePath2, 'w') as fw:
        lines = fr.readlines()
        for i in range(0, len(lines), 48):
            for line in lines:
                splits = line.strip().split()
                lineData = lines[i:i + 48]
            line_max = lineData[0]
            line_maxNum = float(line_max.strip().split()[-1])

            for line in lineData:
                splits = line.strip().split()
                aa=float(splits[-1])
                if line_maxNum != 0:
                    # fw.write(splits[0] + ':' + str(round(float(aa / line_maxNum),10)) + '\n')
                    fw.write(splits[0] + ' ' + splits[1] + ' ' +  splits[2] + ' : ' + str(round(float(aa / line_maxNum),10)) + '\n')
                else:
                    fw.write(splits[0] + ' ' + splits[1] + ' ' +  splits[2] + ' : ' + str(0) + '\n')


# ————4———— 
# 寻找G     
homoDict = {
    'G1': ['list5', 'list11', 'list42', 'list45'],
    'G2': ['list8', 'list12', 'list27', 'list31'],
    'G3': ['list13', 'list14', 'list18', 'list21'],
    'G4': ['list15', 'list17', 'list23', 'list36'],
    'G5': ['list9', 'list19', 'list29', 'list43'],
    'G6': ['list6', 'list20', 'list26', 'list48'],
    'G7': ['list7', 'list22', 'list24', 'list39'],
    'G8': ['list4', 'list25', 'list37', 'list38'],
    'G9': ['list16', 'list28', 'list40', 'list41'],
    'G10': ['list2', 'list3', 'list35', 'list47'],
    'G11': ['list10', 'list30', 'list32', 'list46'],
    'G12': ['list1', 'list33', 'list34', 'list44']
}

def getWillUtg(WillUtgFile):
    willUtg_List = []
    with open(WillUtgFile, 'r', encoding='utf_8') as f:
        for line in f:
            splits = line.strip().split()
            if splits[0] not in willUtg_List:
                willUtg_List.append(splits[0])
        return willUtg_List
    

# 创建存储两个关系和的文件
def add_hic_single(WillUtgFile, hicFile, singleFile, addTwoFile):
    utgHicRelationDict = {}
    utgSingleRelationDict = {}
    addTwoDict = {}
    willUtg_List = getWillUtg(WillUtgFile)
    with open(hicFile, 'r') as fr1, \
            open(singleFile, 'r') as fr2, \
            open(addTwoFile, 'w') as fw:
        # hic
        lines = fr1.readlines()
        for line in lines:
            splitArr = line.strip().split()
            splitArr1 = line.strip().split(':')
            hic_relation = round(float(splitArr1[1]), 10)
            if splitArr[0] not in utgHicRelationDict.keys():
                utgHicRelationDict[splitArr[0]] = {
                    splitArr[2]: hic_relation
                    }
            else:
                utgHicRelationDict[splitArr[0]].update({
                    splitArr[2]: hic_relation
                    })
        # print(utgHicRelationDict)


        # single
        lines = fr2.readlines()
        for line in lines:
            splitArr = line.strip().split()
            splitArr1 = line.strip().split(':')
            single_relation = round(float(splitArr1[1]), 10)
            if splitArr[0] not in utgSingleRelationDict.keys():
                utgSingleRelationDict[splitArr[0]] = {
                    splitArr[2]: single_relation
                }
            else:
                utgSingleRelationDict[splitArr[0]].update(
                    {splitArr[2]: single_relation}
                    )
        # print(utgHicRelationDict)


        # addTwoDict
        for willUtg in utgHicRelationDict.keys():
            for listid in utgHicRelationDict[willUtg].keys():
                if willUtg in utgSingleRelationDict.keys() and listid in utgSingleRelationDict[willUtg].keys():
                    if willUtg not in addTwoDict.keys():
                        addTwoDict[willUtg] = {
                            listid:
                            0.0001*utgHicRelationDict[willUtg][listid] +
                            utgSingleRelationDict[willUtg][listid]
                        }
                    else:
                        addTwoDict[willUtg].update({
                            listid:
                            0.0001*utgHicRelationDict[willUtg][listid] +
                            utgSingleRelationDict[willUtg][listid]
                        })
                
        # print(addTwoDict)



        '''utg000005l_pilon_1_10000  in  list31 的关系为: 11111'''
        for willUtg in willUtg_List:
            for listid in addTwoDict[willUtg].keys():
                fw.write(willUtg + '  in  ' + listid + ' 的关系为: ' +
                         str(addTwoDict[willUtg][listid])+'\n')
        # 存入add_hicSingle_relation.txt


# 对addTwoFile 48list排序
def sorted1(addTwoFile, addTwoSortedFile):
    lineData = []
    with open(addTwoFile, 'r') as fr, open(addTwoSortedFile, 'w') as fw:
        lines = fr.readlines()
        for i in range(0, len(lines), 48):
            for line in lines:
                lineData = lines[i:i + 48]
            lineData.sort(
                key=lambda line: round(float(line.strip().split()[-1]), 10),
                reverse=True)
            for line in lineData:
                fw.write(line)
            lineData = []


# 得到某个utg的分组与权重的字典 —— 分组是按照顺序排列的
# {'utg001l_pilon': [{'list1':'48'}, {'list34':'47'}...], 'utg002l_pilon': [{'list2':'48'}, {'list45':'47'}...]}
def getGroup(addTwoSortedFile):
    utgInfoDict = defaultdict(int)
    tmpInfoDict = defaultdict(int)
    tmpList = []
    with open(addTwoSortedFile, 'r') as mf:
        lines = mf.readlines()
        '''utg000005l_pilon_1_10000  in  list31 的关系为: 11111'''
        for line in lines:
            splits = line.strip().split()
            groupId = ''.join(re.findall(r'\d+', splits[2]))
            utgName = splits[0]
            if utgName not in tmpInfoDict:
                tmpInfoDict[utgName] = [groupId]
            else:
                tmpInfoDict[utgName].append(groupId)
                # {'utg001l_pilon': ['25','45'], 'utg002l_pilon': ['13','46']
        for utgName in tmpInfoDict.keys():
            for index, groupId in enumerate(tmpInfoDict[utgName]):
                weight = str(48 - index)
                groupId_weight = {'list' + groupId: weight}  # {list3:48}
                tmpList.append(groupId_weight)
                utgInfoDict[utgName] = tmpList
            tmpList = []
        return utgInfoDict


# selectGroup[考虑hom] ——> 确定最后分组~
# 确定utg的最后分组——>读文件'310.utgType.will_1k_79k.txt'——>写入文件result.tmp.txt
def selectGroup(addTwoSortedFile,willUtg_file,resultFilePath1,resultFilePath2):
    '''
    utg001l_pilon 类型为trip 在G1(list1 list2 list3)的权重为: 555
    '''
    utgTypeDict = {}
    utgInfoDict = getGroup(addTwoSortedFile)
    # {'utg001l_pilon': [{'list1':'48'}, {'list34':'47'}...], 'utg002l_pilon': [{'list2':'48'}, {'list45':'47'}...]}
    utgInfoDict_new = {}
    for utgName, tmplist in utgInfoDict.items():
        listDict = {}
        for tempDict in tmplist:
            listDict.update(tempDict)
        utgInfoDict_new[utgName] = listDict
    # {'utg001l_pilon':{'list1':'48','list34':'47'}, 'utg002l_pilon':{'list2':'48','list45':'47'}}
    
    # print(utgInfoDict_new['utg000078l_pilon_4390001_4400886'])
    tmpId = []  # 匹配上G1的['list5','list11']
    tmpWeight = 0  # 匹配上G1的list的权重和
    with open(willUtg_file, 'r') as mf, \
            open(resultFilePath1, 'w') as fw1, \
            open(resultFilePath2, 'w') as fw2:
        '''
            '310.utgType.will_1k_79k.txt'  [utg length type]
            resultFilePath1  result.tmp0.txt:  utg007l 在G1...G12分别的权重  ——————只有dip和trip
            resultFilePath2  result.tmp1.txt:  utg007l 在G1...G12找一个最大的G的权重  ——————四种类型都有~最后文件~
        '''
        lines = mf.readlines()
        for line in lines:
            splits = line.strip().split()
            utgTypeDict[splits[0]] = splits[2]
            # {'utg000007l_pilon_1_1420000':hap}
        for utgName, utgType in utgTypeDict.items():
            if utgName in utgInfoDict.keys():
                if utgType == 'hap':
                    selectGroup = 1
                    idList = []
                    for id, weight in utgInfoDict_new[utgName].items(): # {'list1':'48','list34':'47'}
                        idList.append(id)
                    groupIdLast = idList[0]  # ['list1']
                    groupWeightLast = utgInfoDict_new[utgName][groupIdLast]

                    for key in homoDict.keys():
                        if groupIdLast in homoDict[key]:
                            group_G = key

                    fw2.write(
                        utgName + ' 类型为' + utgType + ' 在' + group_G + '(' + groupIdLast + ')的权重为  :' + groupWeightLast + '\n')
                elif utgType == 'dip':
                    # 把12组里面权重最大的两个list+权重输出
                    # selectGroup = 2
                    # tmpId = []
                    # # {'G1': ['list5', 'list11', 'list42', 'list45'],...}
                    # for key in homoDict.keys():  # 自己定义的G1-G12
                    #     if utgName in utgInfoDict_new.keys():  # {'utg001l_pilon':{'list1':'48','list34':'47'},...}
                    #         for listId, weight in utgInfoDict_new[utgName].items():
                    #             if len(tmpId) < selectGroup:
                    #                 if listId in homoDict[key]:
                    #                     if len(tmpId) == 0:
                    #                         tmpId = [listId]
                    #                         tmpWeight += int(weight)
                    #                     else:
                    #                         tmpId.append(listId)
                    #                         tmpWeight += int(weight)
                    #         if len(tmpId) == selectGroup:  # 2
                    #             fw1.write(utgName + ' 类型为' + utgTypeDict[utgName] + ' 在' + key + '(' + tmpId[0] + ',' +
                    #                       tmpId[1] + ')''的权重为: ' + str(tmpWeight) + '\n')
                    #         tmpId = []
                    #         tmpWeight = 0

                    # 版本2
                    # selectGroup = 2
                    # tmpId = [] # 存最后的两个list
                    # idList = []
                    # for id, weight in utgInfoDict_new[utgName].items(): # {'list1':'48','list34':'47'}
                    #     idList.append(id) # ['list1', 'list34']
                    # groupIdLast_one = idList[0] # 'list1'
                    # groupWeightLast = int(utgInfoDict_new[utgName][groupIdLast_one])

                    # for key in homoDict.keys():
                    #     if groupIdLast_one in homoDict[key]:
                    #         group_G = key
                    #         groupId_remain = homoDict[key].remove(groupIdLast_one)
                    #         groupId_remain1 = homoDict[key]
                    #         groupIdLast_two = groupId_remain1[0]
                    #         groupWeightLast += int(utgInfoDict_new[utgName][groupIdLast_two])
                    #         tmpId.append(groupIdLast_one)        
                    #         tmpId.append(groupIdLast_two)    
                    # if len(tmpId) == selectGroup:  # 2
                    #     fw2.write(utgName + ' 类型为' + utgTypeDict[utgName] + ' 在' + key + '(' + tmpId[0] + ',' +
                    #             tmpId[1] + ')''的权重为: ' + str(groupWeightLast) + '\n')

                    # 版本3
                    selectGroup = 2
                    tmpId = []
                    idList = []
                    # {'G1': ['list5', 'list11', 'list42', 'list45'],...}
                    if utgName in utgInfoDict_new.keys():  # {'utg001l_pilon':{'list1':'48','list34':'47'},...}
                        
                        idList = list(utgInfoDict_new[utgName].keys())
                        print(idList)
                        groupIdLast_one = idList[0] # 'list1'第一个list找到了
                        tmpId.append(groupIdLast_one)
                    
                        for key in homoDict.keys():  # 自己定义的G1-G12
                            if groupIdLast_one in homoDict[key]:
                                # min_index = 99999
                                # min_item = ""
                                # for item in homoDict[key]:
                                #     index = idList.index(item)
                                #     if(index < min_index):
                                #         min_item = item
                                #         min_index = index
                                for tmpListId in idList[1:]: # 找第二个list
                                    if tmpListId in homoDict[key]:
                                        groupIdLast_two = tmpListId
                                        tmpId.append(groupIdLast_two) 
                                        print(idList)
                                        print(tmpId)
                                        if len(tmpId) == selectGroup:  # 2
                                            fw2.write(utgName + ' 类型为' + utgTypeDict[utgName] + ' 在' + key + '(' + tmpId[0] + ',' +
                                                    tmpId[1] + ')''的权重为: ' + str(groupWeightLast) + '\n')
                                        else:
                                            pass
                                        tmpId = []


                elif utgType == 'trip':
                    selectGroup = 3
                    tmpId = []
                    # {'G1': ['list5', 'list11', 'list42', 'list45'],...}
                    for key in homoDict.keys():  # 自己定义的G1-G12
                        if utgName in utgInfoDict_new.keys():  # {'utg001l_pilon':{'list1':'48','list34':'47'},...}
                            # for listId, weight in utgInfoDict_new[utgName].items():
                            #     if len(tmpId) < selectGroup:
                            #         if listId in homoDict[key]:
                            #             if len(tmpId) == 0:
                            #                 tmpId = [listId]
                            #                 tmpWeight += int(weight)
                            #             else:
                            #                 tmpId.append(listId)
                            #                 tmpWeight += int(weight)
                            # if len(tmpId) == selectGroup:  # 3
                            #     fw1.write(utgName + ' 类型为' + utgTypeDict[utgName] + ' 在' + key + '(' + tmpId[0] + ',' +
                            #               tmpId[1] + ',' + tmpId[2] + ')的权重为: ' + str(tmpWeight) + '\n')
                            # tmpId = []
                            # tmpWeight = 0

                            # 版本2
                            selectlist = list(utgInfoDict_new[utgName])[0] # 'list1'
                            for tmplist in homoDict[key]:
                                # 遍历这四个list['list5', 'list11', 'list42', 'list45']
                                if selectlist in homoDict[key] and tmplist !=selectlist:
                                    tmpId.append(tmplist)
                            if len(tmpId) == selectGroup:  # 3
                                fw2.write(utgName + ' 类型为' + utgTypeDict[utgName] + ' 在' + key + '(' + tmpId[0] + ',' +
                                          tmpId[1] + ',' + tmpId[2] + ')的权重为: ' + str(tmpWeight) + '\n')
                            tmpId = []


                elif utgType == 'tetrap':
                    selectGroup = 4
                    tmpId = []
                    # for key in homoDict.keys():  # 自己定义的G1-G12
                    #     if utgName in utgInfoDict_new.keys():  # {'utg001l_pilon':{'list1':'48','list34':'47'},...}
                    #         for listId, weight in utgInfoDict_new[utgName].items(): # list1 48
                    #             if len(tmpId) <= selectGroup:
                    #                 if listId in homoDict[key]:
                    #                     if len(tmpId) == 0:
                    #                         tmpId = [listId]
                    #                         tmpWeight += int(weight)
                    #                     else:
                    #                         tmpId.append(listId)
                    #                         tmpWeight += int(weight)
                    #         if len(tmpId) == selectGroup:
                    #             fw1.write(utgName + ' 类型为' + utgTypeDict[utgName] + ' 在' + key + '(' + tmpId[0] + ',' +
                    #                       tmpId[1] + ',' + tmpId[2] + ',' + tmpId[3] + ')的权重为: ' + str(
                    #                 tmpWeight) + '\n')
                    #         tmpId = []
                    #         tmpWeight = 0

                    # 版本2
                    for key in homoDict.keys():  # 自己定义的G1-G12
                        if utgName in utgInfoDict_new.keys():  # {'utg001l_pilon':{'list1':'48','list34':'47'},...}
                            selectlist = list(utgInfoDict_new[utgName])[0] # 'list1'
                            if selectlist in homoDict[key]:
                                tmpId = homoDict[key]
                                if len(tmpId) == selectGroup:
                                    fw2.write(utgName + ' 类型为' + utgTypeDict[utgName] + ' 在' + key + '(' + tmpId[0] + ',' +
                                        tmpId[1] + ',' + tmpId[2] + ',' + tmpId[3] + ')的权重为: ' + str(
                                        tmpWeight) + '\n')
                            tmpId = []
                            tmpWeight = 0
                        # 这儿的weight不管用
                            
                else:
                    pass



# 按照每个UtgId对12个组的关系从大到小排序
def readTmp0Sorted(resultFilePath1,resultFilePath2):
    lineData = []
    with open(resultFilePath1, 'r') as fr, \
            open(resultFilePath2, 'a') as fw2:
        lines = fr.readlines()
        # 对每12行排序
        for i in range(0, len(lines), 12):
            for line in lines:
                # splits = line.strip().split()
                # lineData.append(line)
                lineData = lines[i:i + 12]
            lineData.sort(key=lambda line: int(line.strip().split()[-1]), reverse=True)
            fw2.write(lineData[0])
            lineData = []


# utg000005l_pilon_1_10000 类型为hap 在G12(list34)的权重为  :48
# utg000005l_pilon	10001	60000	dip	12	1,34
# utg000005l_pilon_1_10000 类型为hap 在G7(list39,list24)的权重为 : 48

def result_format(resultFilePath2, result_format_FilePath2):
    with open(resultFilePath2, mode='r', encoding='utf_8') as fr, \
            open(result_format_FilePath2, mode='w', encoding='utf_8') as fw:
        lines = fr.readlines()
        for line in lines:
            splits = line.strip().split()
            utgName = splits[0]
            utgType = splits[1][3:]
            utgGroup = splits[2][splits[2].find('G') + 1:splits[2].find('(')]
            list_str = splits[2][splits[2].find('(') + 1:splits[2].find(')')]
            groupId = ','.join(re.findall(r'\d+', list_str))
            fw.write(utgName + '\t' + utgType + '\t' + utgGroup + '\t' +
                     groupId + '\n')
            

# 310.standard.utg78l.info
def format(standard310File, standard310FileFormat):
    with open(standard310File, 'r') as fr, \
            open(standard310FileFormat, 'w') as fw:

        lines = fr.readlines()
        for line in lines:
            splits = line.strip().split()
            utgName = splits[0] + '_' + splits[1] + '_' + splits[2]
            fw.write(utgName + '\t' + splits[-3] + '\t' + splits[-2] + '\t' +
                     splits[-1] + '\n')
            

def test():
    homoDict = {
    'G1': ['list5', 'list11', 'list42', 'list45'],
    'G2': ['list8', 'list12', 'list27', 'list31'],
    'G3': ['list13', 'list14', 'list18', 'list21'],
    'G4': ['list15', 'list17', 'list23', 'list36'],
    'G5': ['list9', 'list19', 'list29', 'list43'],
    'G6': ['list6', 'list20', 'list26', 'list48'],
    'G7': ['list7', 'list22', 'list24', 'list39'],
    'G8': ['list4', 'list25', 'list37', 'list38'],
    'G9': ['list16', 'list28', 'list40', 'list41'],
    'G10': ['list2', 'list3', 'list35', 'list47'],
    'G11': ['list10', 'list30', 'list32', 'list46'],
    'G12': ['list1', 'list33', 'list34', 'list44']
    }

    dict={'utg001l_pilon':{'list1':'48','list34':'47'},
          'utg002l_pilon':{'list2':'48','list56':'47'}}
    selectList = list(dict['utg001l_pilon'])[0]
    print(selectList)
    for tmplist in homoDict['G1']:
        print(tmplist)

    idList=[]
    for listId, weight in dict['utg001l_pilon'].items():
        idList.append(listId) 
    groupIdLast_one = idList[0]
    groupId_tmp = homoDict['G1']
    groupId_remain=homoDict['G1'].remove('list5')
    # print(groupId_remain)
    # print(groupId_remain)
    print(homoDict['G1'])
    a=homoDict['G1']
    print(a[0])


if __name__ == '__main__':
    result1File = 'result.single.tmp.txt'
    result2File = 'result.single.list.tmp.txt'

    single_List_file = 'result.single.sorted.txt'
    single_tmpList_file = 'result.single.list.normal.tmp1.txt'
    single_lastList_file = 'result.single.list.normal.last.txt'
    single_normal_file = 'result.single.normal.txt'
    willUtg_file = '310.utgType.will.trip.txt'

    hicFile, singleFile = 'result.hic.normal.txt', 'result.single.normal.txt'
    addTwoFile, addTwoSortedFile = 'add_hicSingle_relation.txt', 'add_hicSingle_relation_sorted.txt'
    resultFilePath1, resultFilePath2 = 'result.group.tmp0.txt' , 'result.group.txt'
    result_format_FilePath2 = 'result.group.310.txt'

    # 1 对于每个list只输出最大的一个关系
    # findList_one(result1File,result2File)
    # 2
    # sorted1(result2File,single_List_file)
    # sort -k1,1 -k7,7nr result.single.list.tmp.txt > result.single.sorted.txt # 有点问题
    # 3
    # normalized(single_List_file, single_tmpList_file, single_lastList_file) 
    # data_normal_48_new(single_List_file, single_normal_file) #巨慢

    # 5
    # add_hic_single(willUtg_file, hicFile, single_lastList_file, addTwoFile)
    # 6
    # sorted1(addTwoFile,addTwoSortedFile)
    # sort -k1,1 -k5,5nr add_hicSingle_relation.txt > add_hicSingle_relation_sorted.txt # 有点问题
    # 7
    selectGroup(addTwoSortedFile,willUtg_file,resultFilePath1,resultFilePath2)
    # 8
    readTmp0Sorted(resultFilePath1,resultFilePath2)
    # 9
    result_format(resultFilePath2, result_format_FilePath2)
    # sort -k1,1 result.group.310.txt > result.group.310.sorted.txt

    # format('310.standard.utg78l.info', '310.standard.utg78l.format.info')
    # sort -k1,1 310.standard.utg78l.format.info > 310.standard.utg78l.format.sorted.info

    


