import sqlite3
from sqlite3 import Error
from os import error
import time
import threading


class MyDatabaseController:
    def __init__(self, name: str):
        self.datos = None
        self.__name = name
        self.__con = None
        self.__cursor = None
        self.flag = None
        self.info_key = None

        self.__delete_database(name)
        self.__create_db()
        self.__init_deamons()

        self.info_key = None

    def __create_db(self):
        if self.__name[-3:] == '.db':
            self.__con = sqlite3.connect(self.__name)
            self.__cursor = self.__con.cursor()
            self.con2 = self.__con
            self.cursor2 = self.__cursor
            if self.__con:
                print(f'Base de datos: {self.__name} creada con exito')
                self.__con.commit()
                #text_table = {"Datos": {"Entidad": "varchar(100)", "Kp": "BLOB"}}
                text_table = {"Datos": {"Entidad": "varchar(100)", "Kp": "TEXT"}}
                self.__create_tables(text_table)
                text_table = {"Mensajes": {"Entidad": "varchar(100)", "Date": "varchar(100)", "msg": "text"}}
                self.__create_tables(text_table)

    def __create_tables(self, *models):
        for model in models:
            tb_name = list(model.keys())[0]
            table_sql = f"""CREATE TABLE {tb_name}(id INTEGER PRIMARY KEY AUTOINCREMENT """
            for field_name, field_type in model[tb_name].items():
                table_sql = table_sql + f", {field_name} {field_type}"
            try:
                self.__cursor.execute(table_sql + ")")
                self.__con.commit()
            except Error as err:
                raise err

    def save_key_into(self, tabla: str, person, llave):
        if tabla == 'Datos':
            #for key in dic.keys():
                #llave = str(dic.get(key))
            cmd = f"INSERT INTO {tabla}(Entidad,Kp) VALUES(?,?)"
            datos = (str(person), str(llave))
            self.__con.execute(cmd, datos)
            self.__con.commit()
        else:
            print('Error al elegir la tabla')

    def save_msg(self, tabla: str, entity: str, date: str, msg: str) -> bool:
        if tabla == 'Mensajes':
            cmd = "INSERT INTO Mensajes(Entidad,Date,msg) VALUES(?,?,?)"
            datos = (str(entity), str(date), str(msg))
            self.__cursor.execute(cmd, datos)
            self.__con.commit()
            return True

    def get_all(self, tabla: str):
        try:
            query = f"SELECT * FROM {tabla}"
            info = self.__run_query(query)
            for data in info:
                print(data)
        except error:
            print(f'Error al realizar la consulta de la base de datos {tabla}')
            print(f'Intentalo de nuevo')

    def __run_query(self, query: str, parameter=()):
        conn = sqlite3.connect(self.__name)
        try:
            cursor = conn.cursor()
            cursor.execute(query, parameter)
            result = None
            if parameter:
                conn.commit()
            else:
                result = cursor.fetchall()
            return result
        except Error as err:
            raise err
        finally:
            conn.close()

    def __delete_database(self, name):
        try:
            from os import remove
            if self.__name[-3:] == '.db':
                remove(name)
        except error:
            print(error)

    def end(self):
        self.__con.close()
        self.__delete_database(self.__name)

    def save_msg_2(self):
        while True:
            if self.datos:
                cmd = "INSERT INTO Mensajes(Entidad,Date,msg) VALUES(?,?,?)"
                datos = (str(self.datos[0]), str(time.strftime("%c")), str(self.datos[1]))
                con = sqlite3.connect(self.__name)
                con.execute(cmd, datos)
                con.commit()
                con.close()
                self.datos = None

    def __init_deamons(self):
        procesar = threading.Thread(target=self.save_msg_2)
        save = threading.Thread(target=self.save_key)
        procesar.daemon = True
        save.daemon = True
        procesar.start()
        save.start()

    def save_key(self):
        print('Intentando guardardar')
        while True:
            if self.info_key:
                cmd = f"INSERT INTO 'Datos'(Entidad,Kp) VALUES(?,?)"
                datos = (str(self.info_key[0]), str(self.info_key[1]))
                con = sqlite3.connect(self.__name)
                con.execute(cmd, datos)
                con.commit()
                con.close()
                print('Guardado con exito')
                self.info_key = None




if __name__ == "__main__":
    db = MyDatabaseController('database.db')

    keys = {'cliente': '0x19240', 'server': '0x1', 'juan': '0x12', 'juan': '0x12'}
    #db.save_key_into(tabla='Datos', dic=keys)
    db.save_key_into(tabla='Datos', person='pepe', llave='0x12')
    db.get_all(tabla='Datos')

    msf = f'Alguna vez te han roto el corazón, dime quien fue... NO fue nadie de ellos, porqie realmente no importa' \
          f'lo es? no lo spe... En realidad te extraño mucho como no tienes idea... realmente no lo sé'
    db.save_msg('Mensajes', "Juan", "10-10-20", msf)
    db.save_msg(tabla='Mensajes', entity='Cliente', date=time.strftime("%c"), msg='text')
    db.get_all(tabla='Mensajes')
