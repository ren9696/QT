# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\工作\485上位机\tool_by_qt\ShowDataWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowdataWindow(object):
    def setupUi(self, ShowdataWindow):
        ShowdataWindow.setObjectName("ShowdataWindow")
        ShowdataWindow.resize(1049, 769)
        ShowdataWindow.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(ShowdataWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(ShowdataWindow)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(ShowdataWindow)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_7 = QtWidgets.QLabel(ShowdataWindow)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(ShowdataWindow)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(ShowdataWindow)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(ShowdataWindow)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(ShowdataWindow)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(ShowdataWindow)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_9 = QtWidgets.QLabel(ShowdataWindow)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(ShowdataWindow)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_10 = QtWidgets.QLabel(ShowdataWindow)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(ShowdataWindow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1029, 701))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(ShowdataWindow)
        QtCore.QMetaObject.connectSlotsByName(ShowdataWindow)

    def retranslateUi(self, ShowdataWindow):
        _translate = QtCore.QCoreApplication.translate
        ShowdataWindow.setWindowTitle(_translate("ShowdataWindow", "Form"))
        self.pushButton.setText(_translate("ShowdataWindow", "PushButton"))
        self.label_3.setText(_translate("ShowdataWindow", "设备地址"))
        self.label_7.setText(_translate("ShowdataWindow", "未获取"))
        self.label.setText(_translate("ShowdataWindow", "波特率"))
        self.label_6.setText(_translate("ShowdataWindow", "未获取"))
        self.label_5.setText(_translate("ShowdataWindow", "IMEI"))
        self.label_8.setText(_translate("ShowdataWindow", "未获取"))
        self.label_2.setText(_translate("ShowdataWindow", "网络信号"))
        self.label_9.setText(_translate("ShowdataWindow", "未获取"))
        self.label_4.setText(_translate("ShowdataWindow", "网络状态"))
        self.label_10.setText(_translate("ShowdataWindow", "未获取"))
