from conexionBD import *
try:
    micursor=conexion.cursor()
    sql="select * from clientes"

    micursor.execute(sql)

    #Crear un objeto para enviar el resultado de la ejecucion de la linea execute
    #Para posteriormente mostrar con ciclo
    resultado=micursor.fetchall()
except:
    print("ha ocurrido un error porfavor verfique")
else:
    for x in resultado:
        print(x) 