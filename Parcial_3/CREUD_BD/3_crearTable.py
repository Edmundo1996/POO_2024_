from conexionBD import*

#Conectar con la BD en MySQL

try:
    cursor=conexion.cursor()
    sql="create table clientes(id int primary key auto_increment, nomvre varchar,(60),direccion varchar(120),tel varchar(10))"
    cursor.execute(sql)
except:
    print("ocurrio un probelma porfavor verifica")
else:
    print("se creo la tabla exitosamente")
#Verificar si la conexion fue exitosa
'''
if conexion.is_connected():
    print("La conexion con la BD  fue exitosa ")
else:
    print('No fue posible conectar a la BD ...VERIFIQUE...')
'''