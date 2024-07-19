import mysql.connector
try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
    )

except:
    print("a ocurrido un error porfavor verifique")
else:
     #Crear un objeto de tipo cursor que permita ejecutar instrucciones SQL
    micursor=conexion.cursor()
    sql="CREATE DATABASE nueva_Base"

    #Ejecutar la consulta
    micursor.execute(sql)
    if micursor:
        print('Se creo la BD Exitosamente!!')



    #Mostrar las bases de datos que existen en el SGBD MySQL
    micursor.execute("SHOW DATABASES")

    for x in micursor:
        print(x)