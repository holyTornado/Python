"""这是一个练习，“nester.py”模块，提供了一个名为print_lol()的函数，
这个函数的作用是打印列表，其中有可能包含（也可能不包含）嵌套列表。"""


def print_lol(the_list, indent=False, display_serial=False, level=0, serial=0, print2_files=''):
	"""这个函数取一个位置参数，名为“the_list”，这可以是任何Python列表
	（也可以是包含嵌套列表的列表）。所指定的列表中的每个数据项会（递归地）
	输出到屏幕上，各数据项各占一行。
	第二个参数（名为“indent”）用来判断是否用缩进形式表示；
	第三个参数（名为“display_serial”）用来判断是否需要显示行号；
	第四个参数（名为“level”）用来在遇到嵌套列表时插入制表符；
	第五个参数（名为“serial”）用来设置行号的起始值；
	第六个参数（名为“print2_files”)用来设置是否保存到文件（若文件名为空则打印到屏幕）	:type print2_files: object
	"""
	for _list in the_list:
		if isinstance(_list, list):
			print_lol(_list, indent, display_serial, level + 1, serial, print2_files)
		else:
			print_list = _list
			tab_num = ''
			if indent:
				for stop_tab in range(level):
					tab_num = tab_num + '\t'
				print_list = str(tab_num) + str(print_list)
			if display_serial:
				serial = serial + 1
				print_list = str(serial) + ': ' + str(print_list)
			if print2_files == '':
				print(print_list)
			else:
				print(print_list, print2_files)
