import logging
import socket
import sys
import threading
from cifrado import Entity

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
)


class Server:
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
        info = f'--> Comunicación tipo servidor <--\n' \
               f'Instrucciones.- \n' \
               f'   Enviar:     Escriba el mensaje y pulse enter, puede enviar cuantos mensajes quiera\n' \
               f'   Recibir:    Espere el mensaje, el sistema automaticamente los mostrará\n' \
               f'   Salir:      Escriba la palabra: Salir\n'
        return info

    def __init_deamons(self):
        procesar = threading.Thread(target=self.__recv_msg)
        procesar.daemon = True
        procesar.start()

    def run(self):
        self.__create_socket()

    def __create_socket(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.__s:
                logging.debug("Socket creado con exito")
                self.__wait_for_clients(1)
                if self.__conn:
                    self.__changing_keys()
                    self.__init_deamons()
                    self.__listen_client()
        except socket.error as err:
            logging.debug(f"socket error al crear con error {err}")
            self.__exit()

    def __wait_for_clients(self, clientes: int):
        self.__s.bind((self.__HOST, self.__PORT))
        self.__s.listen(clientes)
        logging.debug('Esperando por cliente')
        while not self.__addr:
            logging.debug('...')
            self.__conn, self.__addr = self.__s.accept()
        logging.debug('Conexion establecida')
        print('Conexion establecida con: ', self.__addr)

    def __changing_keys(self):
        print('La llave publica es: ', self.__entity.pubkey)
        self.__conn.sendall(self.__entity.pubkey.encode('utf-8'))
        print('recibiendo llave')
        key = self.__conn.recv(self.__BUFFER)
        print('La llave recibida es:', key.decode('utf-8'))
        self.__entity.get_public_key('Cliente', key.decode('utf-8'))

    def __listen_client(self):
        while True:
            msg = input('-> ')
            if msg == ('salir' or 'Salir'):
                self.__exit()
            else:
                self.msg_to_all(msg)

    def __recv_msg(self):
        while True:
            try:
                self.__data = self.__conn.recv(1024)
                if self.__data:
                    self.msg_to_all('')
                    print("\t << ", self.__data)
            except:
                pass

    def listen_client(self):
        while True:
            msg = input('-> ')
            if msg == ('salir' or 'Salir'):
                self.__exit()
            else:
                self.msg_to_all(msg)

    def msg_to_all(self, mensaje):
        try:
            self.__conn.sendall(mensaje.encode('utf-8'))
        except Exception:
            logging.debug('Algo salio mal al enviar.')
            self.__exit()

    def __exit(self):
        logging.debug('---> Gracias por usar <---')
        self.__s.shutdown(1)
        self.__s.close()
        sys.exit()


if __name__ == '__main__':
    s = Server(host='127.0.0.1', port=40001)
    if s:
        print(s)
        s.run()
