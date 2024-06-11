try:
    nombre= input("ingresa un nombre")
    if len(nombre)>0:
        nombreusuario="el nombre del ususario del sistema es:"+ nombre
    print(nombreusuario)
except:
    print("es necesario ingresar un nombre de usuario")



# ejemplo 2
try:
    numero = int(input("ingresa un numero entero"))
    if numero>0:
        print("soy mayor que 0")
    else:
        print("soy u numero entero negativo")
except ValueError:
    print("no es posible convertir una letra a un numero verifica porfavor")

# ejemplo 3
try:
    numero1=int(input("ingresa un numero"))
    print("el cuadrado del nuemero es "+ str(numero*numero))
except ValueError:
    print("no coinciden los tipos")
else:
    print("todo se ejecuto sin errores")
finally: #finally simepre se ejcuta 
    print("ya termino")
