def write(filePath, content):
    with open(filePath, mode='a') as f:
        f.write(content)


def get_alreadyContig(alreadyContig):
    alreadyContig_list = []
    with open(alreadyContig, 'r') as fr:
        lines = fr.readlines()
        for line in lines:
            splits = line.strip()
            alreadyContig_list.append(splits)
        return alreadyContig_list


def get_all_splitContig(stan_split_all, all_split_size):
    with open(stan_split_all, 'r') as file:
        with open(all_split_size, 'w') as outfile:
            for line in file:
                line = line.strip()
                fields = line.split('\t')

                ctg_id = fields[0]
                start = int(fields[1])
                end = int(fields[2])
                type = fields[3]
                length = end - start + 1
                new_line = f'{ctg_id}_{start}_{end}\t{length}\t{type}'
                outfile.write(new_line + '\n')


def get_willContig(all_split_size, will_split_sizeType):
    alreadyContig_list = get_alreadyContig(alreadyContig)
    # print(alreadyContig_list)
    with open(all_split_size, 'r') as fr1, open(will_split_sizeType, 'w') as fw:
        lines = fr1.readlines()
        for line in lines:
            splits = line.strip().split()
            utg_splitName = splits[0]
            if utg_splitName[:16] not in alreadyContig_list:
                fw.write(line)


if __name__ == '__main__':
    alreadyContig = '310.alreadyContig_1071.txt'
    stan_split_all, all_split_size = '310.marker.info', '310.marker.output.txt'
    will_split_sizeType = '310.utgType.will.split50k.txt'

    # get_all_splitContig(stan_split_all, all_split_size)
    get_willContig(all_split_size, will_split_sizeType)
