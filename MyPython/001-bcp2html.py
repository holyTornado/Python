TableData = []
CountNum = 0


def funGetColumn(RowData):
	ColData = []
	NextCol = RowData.find("@ts@")
	while NextCol > 0:
		(OneCol, tempCol) = RowData.split("@ts@", 1)
		ColData.append(OneCol)
		RowData = tempCol
		NextCol = RowData.find("@ts@")

	return ColData


BcpFile = open("D:\\code_seat_second.txt")
try:
	for each_line in BcpFile:
		NextOne = each_line.find("#ts#")
		while NextOne > 0:
			(current_row, temp) = each_line.split("#ts#", 1)
			CountNum = CountNum + 1
			TableData.append([CountNum, funGetColumn(current_row)])
			each_line = temp
			NextOne = each_line.find("#ts#")

	BcpFile.close()
except IOError:
	print("数据文件丢失了!")

htmlFile = open("code_seat_second.html", "w")
print(TableData, file=htmlFile)
htmlFile.close()

for recording in TableData:
	if isinstance(recording, list):
		for column in recording:
			print(column)
