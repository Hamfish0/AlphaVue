# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class searchWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(992, 595)
        Form.setMinimumSize(QtCore.QSize(992, 595))
        Form.setMaximumSize(QtCore.QSize(992, 595))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 10, 481, 131))
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(380, 120, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 560, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(360, 170, 261, 371))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.searchButton = QtWidgets.QPushButton(self.groupBox)
        self.searchButton.setGeometry(QtCore.QRect(20, 170, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.helpButton = QtWidgets.QPushButton(self.groupBox)
        self.helpButton.setGeometry(QtCore.QRect(20, 230, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.helpButton.setFont(font)
        self.helpButton.setObjectName("helpButton")
        self.exitButton = QtWidgets.QPushButton(self.groupBox)
        self.exitButton.setGeometry(QtCore.QRect(20, 290, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.tickerLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.tickerLineEdit.setGeometry(QtCore.QRect(20, 20, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.tickerLineEdit.setFont(font)
        self.tickerLineEdit.setText("")
        self.tickerLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.tickerLineEdit.setObjectName("tickerLineEdit")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(830, 500, 161, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.searchStatus = QtWidgets.QLabel(Form)
        self.searchStatus.setGeometry(QtCore.QRect(20, 160, 301, 211))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.searchStatus.setFont(font)
        self.searchStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.searchStatus.setWordWrap(True)
        self.searchStatus.setObjectName("searchStatus")
        self.searchStatus_2 = QtWidgets.QLabel(Form)
        self.searchStatus_2.setGeometry(QtCore.QRect(20, 330, 301, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchStatus_2.setFont(font)
        self.searchStatus_2.setAlignment(QtCore.Qt.AlignCenter)
        self.searchStatus_2.setWordWrap(True)
        self.searchStatus_2.setObjectName("searchStatus_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "AlphaVue"))
        self.label_2.setText(_translate("Form", "US Stock Analysis v2.0"))
        self.label_3.setText(_translate("Form", "by Hamish Anderson | Computer Science 2021"))
        self.searchButton.setText(_translate("Form", "Search"))
        self.helpButton.setText(_translate("Form", "Help"))
        self.exitButton.setText(_translate("Form", "Exit"))
        self.label_4.setText(_translate("Form", "Enter a US stock ticker code in the textfield above."))
        self.label_5.setText(_translate("Form", "Data dependent on IEXcloud API"))
        self.searchStatus.setText(_translate("Form", "Search usually takes ~8 seconds, depending on usage of the IEXcloud API, during this time window may be unresponsive."))
        self.searchStatus_2.setText(_translate("Form", "Future versions will have threading to solve this problem"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
