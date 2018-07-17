# sketch.py

"""
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            if each_line.find(':') > 0:
                [role, line_spoken] = each_line.split(':', 1)
                print(role, end = '')
                print(" 说: ", end = '')
                print(line_spoken, end = '')
            else:
                print(each_line, end = '')
        except:
            pass

    data.close()

except:
    print('<sketch.txt>文件不存在！')
"""
import pickle
from MoviesNester import print_lol

MAN_LIST = []
OTHER_LIST = []

try:
    FILE_DATA = open('sketch.txt')
    for each_line in FILE_DATA:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                MAN_LIST.append(line_spoken)
            elif role == 'Other Man':
                OTHER_LIST.append(line_spoken)
        except ValueError:
            pass
    FILE_DATA.close()
except IOError:
    print('The datafile is missing!')

print("Man:\n")
print_lol(MAN_LIST, True, True, 0, 0, '')

print("\nOther Man:\n")
print_lol(OTHER_LIST, True, True, 0, 0, '')

print('文件内容读取完毕！\n------\n')

try:
    with open('man_data.txt') as man_out, open('other_data.txt') as other_out:
        if 'man_out' in locals():
            print('man_data.txt已存在！内容将被重写！')
        if 'other_out' in locals():
            print('other_data.txt已存在！内容将被重写！')
except IOError as err_tip:
    print('异常：' + str(err_tip))

try:
    with open('man_data.pickle', 'wb') as man_out, open('other_data.pickle', 'wb') as other_out:
        """print_lol(MAN_LIST, True, True, 0, 0, man_out)
        print_lol(OTHER_LIST, True, True, 0, 0, other_out)"""
        pickle.dump(MAN_LIST, man_out)
        pickle.dump(OTHER_LIST, other_out)
except IOError as err_tip:
    print('\n\nIOError: ' + str(err_tip))
except pickle.PickleError as err_tip:
    print('\n\nPickleError: ' + str(err_tip))

if 'man_out' in locals():
    print('man_data 创建成功')

if 'other_out' in locals():
    print('other_data 创建成功')

print('\n---Pickle形式读取数据并显示---')
try:
    with open('man_data.pickle', 'rb') as man_out, open('other_data.pickle', 'rb') as other_out:
        """print_lol(MAN_LIST, True, True, 0, 0, man_out)
        print_lol(OTHER_LIST, True, True, 0, 0, other_out)"""
        MAN_LIST = pickle.load(man_out)
        print('Man_List')
        print(MAN_LIST)
        print('------')
        OTHER_LIST = pickle.load(other_out)
        print('Other_List')
        print(OTHER_LIST)
except IOError as err_tip:
    print('\n\nIOError: ' + str(err_tip))
except pickle.PickleError as err_tip:
    print('\n\nPickleError: ' + str(err_tip))
