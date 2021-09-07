import logging
import socket
import sys
import threading
from cifrado import Entity

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)


class Servidor:
    def __init__(self, host: str, port: int):
        self.__s = None
        self.__conn = None
        self.__addr = None
        self.__data = ""
        self.__HOST = host
        self.__PORT = port
        self.__BUFFER = 1024
        #self.__init_deamons()
        self.__entity = Entity()

    def __str__(self):
        info = f'--> Comunicación tipo servidor <--\n' \
               f'Instrucciones.- \n' \
               f'   Enviar:     Escriba el mensaje y pulse enter, puede enviar cuantos mensajes quiera\n' \
               f'   Recibir:    Espere el mensaje, el sistema automaticamente los mostrará\n' \
               f'   Salir:      Escriba la palabra: Salir\n'
        return info

    def __init_deamons(self):
        procesar = threading.Thread(target=self.recv_msg)
        procesar.daemon = True
        procesar.start()

    def exit(self):
        logging.debug('---> Gracias por usar <---')
        self.__s.shutdown(1)
        self.__s.close()
        sys.exit()

    def __wait_for_clients(self, clientes: int):
        try:
            self.__s.bind((self.__HOST, self.__PORT))
            self.__s.listen(clientes)
            logging.debug('Esperando por cliente')
            while not self.__addr:
                logging.debug('...')
                self.__conn, self.__addr = self.__s.accept()
            print('Conexion establecida con: ', self.__addr)
            print('Conexion con:', self.__conn)
            self.changing_keys()
            self.__init_deamons()
        except Exception:
            print(Exception)
            logging.debug('Algo salio mal al esperar a clientes')

    def changing_keys(self):
        print('Sending key: ')
        self.__conn.sendall(self.__entity.pubkey.encode('utf-8'))
        print('Receiving key: ')
        key = self.__conn.recv(1024)
        llave = key.decode('utf-8')
        self.__entity.get_public_key('Cliente', llave)

    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.__s:
                logging.debug("Socket creado con exito")
                self.__wait_for_clients(1)
                if self.__conn:
                    self.listen_client()
        except socket.error as err:
            logging.debug(f"socket error al crear con error {err}")
            self.exit()

    def listen_client(self):
        while True:
            msg = input('-> ')
            if msg == ('salir' or 'Salir'):
                self.exit()
            else:
                self.msg_to_all(msg)

    def msg_to_all(self, mensaje):
        try:
            self.__conn.sendall(mensaje.encode('utf-8'))
        except:
            logging.debug('Algo salio mal al enviar.')
            self.exit()

    def recv_msg(self):
        while True:
            try:
                self.__data = self.__conn.recv(1024)
                if self.__data:
                    self.msg_to_all('')
                    print("\t << ", self.__data)
                    return self.__data
            except:
                pass


if __name__ == '__main__':
    s = Servidor(host='127.0.0.1', port=40001)
    if s:
        print(s)
        s.run()
