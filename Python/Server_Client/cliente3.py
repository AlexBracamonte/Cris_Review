import logging
import socket
import sys
import threading
from cifrado import Entity


LOG_FILENAME = 'logging_cliente.out'
logging.basicConfig(
    format='%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s',
    level=logging.INFO)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-2s - %(message)s',
)


class Clients:
    def __init__(self, host: str, port: int):
        self.__HOST = host
        self.__PORT = port
        self.__BUFFER = 1024
        self.__data = ""

        self.__s = None
        self.__conn = None
        self.__addr = None

        self.__entity = Entity()

    def __str__(self):
        info = f'--> Comunicación tipo cliente <--\n' \
               f'Instrucciones.- \n' \
               f'   Enviar:     Escriba el mensaje y pulse enter, puede enviar cuantos mensajes quiera\n' \
               f'   Recibir:    Espere el mensaje, el sistema automaticamente los mostrará\n' \
               f'   Salir:      Escriba la palabra: Salir\n'
        return info

    def __init_threads(self):
        msg_recv = threading.Thread(target=self.__msg_recv)
        msg_recv.daemon = True
        msg_recv.start()

    def run(self):
        self.__create_socket()
        self.__init_threads()
        self.__listen_server()

    def __create_socket(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.__sock:
                self.__sock.connect((self.__HOST, self.__PORT))
                self.__changing_keys()

        except socket.error as err:
            logging.debug(f"socket error al crear con error {err}")

    def __msg_recv(self):
        while True:
            try:
                self.data = self.__sock.recv(self.__BUFFER)
                if self.data:
                    self.__send_msg('')
                    print("\t << ", self.data)
            except:
                pass

    def __send_msg(self, msg):
        self.__sock.sendall(msg.encode('utf-8'))
        #except:
        #    logging.debug('Algo salio mal al enviar.')

    def __listen_server(self):
        while True:
            msg = input('-> ')
            if msg == ('salir' or 'Salir'):
                self.__exit()
            else:
                self.__send_msg(msg)

    def __changing_keys(self):
        print('recibiendo llave')
        llave = self.__sock.recv(self.__BUFFER).decode('utf-8')
        print('La llave recibida es:', llave)
        self.__entity.get_public_key('Servidor', llave)
        print('La llave publica es: ', self.__entity.pubkey)
        self.__sock.sendall(self.__entity.pubkey.encode('utf-8'))

    def __exit(self):
        logging.debug('--> Gracias por usar <--')
        self.__sock.close()
        sys.exit()


if __name__ == '__main__':
    c = Clients(host='127.0.0.1', port=40001)
    if c:
        print(c)
    c.run()
