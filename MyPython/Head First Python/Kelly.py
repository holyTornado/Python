# Kelly.py
"""一组U10选手一直在刻苦训练。每跑完一个600米，Kelly就会计时并把时间记录在计算机上的一个文本文件中。总共有4个文件，分别记录James、Sarah、Julie、和Mikey的时间数据。"""


def sanitize(time_string):
    """    过滤时间格式，将‘-’或‘：’转换成‘.‘，如：2.34    """
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + "." + secs)


def get_coach_data(filename):
    """读取文件数据，转换时间格式、排序、集合，使用分片打印前3项"""
    try:
        with open(filename) as printlist:
            file_data = printlist.readline()
            _list = file_data.strip().split(',')
        _sortlist = sorted([sanitize(each_t) for each_t in _list])

        print(str(filename) + '(原始数据): ' + str(file_data))
        print(str(filename) + '(规范排序): ' + str(_sortlist))
        print(str(filename) + '(最快3次): ' + str(sorted(set(_sortlist))[0:3]))
    except IOError as errtip:
        print('File error: ' + str(errtip))
        return (None)


get_coach_data('james.txt')
print('---')
get_coach_data('julie.txt')
print('---')
get_coach_data('mikey.txt')
print('---')
get_coach_data('sarah.txt')
print('---')
get_coach_data('monkey.txt')
