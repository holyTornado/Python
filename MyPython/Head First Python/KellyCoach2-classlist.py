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


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=None):
        list.__init__([])
        if a_times is None:
            a_times = []
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def ath_top(self, _top=3):
        return sorted(set(each_t for each_t in self))[0:_top]


def get_coach_data(filename):
    """读取文件数据，转换时间格式、排序、集合，使用分片打印前3项"""
    try:
        with open(filename) as _list:
            file_text = _list.readline()
        file_data = file_text.strip().split(',')
        print(str(filename) + '(原始数据): ' + str(file_text))
        return AthleteList(file_data.pop(0), file_data.pop(0), [sanitize(each_t) for each_t in file_data])
    except IOError as err_tip:
        print('File error: ' + str(err_tip) + '\n---')
        return None


def customize_print(ath_class, first_num):
    """又换成类的形式调用并打印了，在过程中添加了“最快几次记录查看”的输入，增加了互动性    """
    print('姓名: ' + str(ath_class.name) + ';\t\t生日: ' + str(ath_class.dob) + '\n计时记录: ' + str(ath_class))
    print('最快 ' + str(first_num) + '次: ' + str(ath_class.ath_top(first_num)))
    print('---')


athletes = ['James2', 'Julie2', 'Mikey2', 'Sarah2', 'Monkey2']
first_num_input = input('本轮查看最快几次的记录(默认为3次)?')
if first_num_input.isdigit() is False:
    first_num_input = 3
else:
    first_num_input = int(first_num_input)

for each_ath in athletes:
    temp_class = get_coach_data(each_ath + '.txt')
    if temp_class is not None:
        customize_print(temp_class, first_num_input)

print('---输入测试---')
vera = AthleteList('Vera Vi')
vera.append('1.31')
customize_print(vera, first_num_input)
vera.extend(['2.22', '1-21', '2:34'])
customize_print(vera, first_num_input)
