import re
from collections import defaultdict

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
homoDict_reverse = {}  # {'list5': 'G1', ...}
for Group, List in homoDict.items():
    for l in List:
        homoDict_reverse[l] = Group


# if 48行的最后一列数据均为0 将utg添加到列表 ——> 代表unlinkUtg
def getUnlink(single_list_file, unlink_file):
    with open(single_list_file) as f:
        lines = f.readlines()

    # 存unlink的utg
    utg_unlink_list = []
    for i in range(0, len(lines), 48):
        group = lines[i:i + 48]

        # 判断这48行的最后一列是否全为0
        if all(line.strip().split()[-1] == '0' for line in group):
            utg_unlink_list.append(group[0].strip().split()[0])
    # print(utg_unlink_list)
    # 输出unlink contig到文件
    with open(unlink_file, 'w') as fw:
        for unlink_utg in utg_unlink_list:
            fw.write(unlink_utg + '\n')


# 得到'utg000033l_pilon': {'utg000033l_pilon_1_10000': {10000: {'list38': '0.7299916716448632'}}...}
# 加了size[5000 4000 ...]
def getAll_size_dict(single_list_file, utg_split_onelist_file):
    with open(single_list_file, 'r') as fr, \
            open(utg_split_onelist_file, 'w') as fw:
        utg_list_weight_Dict = {}  # {'utg000005l_pilon_1_10000':{'list5': 0.5867} ...}
        all_dict = {}  # {'utg000005l_pilon':{'utg000005l_pilon_1_10000':['G1','list5']:0.5867}
        utg_Group_standard_dict = {}  # 标准答案的utg和所属group的字典

        count = 0
        lines = fr.readlines()
        for line in lines:
            if count == 0:
                line_max = line
                line_max_splits = line_max.strip().split()

                willUtg, tmplist, tmpWeight = line_max_splits[0], line_max_splits[2], line_max_splits[-1]

                utg = willUtg[:16]
                homo_group = homoDict_reverse[tmplist]
                utg_list_weight_Dict[willUtg] = {
                    tmplist: tmpWeight
                }  # {'utg000005l_pilon_1_10000':{'list5': 0.5867} ...}

                if utg not in all_dict.keys():
                    all_dict[utg] = {willUtg: {tmplist: tmpWeight}}
                else:
                    if willUtg not in all_dict[utg].keys():
                        all_dict[utg][willUtg] = {tmplist: tmpWeight}
                    else:
                        all_dict[utg][willUtg].update({tmplist: tmpWeight})
                # all_dict = {'utg000005l_pilon': {'utg000005l_pilon_1_10000': {'list34': '0.5867265496338172'},
                #                                  'utg000005l_pilon_10001_60000': {'list2': '0.9680494178792686'}},
                #             'utg000104l_pilon': {'utg000104l_pilon_370001_380000': {'list1': '0'}}}
            count += 1
            if count == 48:
                count = 0

        all_size_dict = {}
        for utg, utgData in all_dict.items():
            for willUtg, data in utgData.items():
                willUtg_size = int(willUtg.split('_')[-1]) - int(willUtg.split('_')[-2]) + 1
                if utg not in all_size_dict.keys():
                    all_size_dict.update({utg: {willUtg: {willUtg_size: data}}})
                else:
                    all_size_dict[utg].update({willUtg: {willUtg_size: data}})

        for utg in all_size_dict.keys():
            for willUtg in all_size_dict[utg].keys():
                for willUtg_size in all_size_dict[utg][willUtg].keys():
                    for list in all_size_dict[utg][willUtg][willUtg_size].keys():
                        will_weight = round(float(all_size_dict[utg][willUtg][willUtg_size][list]), 6)
                        fw.write(
                            utg + ' ' + willUtg + ' ' + str(willUtg_size) + ' ' + list + ' ' + str(will_weight) + '\n')
        return all_size_dict


