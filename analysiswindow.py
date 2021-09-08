# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alphavuemain.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class analysisWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1700, 854)
        Form.setMinimumSize(QtCore.QSize(1700, 800))
        Form.setMaximumSize(QtCore.QSize(1682, 854))
        self.descriptionGroup = QtWidgets.QGroupBox(Form)
        self.descriptionGroup.setGeometry(QtCore.QRect(270, 20, 1061, 191))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.descriptionGroup.setFont(font)
        self.descriptionGroup.setObjectName("descriptionGroup")
        self.descriptionText = QtWidgets.QLabel(self.descriptionGroup)
        self.descriptionText.setGeometry(QtCore.QRect(10, 30, 791, 141))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.descriptionText.setFont(font)
        self.descriptionText.setTextFormat(QtCore.Qt.AutoText)
        self.descriptionText.setScaledContents(True)
        self.descriptionText.setWordWrap(True)
        self.descriptionText.setObjectName("descriptionText")
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(50, 140, 151, 31))
        self.closeButton.setObjectName("closeButton")
        self.helpButton = QtWidgets.QPushButton(Form)
        self.helpButton.setGeometry(QtCore.QRect(50, 180, 151, 31))
        self.helpButton.setObjectName("helpButton")
        self.tickercodeLabel = QtWidgets.QLabel(Form)
        self.tickercodeLabel.setGeometry(QtCore.QRect(30, 30, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.tickercodeLabel.setFont(font)
        self.tickercodeLabel.setMidLineWidth(1)
        self.tickercodeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tickercodeLabel.setWordWrap(False)
        self.tickercodeLabel.setObjectName("tickercodeLabel")
        self.generalGroup = QtWidgets.QGroupBox(Form)
        self.generalGroup.setGeometry(QtCore.QRect(30, 230, 211, 601))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.generalGroup.setFont(font)
        self.generalGroup.setObjectName("generalGroup")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.generalGroup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 223, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.countryLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.countryLabel.setFont(font)
        self.countryLabel.setObjectName("countryLabel")
        self.verticalLayout.addWidget(self.countryLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.exchangeLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exchangeLabel.setFont(font)
        self.exchangeLabel.setObjectName("exchangeLabel")
        self.verticalLayout.addWidget(self.exchangeLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.currencyLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currencyLabel.setFont(font)
        self.currencyLabel.setObjectName("currencyLabel")
        self.verticalLayout.addWidget(self.currencyLabel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.industryLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.industryLabel.setFont(font)
        self.industryLabel.setScaledContents(True)
        self.industryLabel.setWordWrap(True)
        self.industryLabel.setObjectName("industryLabel")
        self.verticalLayout.addWidget(self.industryLabel)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.ceoLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ceoLabel.setFont(font)
        self.ceoLabel.setObjectName("ceoLabel")
        self.verticalLayout.addWidget(self.ceoLabel)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.employeesLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employeesLabel.setFont(font)
        self.employeesLabel.setObjectName("employeesLabel")
        self.verticalLayout.addWidget(self.employeesLabel)
        self.incomeGroup = QtWidgets.QGroupBox(Form)
        self.incomeGroup.setGeometry(QtCore.QRect(270, 230, 471, 601))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.incomeGroup.setFont(font)
        self.incomeGroup.setObjectName("incomeGroup")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.incomeGroup)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 50, 151, 541))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.line_6 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_2.addWidget(self.line_6)
        self.line_5 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.incomeGroup)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(210, 50, 115, 541))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cyRevenueLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cyRevenueLabel.setFont(font)
        self.cyRevenueLabel.setObjectName("cyRevenueLabel")
        self.verticalLayout_3.addWidget(self.cyRevenueLabel)
        self.cyCostOfRevenueLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cyCostOfRevenueLabel.setFont(font)
        self.cyCostOfRevenueLabel.setObjectName("cyCostOfRevenueLabel")
        self.verticalLayout_3.addWidget(self.cyCostOfRevenueLabel)
        self.line_7 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_3.addWidget(self.line_7)
        self.cyGrossProfitLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cyGrossProfitLabel.setFont(font)
        self.cyGrossProfitLabel.setObjectName("cyGrossProfitLabel")
        self.verticalLayout_3.addWidget(self.cyGrossProfitLabel)
        self.cyInterestIncomeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cyInterestIncomeLabel.setFont(font)
        self.cyInterestIncomeLabel.setObjectName("cyInterestIncomeLabel")
        self.verticalLayout_3.addWidget(self.cyInterestIncomeLabel)
        self.cySubtotalLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cySubtotalLabel.setFont(font)
        self.cySubtotalLabel.setObjectName("cySubtotalLabel")
        self.verticalLayout_3.addWidget(self.cySubtotalLabel)
        self.line_8 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_3.addWidget(self.line_8)
        self.cySgaLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cySgaLabel.setFont(font)
        self.cySgaLabel.setObjectName("cySgaLabel")
        self.verticalLayout_3.addWidget(self.cySgaLabel)
        self.cyRdLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cyRdLabel.setFont(font)
        self.cyRdLabel.setObjectName("cyRdLabel")
        self.verticalLayout_3.addWidget(self.cyRdLabel)
        self.cyTotalExpLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cyTotalExpLabel.setFont(font)
        self.cyTotalExpLabel.setObjectName("cyTotalExpLabel")
        self.verticalLayout_3.addWidget(self.cyTotalExpLabel)
        self.line_10 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_3.addWidget(self.line_10)
        self.cyNetProfitLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cyNetProfitLabel.setFont(font)
        self.cyNetProfitLabel.setObjectName("cyNetProfitLabel")
        self.verticalLayout_3.addWidget(self.cyNetProfitLabel)
        self.line_9 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_3.addWidget(self.line_9)
        self.cyProfitTaxLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cyProfitTaxLabel.setFont(font)
        self.cyProfitTaxLabel.setObjectName("cyProfitTaxLabel")
        self.verticalLayout_3.addWidget(self.cyProfitTaxLabel)
        self.line_12 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_3.addWidget(self.line_12)
        self.line_11 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_3.addWidget(self.line_11)
        self.cyLabel = QtWidgets.QLabel(self.incomeGroup)
        self.cyLabel.setGeometry(QtCore.QRect(230, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cyLabel.setFont(font)
        self.cyLabel.setObjectName("cyLabel")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.incomeGroup)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(340, 50, 115, 541))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pyRevenueLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pyRevenueLabel.setFont(font)
        self.pyRevenueLabel.setObjectName("pyRevenueLabel")
        self.verticalLayout_4.addWidget(self.pyRevenueLabel)
        self.pyCostOfRevenueLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pyCostOfRevenueLabel.setFont(font)
        self.pyCostOfRevenueLabel.setObjectName("pyCostOfRevenueLabel")
        self.verticalLayout_4.addWidget(self.pyCostOfRevenueLabel)
        self.line_13 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout_4.addWidget(self.line_13)
        self.pyGrossProfitLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pyGrossProfitLabel.setFont(font)
        self.pyGrossProfitLabel.setObjectName("pyGrossProfitLabel")
        self.verticalLayout_4.addWidget(self.pyGrossProfitLabel)
        self.pyInterestIncomeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pyInterestIncomeLabel.setFont(font)
        self.pyInterestIncomeLabel.setObjectName("pyInterestIncomeLabel")
        self.verticalLayout_4.addWidget(self.pyInterestIncomeLabel)
        self.pySubtotalLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pySubtotalLabel.setFont(font)
        self.pySubtotalLabel.setObjectName("pySubtotalLabel")
        self.verticalLayout_4.addWidget(self.pySubtotalLabel)
        self.line_14 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_4.addWidget(self.line_14)
        self.pySgaLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pySgaLabel.setFont(font)
        self.pySgaLabel.setObjectName("pySgaLabel")
        self.verticalLayout_4.addWidget(self.pySgaLabel)
        self.pyRdLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pyRdLabel.setFont(font)
        self.pyRdLabel.setObjectName("pyRdLabel")
        self.verticalLayout_4.addWidget(self.pyRdLabel)
        self.pyTotalExpLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pyTotalExpLabel.setFont(font)
        self.pyTotalExpLabel.setObjectName("pyTotalExpLabel")
        self.verticalLayout_4.addWidget(self.pyTotalExpLabel)
        self.line_15 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.verticalLayout_4.addWidget(self.line_15)
        self.pyNetProfitLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pyNetProfitLabel.setFont(font)
        self.pyNetProfitLabel.setObjectName("pyNetProfitLabel")
        self.verticalLayout_4.addWidget(self.pyNetProfitLabel)
        self.line_16 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.verticalLayout_4.addWidget(self.line_16)
        self.pyProfitTaxLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pyProfitTaxLabel.setFont(font)
        self.pyProfitTaxLabel.setObjectName("pyProfitTaxLabel")
        self.verticalLayout_4.addWidget(self.pyProfitTaxLabel)
        self.line_17 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.verticalLayout_4.addWidget(self.line_17)
        self.line_18 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.verticalLayout_4.addWidget(self.line_18)
        self.pyLabel = QtWidgets.QLabel(self.incomeGroup)
        self.pyLabel.setGeometry(QtCore.QRect(360, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pyLabel.setFont(font)
        self.pyLabel.setObjectName("pyLabel")
        self.balancegroup = QtWidgets.QGroupBox(Form)
        self.balancegroup.setGeometry(QtCore.QRect(1360, 20, 311, 501))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.balancegroup.setFont(font)
        self.balancegroup.setObjectName("balancegroup")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.balancegroup)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 40, 157, 441))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_5.addWidget(self.label_20)
        self.line_19 = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.verticalLayout_5.addWidget(self.line_19)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_5.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_5.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        self.line_20 = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.verticalLayout_5.addWidget(self.line_20)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_5.addWidget(self.label_24)
        self.line_22 = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.verticalLayout_5.addWidget(self.line_22)
        self.line_21 = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.verticalLayout_5.addWidget(self.line_21)
        self.label_25 = QtWidgets.QLabel(self.balancegroup)
        self.label_25.setGeometry(QtCore.QRect(220, 20, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.balancegroup)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(200, 40, 91, 441))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.caLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.caLabel.setFont(font)
        self.caLabel.setObjectName("caLabel")
        self.verticalLayout_6.addWidget(self.caLabel)
        self.ncLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ncLabel.setFont(font)
        self.ncLabel.setObjectName("ncLabel")
        self.verticalLayout_6.addWidget(self.ncLabel)
        self.taLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.taLabel.setFont(font)
        self.taLabel.setObjectName("taLabel")
        self.verticalLayout_6.addWidget(self.taLabel)
        self.line_24 = QtWidgets.QFrame(self.verticalLayoutWidget_6)
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.verticalLayout_6.addWidget(self.line_24)
        self.clLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clLabel.setFont(font)
        self.clLabel.setObjectName("clLabel")
        self.verticalLayout_6.addWidget(self.clLabel)
        self.nclLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nclLabel.setFont(font)
        self.nclLabel.setObjectName("nclLabel")
        self.verticalLayout_6.addWidget(self.nclLabel)
        self.tlLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tlLabel.setFont(font)
        self.tlLabel.setObjectName("tlLabel")
        self.verticalLayout_6.addWidget(self.tlLabel)
        self.line_23 = QtWidgets.QFrame(self.verticalLayoutWidget_6)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.verticalLayout_6.addWidget(self.line_23)
        self.oeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.oeLabel.setFont(font)
        self.oeLabel.setObjectName("oeLabel")
        self.verticalLayout_6.addWidget(self.oeLabel)
        self.line_26 = QtWidgets.QFrame(self.verticalLayoutWidget_6)
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.verticalLayout_6.addWidget(self.line_26)
        self.line_25 = QtWidgets.QFrame(self.verticalLayoutWidget_6)
        self.line_25.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.verticalLayout_6.addWidget(self.line_25)
        self.chartgrroup = QtWidgets.QGroupBox(Form)
        self.chartgrroup.setGeometry(QtCore.QRect(770, 230, 561, 601))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chartgrroup.setFont(font)
        self.chartgrroup.setObjectName("chartgrroup")
        self.stockChartLabel = QtWidgets.QLabel(self.chartgrroup)
        self.stockChartLabel.setGeometry(QtCore.QRect(10, 32, 541, 551))
        self.stockChartLabel.setText("")
        self.stockChartLabel.setObjectName("stockChartLabel")
        self.imageLabel = QtWidgets.QLabel(Form)
        self.imageLabel.setGeometry(QtCore.QRect(1380, 550, 255, 255)) #change from 255
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AlphaVue Stock Analysis"))
        self.descriptionGroup.setTitle(_translate("Form", "Description"))
        self.descriptionText.setText(_translate("Form", "detailed description NA"))
        self.closeButton.setText(_translate("Form", "Close"))
        self.helpButton.setText(_translate("Form", "Help"))
        self.tickercodeLabel.setText(_translate("Form", "TSLA"))
        self.generalGroup.setTitle(_translate("Form", "General information"))
        self.label_4.setText(_translate("Form", "Name:"))
        self.nameLabel.setText(_translate("Form", "Error retrieving Name"))
        self.label_2.setText(_translate("Form", "Country:"))
        self.countryLabel.setText(_translate("Form", "Error retrieving Country"))
        self.label.setText(_translate("Form", "Exchange:"))
        self.exchangeLabel.setText(_translate("Form", "Error retrieving Exchange"))
        self.label_3.setText(_translate("Form", "Currency:"))
        self.currencyLabel.setText(_translate("Form", "Error retrieving Currency"))
        self.label_5.setText(_translate("Form", "Industry:"))
        self.industryLabel.setText(_translate("Form", "Error retrieving Industry"))
        self.label_6.setText(_translate("Form", "CEO:"))
        self.ceoLabel.setText(_translate("Form", "Error retrieving CEO"))
        self.label_7.setText(_translate("Form", "Employees:"))
        self.employeesLabel.setText(_translate("Form", "Error retrieving Employees"))
        self.incomeGroup.setTitle(_translate("Form", "Income Statement"))
        self.label_8.setText(_translate("Form", "Revenue"))
        self.label_9.setText(_translate("Form", "   Cost of Revenue"))
        self.label_10.setText(_translate("Form", "Gross Profit"))
        self.label_11.setText(_translate("Form", "Interest Income"))
        self.label_17.setText(_translate("Form", "   Subtotal"))
        self.label_12.setText(_translate("Form", "Selling, General & Administration "))
        self.label_13.setText(_translate("Form", "Research & Development"))
        self.label_16.setText(_translate("Form", "   Total expenses"))
        self.label_14.setText(_translate("Form", "Net profit"))
        self.label_15.setText(_translate("Form", "Profit (minus tax)"))
        self.cyRevenueLabel.setText(_translate("Form", "$10,000 NA"))
        self.cyCostOfRevenueLabel.setText(_translate("Form", "($2,000) NA"))
        self.cyGrossProfitLabel.setText(_translate("Form", "$8,000 NA"))
        self.cyInterestIncomeLabel.setText(_translate("Form", "$100 NA"))
        self.cySubtotalLabel.setText(_translate("Form", "  $8,100 NA"))
        self.cySgaLabel.setText(_translate("Form", "($1,000) NA"))
        self.cyRdLabel.setText(_translate("Form", "($2,500) NA"))
        self.cyTotalExpLabel.setText(_translate("Form", "   ($3,500) NA"))
        self.cyNetProfitLabel.setText(_translate("Form", "$4,600 NA"))
        self.cyProfitTaxLabel.setText(_translate("Form", "$3,000 NA"))
        self.cyLabel.setText(_translate("Form", "2021"))
        self.pyRevenueLabel.setText(_translate("Form", "$10,000 NA"))
        self.pyCostOfRevenueLabel.setText(_translate("Form", "($2,000) NA"))
        self.pyGrossProfitLabel.setText(_translate("Form", "$8,000 NA"))
        self.pyInterestIncomeLabel.setText(_translate("Form", "$100 NA"))
        self.pySubtotalLabel.setText(_translate("Form", "  $8,100 NA"))
        self.pySgaLabel.setText(_translate("Form", "($1,000) NA"))
        self.pyRdLabel.setText(_translate("Form", "($2,500) NA"))
        self.pyTotalExpLabel.setText(_translate("Form", "   ($3,500) NA"))
        self.pyNetProfitLabel.setText(_translate("Form", "$4,600 NA"))
        self.pyProfitTaxLabel.setText(_translate("Form", "$3,000 NA"))
        self.pyLabel.setText(_translate("Form", "2020"))
        self.balancegroup.setTitle(_translate("Form", "Balance sheet"))
        self.label_18.setText(_translate("Form", "Current assets"))
        self.label_19.setText(_translate("Form", "Non-current assets"))
        self.label_20.setText(_translate("Form", "   Total assets"))
        self.label_21.setText(_translate("Form", "Current liabillities"))
        self.label_22.setText(_translate("Form", "Non-current liabillities"))
        self.label_23.setText(_translate("Form", "   Total liabillities"))
        self.label_24.setText(_translate("Form", "Owners Equity"))
        self.label_25.setText(_translate("Form", "2021"))
        self.caLabel.setText(_translate("Form", "$2000 NA"))
        self.ncLabel.setText(_translate("Form", "$2000 NA"))
        self.taLabel.setText(_translate("Form", "$4000 NA"))
        self.clLabel.setText(_translate("Form", "$1000 NA"))
        self.nclLabel.setText(_translate("Form", "$500 NA"))
        self.tlLabel.setText(_translate("Form", "$1500 NA"))
        self.oeLabel.setText(_translate("Form", "$2500 NA"))
        self.chartgrroup.setTitle(_translate("Form", "Stock price chart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
