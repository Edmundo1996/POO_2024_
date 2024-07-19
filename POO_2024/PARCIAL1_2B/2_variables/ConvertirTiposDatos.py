""" 
Cuando se imprime en pantalla una cadena de caracteres se trabaja por default con cadenas es decir python no puede concatenar
otra cosa que no sea un STR 
 """
texto = "soy una cadena de caracteres"
numero = 23

# concatenar STR con STR
print("soy una cadena " + texto)

# concatenar un STR con un entero 
numero_str = str(numero)
print("El numero es  "+ numero_str) #forma numero 1
print("el numero convertido en STR es " + str(numero)) #forma comprimida

n1= int("23")#convertir el STR a un entero para poder realizar operaciones
n2 = 33

print(type(n1))
suma = n1+n2
print(f"La suma es ==> {suma}")

#conectar int con float

n3 = 23
n4 = 24.5
suma2 = int(n3+n4) #siempre se redondea hacia abajo 

print(suma2)