def get_max_weight_list(utg_split_onelist_file, single_list_first_file, unlinked_limited_gamete_file):
    utg_dict = {}  # {utg:[(),(),()...]}
    result_dict = {}  # {utg:()} 保留一个权重最大的tuple
    unlinked_limited_list = []
    utg_Group_standard_dict = {}  # {utg:3} 标准答案的utg和所属group的字典
    with open(utg_split_onelist_file, 'r') as fr, \
            open(single_list_first_file, 'w') as fw,\
                open(unlinked_limited_gamete_file, 'w') as fw1:
        lines = fr.readlines()
        for line in lines:
            splits = line.strip().split()
            utg = splits[0]
            utg_tuple = tuple(splits[1:])
            if utg not in utg_dict.keys():
                utg_dict[utg] = [utg_tuple]
            else:
                utg_dict[utg].append(utg_tuple)

        for utg in utg_dict.keys():
            willutg_tuple_set = utg_dict[utg]  # [(),(),()...]
            willutg_tuple_set_sorted = sorted(
                willutg_tuple_set,
                key=lambda x: (int(x[1]), float(x[-1]), -int(x[0].split('_')[2])),
                reverse=True
            )
            max_tuple = willutg_tuple_set_sorted[0]  # {utg:()} 保留一个权重最大的tuple
            if int(max_tuple[1]) > 50000:  # ('utg000052l_pilon_1_10000', '10000', 'list22', '0.653456')
                for tmptuple in willutg_tuple_set_sorted:
                    if int(tmptuple[1]) == 50000 and float(tmptuple[-1]) != 0.0:
                        result_dict[utg] = tmptuple
                        break
                    elif int(tmptuple[1]) < 50000 and float(tmptuple[-1]) != 0.0:
                        result_dict[utg] = tmptuple
                        break
                if utg not in result_dict.keys():
                    for tmptuple in willutg_tuple_set_sorted:
                        if int(tmptuple[1]) > 50000 and float(tmptuple[-1]) != 0.0:
                            result_dict[utg] = tmptuple
            elif int(max_tuple[1]) == 50000:
                if float(max_tuple[-1]) != 0.0:
                    result_dict[utg] = max_tuple
                else:
                    for tmptuple in willutg_tuple_set_sorted:
                        if int(tmptuple[1]) == 50000 and float(tmptuple[-1]) != 0.0:
                            result_dict[utg] = tmptuple
                            break
                        elif int(tmptuple[1]) < 50000 and float(tmptuple[-1]) != 0.0:
                            result_dict[utg] = tmptuple
                            break
            elif int(max_tuple[1]) < 50000:
                if float(max_tuple[-1]) != 0.0:
                    result_dict[utg] = max_tuple
                else:
                    for tmptuple in willutg_tuple_set_sorted:
                        if int(tmptuple[1]) == 50000 and float(tmptuple[-1]) != 0.0:
                            result_dict[utg] = tmptuple
                            break
                        elif int(tmptuple[1]) < 50000 and float(tmptuple[-1]) != 0.0:
                            result_dict[utg] = tmptuple
                            break
            if utg not in result_dict.keys():
                unlinked_limited_list.append(utg)
                fw1.write(utg + '\tre-linking unlinked impossible. '+'\n')
            # print(len(result_dict))  # 3721
        #     if utg == 'utg001876l_pilon':
        #         print(willutg_tuple_set_sorted)
        # print(utg_dict['utg001876l_pilon'])
        # print(unlinked_limited_list)
        # print(result_dict['utg001876l_pilon'])

            if utg not in unlinked_limited_list:
                utg_tuple = result_dict[utg]  # ('utg000005l_pilon_1_10000', 10000, 'list34', '0.5867265496338172')
                max_list = utg_tuple[2]
                max_weight = utg_tuple[3]
                utg_Group_standard_dict[utg] = homoDict_reverse[max_list][1:]
                # 输出权重最大的元组
                fw.write(utg + ' ' + homoDict_reverse[max_list][1:] + ' ' + max_list[4:] + ' ' + str(max_weight) + '\n')
        return utg_Group_standard_dict


# 读取4.py的结果文件result.group.310.txt 找出group与标准答案不一致的,重新分组
def refine_result_group(resultgroup_file, errorutg_file):
    utg_type_group_dict = {}
    # {'utg017108l_pilon': {'utg017108l_pilon_1_10000': '8', 'utg017108l_pilon_10001_17026': '11'}

    utg_Group_standard_dict = get_max_weight_list(utg_split_onelist_file,
                                                  single_list_first_file,unlinked_limited_gamete_file)  # {'utg017108l_pilon': '8'}
    # willUtg标准答案所属的G ——> {'utg017108l_pilon': '8'}

    with open(resultgroup_file, 'r') as fr, \
            open(errorutg_file, 'w') as fw:
        lines = fr.readlines()
        for line in lines:
            splits = line.strip().split()
            willUtg, utgType, utgGroup = splits[0], splits[1], splits[2]

            utg = willUtg[:16]
            if utg not in utg_type_group_dict.keys():
                utg_type_group_dict[utg] = {willUtg: utgGroup}
            else:
                if willUtg not in utg_type_group_dict[utg].keys():
                    utg_type_group_dict[utg][willUtg] = utgGroup
        # print(utg_type_group_dict) # √

        result = {}  # 存与标准答案Group不一致的willUtg
        for key, value in utg_type_group_dict.items():  # {utg:{willUtg: utgGroup}}
            if key in utg_Group_standard_dict.keys():
                result[key] = []
                for sub_key, sub_value in value.items():  # {willUtg: utgGroup}
                    if sub_key not in result.keys() and sub_value != utg_Group_standard_dict[key]:
                        result[key].append(sub_key)
        # {'utg017108l_pilon': ['utg017108l_pilon_10001_17026', 'utg017108l_pilon_11001_17026'], ...}
        for utg, errorList in result.items():
            for errorUtg in errorList:
                fw.write(errorUtg + '\n')


