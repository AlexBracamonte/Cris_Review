# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entrada.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 400)
        MainWindow.setMaximumSize(QtCore.QSize(550, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(200, 10, 117, 17))
        self.info.setObjectName("info")
        self.text_revc = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_revc.setGeometry(QtCore.QRect(20, 40, 431, 241))
        self.text_revc.setObjectName("text_revc")
        self.button_send = QtWidgets.QPushButton(self.centralwidget)
        self.button_send.setGeometry(QtCore.QRect(460, 308, 80, 25))
        self.button_send.setObjectName("button_send")
        self.text_send = QtWidgets.QTextEdit(self.centralwidget)
        self.text_send.setGeometry(QtCore.QRect(21, 291, 431, 59))
        self.text_send.setObjectName("text_send")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "INTEL - INAOE"))
        self.info.setText(_translate("MainWindow", "Alex Bracamonte"))
        self.button_send.setText(_translate("MainWindow", "Enviar"))
