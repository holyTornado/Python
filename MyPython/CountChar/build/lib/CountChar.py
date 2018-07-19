"""
统计指定文件文件里指定字符出现的次数！
"""

CountNum = 0
FileName = input("Please Enter a FileName(E.g:C:\\text.txt): ").strip()
FindChar = input("Please Enter Char: ")

try:
	TxtFile = open(FileName, "r")
	for each_line in TxtFile:
		NextOne = each_line.find(FindChar)
		while NextOne != -1:
			CountNum = CountNum + 1
			NextOne = each_line.find(FindChar, NextOne + 1)

	TxtFile.close()

	print("In the file [" + str(FileName) + "], the number of occurrences of the character [" + FindChar + "]: " + str(
		CountNum))
except IOError:
	print("File cannot be found!")
