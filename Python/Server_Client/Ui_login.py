# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(250, 300)
        dialog.setMinimumSize(QtCore.QSize(250, 150))
        dialog.setMaximumSize(QtCore.QSize(250, 300))
        self.layoutWidget = QtWidgets.QWidget(dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 221, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.le_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_password.setObjectName("le_password")
        self.gridLayout.addWidget(self.le_password, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_user = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_user.setObjectName("le_user")
        self.gridLayout.addWidget(self.le_user, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.btn_login = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_login.setObjectName("btn_login")
        self.verticalLayout.addWidget(self.btn_login)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Ejemplo"))
        self.label_2.setText(_translate("dialog", "Password"))
        self.label.setText(_translate("dialog", "Username"))
        self.btn_login.setText(_translate("dialog", "Login"))