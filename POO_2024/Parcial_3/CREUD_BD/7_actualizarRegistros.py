from conexionBD import *
try:

    micursor=conexion.cursor()
    sql="update clientes set direccion=('Col vizcaya' where id=1)"

    micursor.execute(sql)
    conexion.commit()
except:
    print("ha ocurrido un error")
else:
    print("Registro(s) Eliminado(s) exitosamente!!")