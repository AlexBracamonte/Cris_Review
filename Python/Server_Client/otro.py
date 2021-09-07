import sys
from PyQt5.QtWidgets import QApplication, QDialog
from Ui_login import Ui_login


class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.le_validators()
        self.ui.btn_login.clicked.connect(self.on_clicked_login)

    def le_validators(self):
        from PyQt5.QtGui import QRegExpValidator
        from PyQt5.QtCore import QRegExp
        from PyQt5.QtWidgets import QLineEdit
        only_text = QRegExpValidator(QRegExp('^[A-Za-z]{4,8}'))
        only_numbers = QRegExpValidator(QRegExp('^[0-9]{4,8}'))
        self.ui.le_user.setValidator(only_text)
        self.ui.le_password.setValidator(only_numbers)
        for line_edit in self.findChildren(QLineEdit):
            line_edit.textChanged.connect(self.check_changes)
            line_edit.textChanged.emit(line_edit.text())

    def check_changes(self):
        from PyQt5.QtGui import QValidator
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if state == QValidator.Acceptable:
            color = '#59cf8f'
        else:
            color = '#fe3e23'
        sender.setStyleSheet('QLineEdit{ background-color:'+color+'}')

    def on_clicked_login(self):
        from PyQt5.QtWidgets import QMessageBox
        user = self.ui.le_user.text()
        password = self.ui.le_password.text()
        if user == "admin" and password == "1234":
            QMessageBox.information(self, "Success", "You're logged")
        else:
            QMessageBox.warning(self, "Error", "You're not logged")

    def keyPressEvent(self, event):
        from PyQt5.QtCore import Qt
        if event.key() == Qt.Key_Escape:
            self.close()

    def mouseDoubleClickEvent(self, event):
        self.close()


if __name__ == "__main__":
    try:
        myApp = QApplication(sys.argv)
        myWidget = Login()
        myWidget.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])

