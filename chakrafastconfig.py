# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chakrafastconfig.ui'
#
# Created: Sat Dec 31 17:10:20 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(621, 545)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 151, 201))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Chakra codec", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 130, 95, 41))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Install ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 40, 85, 21))
        self.checkBox_4.setText(QtGui.QApplication.translate("MainWindow", "Codec", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 80, 85, 21))
        self.checkBox_5.setText(QtGui.QApplication.translate("MainWindow", "flash", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 10, 151, 201))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Chakra locale", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 130, 95, 41))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 30, 131, 80))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Language system", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.comboBox = QtGui.QComboBox(self.groupBox_5)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 85, 23))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Nowy element", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(310, 10, 151, 201))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Chakra fonts", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 130, 95, 41))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Install ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.checkBox_6 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 40, 111, 21))
        self.checkBox_6.setText(QtGui.QApplication.translate("MainWindow", "Ubuntu fonts", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_7 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 70, 111, 21))
        self.checkBox_7.setText(QtGui.QApplication.translate("MainWindow", "ms fonts", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.checkBox_8 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 100, 111, 21))
        self.checkBox_8.setText(QtGui.QApplication.translate("MainWindow", "oxygen fonts", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(460, 10, 151, 201))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Chakra repo config", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox.setGeometry(QtCore.QRect(20, 40, 85, 16))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "stable", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 100, 85, 16))
        self.checkBox_2.setText(QtGui.QApplication.translate("MainWindow", "unstable", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 70, 85, 16))
        self.checkBox_3.setText(QtGui.QApplication.translate("MainWindow", "testing", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 130, 95, 41))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 220, 621, 321))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("MainWindow", "Install aplication", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 20, 301, 261))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("MainWindow", "Bundle install", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox_7)
        self.scrollArea.setGeometry(QtCore.QRect(20, 30, 261, 231))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 255, 225))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_8.setGeometry(QtCore.QRect(310, 20, 301, 261))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("MainWindow", " QT install", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.scrollArea_2 = QtGui.QScrollArea(self.groupBox_8)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 30, 261, 231))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 255, 225))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 280, 131, 23))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 280, 131, 23))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 280, 131, 23))
        self.pushButton_7.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_8.setGeometry(QtCore.QRect(160, 280, 131, 23))
        self.pushButton_8.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

