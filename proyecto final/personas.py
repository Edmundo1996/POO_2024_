from funcionesBD import Utilidades
import mysql.connector
from mysql.connector import Error

class Personas:
    def __init__(self, nombre, apellido, email, password, puesto=None):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.puesto = puesto

class Empleados(Personas):
    def __init__(self, nombre, apellido, email, password, puesto):
        super().__init__(nombre, apellido, email, password, puesto)

    def agregar_cliente(self, nombre, apellido, rfc, direccion, telefono, email, password):
        try:
            cursor, conexion = Utilidades.cursor()
            if cursor and conexion:
                contrasena_encriptada = Utilidades.encriptar(password)
                datos = (nombre, apellido, rfc, direccion, telefono, email, contrasena_encriptada, self.id_empleado)
                cursor.execute("""
                    INSERT INTO CLIENTES (nombre, apellido, rfc, direccion, telefono, email, password, id_empleado)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, datos)
                conexion.commit()
                
                id_cliente = cursor.lastrowid
                no_cuenta = Utilidades.generar_numero_cuenta()
                no_tarjeta = Utilidades.generar_numero_tarjeta()
                cursor.execute("""
                    INSERT INTO CUENTAS (numero_cuenta, numero_tarjeta, id_usuario)
                    VALUES (%s, %s, %s)
                """, (no_cuenta, no_tarjeta, id_cliente))
                conexion.commit()

                print(f"Cliente agregado correctamente con cuenta {no_cuenta} y tarjeta {no_tarjeta}.")
        except Error as e:
            print(f"Ocurrió un error al agregar el cliente: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    @staticmethod
    def consultar_clientes():
        try:
            cursor, conexion = Utilidades.cursor()
            if cursor and conexion:
                cursor.execute("SELECT * FROM CLIENTES")
                clientes = cursor.fetchall()
                for cliente in clientes:
                    print(cliente)
        except Error as e:
            print(f"Error al consultar los clientes: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    @staticmethod
    def consultar_movimientos(id_usuario):
        try:
            cursor, conexion = Utilidades.cursor()
            if cursor and conexion:
                cursor.execute("SELECT * FROM MOVIMIENTOS WHERE id_usuario_emisor = %s", (id_usuario,))
                movimientos_cliente = cursor.fetchall()
                if movimientos_cliente:
                    for movimiento in movimientos_cliente:
                        print(movimiento)
                else:
                    print("No se encontraron movimientos.")
        except Error as e:
            print(f"Error al consultar los movimientos: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

class Cliente(Personas):
    def __init__(self, nombre, apellido, email, password, rfc=None, telefono=None, id_cliente=None):
        super().__init__(nombre, apellido, email, password)
        self.rfc = rfc
        self.telefono = telefono
        self.id_cliente = id_cliente

    def retirar(self, cantidad):
        if cantidad <= 0:
            return "Cantidad no válida"
        try:
            cursor, conexion = Utilidades.cursor()
            if cursor and conexion:
                cursor.execute("SELECT saldo FROM CUENTAS WHERE id_usuario = %s", (self.id_cliente,))
                saldo = cursor.fetchone()
                
                if saldo is None:
                    return "No se encontró la cuenta"
                
                saldo_actual = saldo[0]
                if saldo_actual < cantidad:
                    return "No dispone de esa cantidad"
                
                cursor.execute("UPDATE CUENTAS SET saldo = saldo - %s WHERE id_usuario = %s", (cantidad, self.id_cliente))
                conexion.commit()
                
                if cursor.rowcount > 0:
                    cursor.execute("""
                        INSERT INTO MOVIMIENTOS (tipo_movimiento, monto, id_usuario_emisor)
                        VALUES (%s, %s, %s)
                    """, ("retiro", cantidad, self.id_cliente))
                    conexion.commit()
                    return "Retiro realizado y movimiento registrado con éxito"
                else:
                    return "No se pudo actualizar el saldo"
        except Error as e:
            return f"Error durante el retiro: {e}"
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def depositar(self, cantidad):
        if cantidad <= 0:
            return "Cantidad no válida"
        try:
            cursor, conexion = Utilidades.cursor()
            if cursor and conexion:
                cursor.execute("UPDATE CUENTAS SET saldo = saldo + %s WHERE id_usuario = %s", (cantidad, self.id_cliente))
                conexion.commit()
                
                if cursor.rowcount > 0:
                    cursor.execute("""
                        INSERT INTO MOVIMIENTOS (tipo_movimiento, monto, id_usuario_emisor)
                        VALUES (%s, %s, %s)
                    """, ("depósito", cantidad, self.id_cliente))
                    conexion.commit()
                    return "Depósito realizado y movimiento registrado con éxito"
                else:
                    return "Error al realizar el depósito"
        except Error as e:
            return f"Error: {e}"
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def transferir(self, no_tarjeta, cantidad, tipo="transferencia", motivo=None):
        if cantidad <= 0:
            return "Cantidad no válida"
        try:
            cursor, conexion = Utilidades.cursor()
            if cursor and conexion:
                cursor.execute("SELECT id_usuario FROM CUENTAS WHERE numero_tarjeta = %s", (no_tarjeta,))
                resultado = cursor.fetchone()
                
                if resultado:
                    id_cuenta_receptor = resultado[0]
                    
                    cursor.execute("""
                        INSERT INTO MOVIMIENTOS (tipo_movimiento, monto, id_usuario_emisor, id_usuario_receptor, motivo)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (tipo, cantidad, self.id_cliente, id_cuenta_receptor, motivo))
                    
                    cursor.execute("UPDATE CUENTAS SET saldo = saldo - %s WHERE id_usuario = %s", (cantidad, self.id_cliente))
                    cursor.execute("UPDATE CUENTAS SET saldo = saldo + %s WHERE id_usuario = %s", (cantidad, id_cuenta_receptor))
                    conexion.commit()
                    
                    return f"Transferencia exitosa de {cantidad} al número de tarjeta {no_tarjeta}."
                else:
                    return "El número de tarjeta proporcionado no existe."
        except Error as e:
            conexion.rollback()
            return f"Error en la transferencia: {e}"
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

class Gerente(Empleados):
    def __init__(self, nombre, apellido, email, password):
        super().__init__(nombre, apellido, email, password, puesto="gerente")
    
    @staticmethod
    def agregar_empleado(nombre, apellido, email, password, puesto):
        password = Utilidades.encriptar(password)

        try:
            cursor, conexion = Utilidades.cursor()
            if cursor and conexion:
                cursor.execute("""
                    INSERT INTO EMPLEADOS (nombre, apellido, email, password, puesto)
                    VALUES (%s, %s, %s, %s, %s)
                """, (nombre, apellido, email, password, puesto))
                
                conexion.commit()
                print(f"Empleado {puesto} agregado exitosamente.")
        except Error as e:
            conexion.rollback()
            print(f"Ocurrió un error al agregar el empleado: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
