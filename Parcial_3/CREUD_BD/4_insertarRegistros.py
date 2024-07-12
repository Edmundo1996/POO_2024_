from conexionBD import *
try:
    micursor=conexion.cursor()
    nombre=input("cual es el nombre")
    direccion=input("¿cual es la direccion?")
    tel=input("¿cual es el numero de telefono?")

    sql="INSERT INTO `clientes` (`id`, `nombre`, `direccion`, `tel`) VALUES (NULL, '%s', '%s', '%s');"
    valores=(nombre,direccion,tel)
    micursor.execute(sql,valores)

    #El 'comit' sirve para finalizar la conexion de sql cuando se intenta hacer un insert, un update y un delete en una tabla
    conexion.commit()
except:
    print("ha ocurrido un error porfavor verifique")
else:
    print(f"Registro(s) insertado(s) exitosamente!!! ")