# 得到某个utg的分组与权重的字典 —— 分组是按照顺序排列的
# {'utg001l_pilon': [{'list1':'48'}, {'list34':'47'}...], 'utg002l_pilon': [{'list2':'48'}, {'list45':'47'}...]}
def getGroup(addTwoSortedFile):
    utgInfoDict = defaultdict(int)
    tmpInfoDict = defaultdict(int)
    tmpList = []
    utgInfoDict_new = {}
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
        # {'utg001l_pilon_10_20': [{'list1':'48'}, {'list34':'47'}...], 'utg002l_pilon_20_30': [{'list2':'48'}, {'list45':'47'}...]}
        for utgName, tmplist in utgInfoDict.items():
            listDict = {}
            for tempDict in tmplist:
                listDict.update(tempDict)
            utgInfoDict_new[utgName] = listDict
        # {'utg001l_pilon_10_20':{'list1':'48','list34':'47'}, 'utg002l_pilon_20_30':{'list2':'48','list45':'47'}}
        return utgInfoDict_new


# 将重新分组结果写入文件'error_utg_refine.txt'
def write_refine_result_group(resultgroup_file, errorutg_file, single_list_first_file, err_refine_file):
    utg_type_dict = {}
    err_list = []
    err_type_dict = {}
    utg_main_group_dict = {}  # 存utg_main和标准Group ——> {utg001147l_pilon:12}

    utgInfoDict_new = getGroup(addTwoSortedFile)
    with open(resultgroup_file, 'r') as fr1, \
            open(errorutg_file, 'r') as fr2, \
            open(single_list_first_file, 'r') as fr3:
        # 存所有contig的类型
        lines1 = fr1.readlines()
        for line in lines1:
            splits = line.strip().split('\t')
            utgName, utgType = splits[0], splits[1]
            utg_type_dict[utgName] = utgType
        # 存error的contig类型
        lines2 = fr2.readlines()
        for line in lines2:
            splits = line.strip().split('\t')
            errUtg = splits[0]
            err_list.append(errUtg)
        for utg in utg_type_dict.keys():
            if utg in err_list:
                err_type_dict[utg] = utg_type_dict[utg]  # {utg:type}
        # 存utg和标准Group utg001144l_pilon 5 19 0.931381
        lines3 = fr3.readlines()
        for line in lines3:
            splits = line.strip().split()
            utg_main, group_main = splits[0], splits[1]
            utg_main_group_dict[utg_main] = group_main  # {utg001147l_pilon:12}

    with open(err_refine_file, 'w') as fw:
        for err_utgName, utgType in err_type_dict.items():
            if err_utgName in utgInfoDict_new.keys():
                err_utgName_main = err_utgName[:16]
                if err_utgName_main in utg_main_group_dict.keys():
                    group_main = utg_main_group_dict[err_utgName_main]
                if utgType == 'hap':
                    selectGroup = 1
                    tmpId = []
                    # {'G1': ['list5', 'list11', 'list42', 'list45'],...}
                    if 'G'+group_main in homoDict.keys():  # 自己定义的G1-G12
                        idList = list(utgInfoDict_new[err_utgName].keys())
                        for tmpListId in idList:
                            if tmpListId in homoDict['G'+group_main]:
                                # 遍历这四个list['list5', 'list11', 'list42', 'list45']
                                tmpId.append(tmpListId)
                                if len(tmpId) == selectGroup:
                                    break
                        if len(tmpId) == selectGroup:  # 1
                            fw.write(
                                err_utgName + '\t' + err_type_dict[err_utgName] + '\t' + group_main + '\t' + tmpId[
                                    0][4:] + '\n')
                        tmpId = []
                elif utgType == 'dip':
                    selectGroup = 2
                    tmpId = []
                    # {'G1': ['list5', 'list11', 'list42', 'list45'],...}
                    if 'G'+group_main in homoDict.keys():  # 自己定义的G1-G12
                        idList = list(utgInfoDict_new[err_utgName].keys())
                        for tmpListId in idList:
                            if tmpListId in homoDict['G'+group_main]:
                                # 遍历这四个list['list5', 'list11', 'list42', 'list45']
                                tmpId.append(tmpListId)
                                if len(tmpId) == selectGroup:
                                    break
                        if len(tmpId) == selectGroup:  # 2
                            fw.write(
                                err_utgName + '\t' + err_type_dict[err_utgName] + '\t' + group_main + '\t' + tmpId[
                                    0][4:] + ',' + tmpId[1][4:] + '\n')
                        tmpId = []
                elif utgType == 'trip':
                    selectGroup = 3
                    tmpId = []
                    # {'G1': ['list5', 'list11', 'list42', 'list45'],...}
                    if 'G' + group_main in homoDict.keys():  # 自己定义的G1-G12
                        idList = list(utgInfoDict_new[err_utgName].keys())
                        for tmpListId in idList:
                            if tmpListId in homoDict['G' + group_main]:
                                selectlist = tmpListId  # 权重排序最大的list
                                break
                        for tmpListId in homoDict['G' + group_main]:
                            # 遍历这四个list['list5', 'list11', 'list42', 'list45']
                            if tmpListId != selectlist:
                                tmpId.append(tmpListId)
                                if len(tmpId) == selectGroup:
                                    break
                        if len(tmpId) == selectGroup:  # 3
                            fw.write(
                                err_utgName + '\t' + err_type_dict[err_utgName] + '\t' + group_main + '\t'
                                + tmpId[0][4:] + ',' +
                                tmpId[1][4:] + ',' + tmpId[2][4:] + '\n')
                        tmpId = []
                elif utgType == 'tetrap':
                    selectGroup = 4
                    if 'G'+group_main in homoDict.keys():
                        tmpId = homoDict['G'+group_main]
                        if len(tmpId) == selectGroup:
                            fw.write(
                                err_utgName + '\t' + err_type_dict[err_utgName] + '\t' + group_main + '\t' + tmpId[
                                    0][4:] + ',' +
                                tmpId[1][4:] + ',' + tmpId[2][4:] + ',' + tmpId[3][4:] + '\n')


