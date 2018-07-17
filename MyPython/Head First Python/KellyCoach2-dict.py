# KellyCoach2.py
"""一组U10选手一直在刻苦训练。每跑完一个600米，Kelly就会计时并把时间记录在计算机上的一个文本文件中。总共有4个文件，分别记录James、Sarah、Julie、和Mikey的时间数据。"""


def sanitize(time_string):
    """    过滤时间格式，将‘-’或‘：’转换成‘.‘，如：2.34    """
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (minute, secs) = time_string.split(splitter)
    return minute + '.' + secs


def get_coach_data(filename):
    """读取文件数据，转换时间格式、排序、集合，使用分片打印前3项"""
    try:
        with open(filename) as _list:
            file_text = _list.readline()
        file_data = file_text.strip().split(',')
        print(str(filename) + '(原始数据): ' + str(file_text))
        return {'Name': file_data.pop(0), 'BirthDay': file_data.pop(0),
                'Times': [sanitize(each_t) for each_t in file_data]}
    except IOError as err_tip:
        print('File error: ' + str(err_tip) + '\n---')
        return None


def customize_print(_dic):
    """'先保存到文件名+dic.txt文件，再分组打印"""
    try:
        save_file = str(_dic['Name']) + '_dic.txt'
        with open(save_file, 'w') as s_file:
            print(str(_dic), file=s_file)
    except IOError as err_tip:
        print('File error: ' + str(err_tip) + '\n---')

    print('姓名: ' + str(_dic['Name']) + ';\t\t生日: ' + str(_dic['BirthDay']) + '\n计时记录: ' + str(_dic['Times']))
    print('最快 3次: ' + str(sorted(set(each_t for each_t in _dic['Times']))[0:3]))
    print('---')


athletes = ['James2', 'Julie2', 'Mikey2', 'Sarah2', 'Monkey2']
for each_ath in athletes:
    temp_dic = get_coach_data(each_ath + '.txt')
    if temp_dic is not None:
        customize_print(temp_dic)
