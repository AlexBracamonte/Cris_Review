import socket
import threading
import sys
import logging
from Cipher import Entity
import time
from database import MyDatabaseController


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)


class Clients:
    def __init__(self, host: str, port: int):
        self.__HOST = host
        self.__PORT = port
        self.__BUFFER = 1024
        self.__data = ""
        self.__data2 = ""

        self.__sock = None
        self.__entity = Entity()
        self.__db = MyDatabaseController('Cliente.db')


    def __str__(self):
        info = f'--> Comunicación tipo cliente <--\n' \
               f'Datos --> {self.__entity}' \
               f'Instrucciones.- \n' \
               f'   Enviar:     Escriba el mensaje y pulse enter, puede enviar cuantos mensajes quiera\n' \
               f'   Recibir:    Espere el mensaje, el sistema automaticamente los mostrará\n' \
               f'   Salir:      Escriba la palabra: Salir\n'
        return info

    def __init_threads(self):
        msg_recv = threading.Thread(target=self.__msg_recv)
        msg_recv.daemon = True
        msg_recv.start()

    def __listen_server(self):
        while True:
            msg = input('-> ')
            if msg == ('salir' or 'Salir'):
                self.__exit()
            else:
                self.__send_msg(msg)

    def run(self):
        self.__create_socket()

    def __create_socket(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.__sock:
                self.__sock.connect((self.__HOST, self.__PORT))
                self.__changing_keys()
                self.__init_threads()
                self.__listen_server()

        except socket.error as err:
            logging.debug(f"socket error al crear con error {err}")

        finally:
            self.__exit()

    def __msg_recv(self):
        while True:
            try:
                self.__data = self.__sock.recv(self.__BUFFER)
                if self.__data:
                    text = self.__data
                    self.__data2 = self.__entity.desencrypt_text(self.__data)
                    print("\t << ", self.__data2)
                    self.__db.save_msg(tabla='Mensajes', entity='Servidor', date=time.strftime("%c"), msg='text')
                    self.__data = None
            except:
                pass

    def __send_msg(self, msg):
        try:
            text = self.__entity.encrypt_text(person='Servidor', text=msg)
            self.__sock.sendall(text)
            self.__db.save_msg(tabla='Mensajes', entity='This', date=time.strftime("%c"), msg=text)
        except:
            logging.debug('Algo salio mal al enviar.')

    def __changing_keys(self):
        print('Recibiendo llave')
        self.__sock.sendall(self.name.encode('utf-8'))
        person = self.__sock.recv(self.__BUFFER)

        self.__sock.sendall(self.__entity.pubkey.encode('utf-8'))
        print('')
        print('')
        key = self.__sock.recv(self.__BUFFER)
        self.__entity.get_public_key(person.decode('utf-8'), key.decode('utf-8'))

        print(person.decode('utf-8'), key.decode('utf-8'))
        print('Recibiendo llave')
        print('La llave recibida es:', key.decode('utf-8'))

    def __exit(self):
        logging.debug('--> Gracias por usar <--')
        self.__sock.close()
        sys.exit()


if __name__ == '__main__':
    c = Clients(host='127.0.0.1', port=40000)
    if c:
        print(c)
    c.run()
