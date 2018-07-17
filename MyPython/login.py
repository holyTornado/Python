# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Login")
		Form.resize(282, 118)
		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(60, 30, 54, 12))
		self.label.setObjectName("label")
		self.pushButton = QtWidgets.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(150, 60, 75, 23))
		self.pushButton.setObjectName("pushButton")
		self.checkBox = QtWidgets.QCheckBox(Form)
		self.checkBox.setGeometry(QtCore.QRect(50, 60, 71, 16))
		self.checkBox.setObjectName("checkBox")
		self.lineEdit = QtWidgets.QLineEdit(Form)
		self.lineEdit.setGeometry(QtCore.QRect(120, 20, 113, 20))
		self.lineEdit.setObjectName("lineEdit")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "[Login]"))
		self.label.setText(_translate("Form", "密码："))
		self.pushButton.setText(_translate("Form", "确定"))
		self.checkBox.setText(_translate("Form", "记住密码"))


if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	widget = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(widget)
	widget.show()
	sys.exit(app.exec_())