# 将第一阶段结果result.group.310.txt + error_utg_refine.txt ——> result.group.310.refine.txt
def refine_merge(resultgroup_file, err_refine_file, merge_file):
    allUtg_dict = {}
    errUtg_dict = {}
    with open(resultgroup_file, 'r') as fr1, \
            open(err_refine_file, 'r') as fr2, \
            open(merge_file, 'w') as fw:
        lines1 = fr1.readlines()
        for line in lines1:
            splits = line.strip().split('\t')
            allUtg, all_info = splits[0], splits[1:]
            allUtg_dict[allUtg] = all_info

        lines2 = fr2.readlines()
        for line in lines2:
            splits = line.strip().split('\t')
            errUtg, err_info = splits[0], splits[1:]
            errUtg_dict[errUtg] = err_info

        for utg in allUtg_dict.keys():
            if utg not in errUtg_dict.keys():
                fw.write(utg + '\t')
                for utg_info in allUtg_dict[utg]:
                    fw.write(utg_info + '\t')
                fw.write('\n')
            else:
                fw.write(utg + '\t')
                for utg_info in errUtg_dict[utg]:
                    fw.write(utg_info + '\t')
                fw.write('\n')


if __name__ == '__main__':
    single_list_file = 'result.single.sorted.txt'
    utg_split_onelist_file = 'result.single.willutg.sorted.txt'  # 每个utg下面的willutg存权重最大的list
    single_list_first_file = 'result.single.sorted.one.txt'  # 每个utg存一个list
    unlinked_limited_gamete_file = 'unlinked_limited_gamete.txt'
    resultgroup_file = 'result.group.350.txt'

    addTwoSortedFile = 'add_hicSingle_relation_sorted.txt'
    unlink_file, errorutg_file, err_refine_file = 'unlink_utg.txt', 'error_utg.txt', 'error_utg_refine.txt'
    merge_file = 'result.group.350.refine.txt'

    getUnlink(single_list_file, unlink_file)
    getAll_size_dict(single_list_file, utg_split_onelist_file)
    get_max_weight_list(utg_split_onelist_file, single_list_first_file, unlinked_limited_gamete_file)
    refine_result_group(resultgroup_file, errorutg_file)
    #
    write_refine_result_group(resultgroup_file, errorutg_file, single_list_first_file, err_refine_file)
    refine_merge(resultgroup_file, err_refine_file, merge_file)

