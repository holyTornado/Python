# KellyCoach2.py
"""一组U10选手一直在刻苦训练。每跑完一个600米，Kelly就会计时并把时间记录在计算机上的一个文本文件中。总共有4个文件，分别记录James、Sarah、Julie、和Mikey的时间数据。"""


def sanitize(time_string):
    """过滤时间格式，将‘-’或‘：’转换成‘.‘，如：2.34"""
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


def get_coach_data(filename):
    '''读取文件数据，转换时间格式、排序、集合，使用分片打印前3项'''
    try:
        with open(filename) as _list:
            file_data = _list.readline().strip().split(',')
        (ath_name, ath_dob) = file_data.pop(0), file_data.pop(0)
        _sortlist = sorted([sanitize(each_t) for each_t in file_data])
        print(str(filename) + '(原始数据): ' + str(file_data) + '\n姓名: ' + ath_name + '\t\t；生日: ' + ath_dob)
        return (_sortlist)
    except IOError as errtip:
        print('File error: ' + str(errtip) + '\n---')
        return (None)


def customize_print(_list):
    '''分片打印'''
    print('(最快 3次): ' + str(sorted(set([each_t for each_t in _list]))[0:3]) + '\n---')


athletes = ['James2', 'Julie2', 'Mikey2', 'Sarah2', 'Monkey2']
for each_ath in athletes:
    temp_list = get_coach_data(each_ath + '.txt')
    if temp_list != None:
        customize_print(temp_list)
