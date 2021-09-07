import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic


class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        uic.loadUi("login.ui", self)
        self.le_user.setText("Intel")
        self.btn_login.clicked.connect(self.on_clicked_login)

    def on_clicked_login(self):
        user = self.le_user.text()
        password = self.le_password.text()
        print(user, password)


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