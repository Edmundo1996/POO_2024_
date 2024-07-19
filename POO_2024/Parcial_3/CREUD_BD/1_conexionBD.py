import mysql.connector
try:
#Conectar con la BD en MySQL
    conexion=mysql.connector.connect(
        host='local',
        user='root',
        password='',
        database=''
    )
except Exception as e:
    print("ocurrio un error con el servidor")
    print(e)
    print(type(e))
    print(f"tipo de exepcion {type(e).__name__}")
    print("no es posible conectarse con el servidor en este momento intentalo mas tarde")
#Verificar si la conexion fue exitosa

if conexion.is_connected():
    print("La conexion con la BD  fue exitosa ")
else:
    print('No fue posible conectar a la BD ...VERIFIQUE...')
