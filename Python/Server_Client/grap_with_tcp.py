import sys
import time
from PyQt5 import QtWidgets, uic
import threading

from Server_grap import Servidor
from entrada import Ui_MainWindow


class ChatWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(ChatWindow, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_send.clicked.connect(self.on_clicked_login)
        self.tcp = Servidor(host='127.0.0.1', port=40001)

        self.__init_deamons()

    def __init_deamons(self):
        procesar = threading.Thread(target=self.tcp.run)
        procesar.daemon = True
        procesar.start()

        mostrar = threading.Thread(target=self.tcp2window)
        mostrar.daemon = True
        mostrar.start()

    def tcp2window(self):
        while True:
            try:
                msg = self.tcp.recv_msg()
                mensaje = msg.decode('utf-8')
                self.receiver_msg(mensaje)
            except:
                pass

    def write_text(self, msg: str):
        self.ui.text_revc.insertPlainText(msg)


    def on_clicked_login(self):
        text = self.ui.text_send.toPlainText()
        self.tcp.msg_to_all(text)
        localtime = time.asctime(time.localtime(time.time()))
        self.write_text(msg=f"{localtime} >> {text}\n")
        print(f"{localtime} >> {text}")
        self.ui.text_send.clear()

    def receiver_msg(self, msg: str):
        localtime = time.asctime(time.localtime(time.time()))
        self.write_text(msg=f"\t{localtime} << {msg}\n")

    def keyPressEvent(self, event):
        from PyQt5.QtCore import Qt
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = ChatWindow()
        window.show()
        app.exec()
        sys.exit(0)

    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        window.tcp.exit()
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])