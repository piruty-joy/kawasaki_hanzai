
# coding: utf-8
import os
import re

date_pattern = r"([0-9]+)月([0-9]+)日"


def conv_txt_to_csv(path):
    hanzai_list = {}
    for hanzai_t in hanzai_type:
        hanzai_list[hanzai_t] = []
    date_list = []
    filename = path.split('.')[0]
    heisei_year = filename[6:8]
    year = '2016' if heisei_year == '28' \
            else '2015' if heisei_year == '27' \
            else '2014' if heisei_year == '26' \
            else '2013'
    with open('./txt/' + filename + '.txt', 'r') as file:
        for line in file:
            is_added = False
            for hanzai_t in hanzai_type:
                if hanzai_t in line:
                    split_line = line.strip().split(' ')
                    hanzai_list[split_line[0]].append(int(split_line[1]))
                    is_added = True
                    break
            if is_added:
                continue
            # 犯罪の種類ではない →  日付, 地名, 空白・改行のいずれか
            match = re.match(date_pattern, line)
            if match:
                date_list.append("{0:02d}{1:02d}".format(int(match.group(1)), int(match.group(2))))

    date_list.sort()
    date_list.reverse()

    with open('./csv/' + filename + '.csv', 'w') as file:
        file.write('日付,路上強盗,ひったくり,空き巣,車上ねらい,自転車盗\n')
        for i in range(0, len(date_list)):
            file.write('{},{},{},{},{},{}\n'.format(year + date_list[i], hanzai_list['路上強盗'][i], hanzai_list['ひったくり'][i], hanzai_list['空き巣'][i], hanzai_list['車上ねらい'][i], hanzai_list['自転車盗'][i]))

hanzai_type = ['路上強盗', 'ひったくり', '空き巣', '車上ねらい', '自転車盗']

txt_files = os.listdir('./txt/')

for txt in txt_files:
    conv_txt_to_csv(txt)
