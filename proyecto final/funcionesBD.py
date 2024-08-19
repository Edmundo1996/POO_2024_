import mysql.connector
import os
import bcrypt
import random
from mysql.connector import errors

class Utilidades:

    @staticmethod
    def conectar():
        try:
            con = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='bancoppel'
            )
            return con
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return None
            
    @staticmethod
    def borrarscreen():
        os.system('cls')
        
    @staticmethod
    def encriptar(password):
        sal = bcrypt.gensalt()
        encrypass = bcrypt.hashpw(password.encode('utf-8'), sal)
        return encrypass
    
    @staticmethod
    def cursor():
        conexion = Utilidades.conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            return cursor, conexion
        else:
            return None, None

    @staticmethod
    def generar_numero_tarjeta():
        numero_tarjeta = ''.join([str(random.randint(0, 9)) for _ in range(16)])
        return numero_tarjeta

    @staticmethod
    def generar_numero_cuenta():
        numero_cuenta = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        return numero_cuenta