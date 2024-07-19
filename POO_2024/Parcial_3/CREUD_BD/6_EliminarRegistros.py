from conexionBD import *
try:

    micursor=conexion.cursor()
    sql="delete from clientes WHERE id=3"

    micursor.execute(sql)
    conexion.commit()
except:
    print("ha ocurrido un error")
else:
    print("Registro(s) Eliminado(s) exitosamente!!")