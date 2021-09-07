import logging
import socket
import sys
import threading
import time

from Cipher import Entity
from database import MyDatabaseController

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
        self.__HOST = host
        self.__PORT = port
        self.__BUFFER = 1024
        self.__data = ""
        self.__data2 = ""
        self.bandera = None
        self.name = ""

        self.__clientes = {}
        self.__s = None
        self.__conn = None
        self.__addr = None
        self.__entity = Entity()
        self.__db = MyDatabaseController('Servidor.db')

    def __str__(self):
        info = f'--> Comunicación tipo servidor <--\n' \
               f'Instrucciones.- \n' \
               f'   Enviar:     Escriba el mensaje y pulse enter, puede enviar cuantos mensajes quiera\n' \
               f'   Recibir:    Espere el mensaje, el sistema automaticamente los mostrará\n' \
               f'   Salir:      Escriba la palabra: Salir\n'
        return info

    def __init_deamons(self):
        """Inicializamos los hilos como demonios, con el objetivo de habilitarlos durante el proceso"""
        msg_rcv = threading.Thread(target=self.__recv_msg)  # Hilo de Recepcio de mensajes
        msg_rcv.daemon = True
        msg_rcv.start()  # Iniciamos el deamon

    def __exit(self):
        """Comando para salir, cierra los comandos"""
        logging.debug('---> Gracias por usar <---')         # Mensaje de salida
        self.__s.shutdown(1)                                # Cerramos la comunicacion
        self.__s.close()                                    # Cerramos el puerto
        sys.exit()                                          # Salimos del sistema

    def run(self):
        self.name = input('¿Cual es tu nombre?')
        self.__create_socket()

    def __create_socket(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.__s:     # Abrimos el socket
                logging.debug("Socket creado con exito")                            # Mensaje de extito
                self.__wait_for_clients(1)                                          # Espereamos por los clientes
                if self.__conn:
                    self.__changing_keys()
                    self.__init_deamons()
                    self.listen_client()
        except socket.error as err:
            logging.debug(f"socket error al crear con error {err}")
            self.__exit()

    def __wait_for_clients(self, clientes: int):
        """Metodo para esperar a los clientes"""
        try:
            self.__s.settimeout(5)                              # Tiempo maximo de espera
            self.__s.bind((self.__HOST, self.__PORT))           # Esperamos en el puerto establecido
            self.__s.listen(clientes)                           # Esperamos a 'n' clientes
            logging.debug('Esperando por cliente')              # Mensaje
            while not self.__addr:
                logging.debug('...')
                self.__conn, self.__addr = self.__s.accept()    # Aceptamos a los clientes.
            print('Conexion establecida con: ', self.__addr)    # Mensaje de dirección
            print('Conexion con:', self.__conn)                 # Mensaje de conexión.
        except socket.timeout:
            logging.debug('Se expiro el tiempo')                # Mensaje de 'Time-out'
            self.__exit()                                       # Salida de SOCKET
            pass
        except:
            logging.debug('Algo salio mal al esperar a clientes') # Mensaje de salida

    def __wait_for_more_clients(self, clientes: int):
        """Metodo para esperar a los clientes"""
        try:
            while not addr:
                logging.debug('...')
                conn, addr = self.__s.accept()    # Aceptamos a los clientes.
                conn.setblocking(False)
                self.___get_name_con(name='aqui', conn=conn)
            print('Conexion establecida con: ', addr, 'addr')    # Mensaje de dirección
            print('Conexion con:', conn, 'conn')                 # Mensaje de conexión.
        except:
            logging.debug('Algo salio mal al esperar a clientes') # Mensaje de salida

    def __changing_keys(self):
        print('La llave publica es: ', self.__entity.pubkey)
        self.__conn.sendall(self.__entity.pubkey.encode('utf-8'))
        print('recibiendo llave')
        key = self.__conn.recv(self.__BUFFER)
        print('La llave recibida es:', key.decode('utf-8'))
        self.__entity.get_public_key('Cliente', key.decode('utf-8'))
        self.__db.save_key_into('Datos', self.__entity.kchain)

    def listen_client(self):
        while True:
            msg = input('-> ')
            if msg == ('salir' or 'Salir'):
                self.__exit()
            else:
                self.msg_to_all(msg)

    def msg_to_all(self, mensaje):
        try:
            text = self.__entity.encrypt_text(person='Cliente', text=mensaje)
            self.__conn.sendall(text)
            self.__db.save_msg(tabla='Mensajes', entity='This', date=time.strftime("%c"), msg=text)
        except:
            logging.debug('Algo salio mal al enviar.')
            self.__exit()

    def __recv_msg(self):
        while True:
            try:
                self.__data = self.__conn.recv(self.__BUFFER)
                if self.__data:
                    self.__db.bandera = True
                    self.__data2 = self.__entity.desencrypt_text(self.__data)
                    self.__db.datos = self.__data2
                    print("\t << ", self.__data2)
                    self.__data = None
            except:
                pass

    def ___get_name_con(self, name, conn):
        self.__clientes.update({name: conn})


if __name__ == '__main__':
    s = Servidor(host='127.0.0.1', port=40000)
    if s:
        print(s)
        s.run()
