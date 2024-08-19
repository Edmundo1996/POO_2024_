import mysql.connector
from mysql.connector import Error

class Banco:
    def __init__(self, name, host, user, password, database):
        self.name = name
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None

    def conectar_BD(self):
        try:
            self.conexion = mysql.connector.connect(
                user=self.user,
                host=self.host,
                password=self.password,
                database=self.database
            )
            if self.conexion.is_connected():
                print("Conectado a la base de datos")
                return self.conexion
        except Error as e:
            print(f"Error en la conexión a la base de datos: {e}")
            return None

    def crear_BD(self):
        try:
            conect = mysql.connector.connect(
                user="root",
                password="",
                host="localhost"
            )
            cursor = conect.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            print(f"Base de datos '{self.database}' creada o ya existe.")
            cursor.close()
            conect.close()
            self.conectar_BD()
            if self.conexion:
                self.create_tablas()
            else:
                print("No se pudo conectar a la base de datos después de crearla.")
        except mysql.connector.Error as e:
            print(f"HA OCURRIDO UN ERROR AL CREAR LA BASE DE DATOS: {e}")

    def create_tablas(self):
        try:
            if self.conexion: 
                cursor = self.conexion.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS EMPLEADOS (
                        id_empleado INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(50) NOT NULL,
                        apellido VARCHAR(50) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL,
                        puesto ENUM('gerente', 'empleado') NOT NULL
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS CLIENTES (
                        id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(100) NOT NULL,
                        apellido VARCHAR(100) NOT NULL,
                        rfc VARCHAR(13) NOT NULL UNIQUE,
                        direccion VARCHAR(255) NOT NULL,
                        telefono VARCHAR(20),
                        email VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL,
                        id_empleado INT,
                        FOREIGN KEY (id_empleado) REFERENCES EMPLEADOS(id_empleado)
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS CUENTAS (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        numero_cuenta VARCHAR(16) UNIQUE NOT NULL,
                        numero_tarjeta VARCHAR(20) NOT NULL,
                        saldo DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
                        id_usuario INT,
                        FOREIGN KEY (id_usuario) REFERENCES CLIENTES(id_usuario)
                    )
                """)


                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS MOVIMIENTOS (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        tipo_movimiento ENUM('depósito', 'retiro', 'transferencia') NOT NULL,
                        monto DECIMAL(15, 2) NOT NULL,
                        id_usuario_emisor INT,
                        id_usuario_receptor INT,
                        motivo TEXT,
                        FOREIGN KEY (id_usuario_emisor) REFERENCES CLIENTES(id_usuario),
                        FOREIGN KEY (id_usuario_receptor) REFERENCES CLIENTES(id_usuario)
                    )
                """)

                print("Tablas EMPLEADOS, CLIENTES, CUENTAS y MOVIMIENTOS creadas o ya existen.")
                cursor.close()
            else:
                print("No se pudo establecer conexión para crear las tablas.")
        except mysql.connector.Error as e:
            print(f"HA OCURRIDO UN ERROR AL CREAR LAS TABLAS: {e}")
        finally:
            if self.conexion.is_connected():
                self.conexion.close()
                print("Conexión cerrada.")

# banco = Banco("bancoppel", "localhost", "root", "", "bancoppel")
# banco.crear_BD()
