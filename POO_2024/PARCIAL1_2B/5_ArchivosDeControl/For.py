# Este ciclo es un iterable y se ejecuta x veces dea cuerdo a los valores numericos enteros establecidos

# sintaxis
# for "variable" in "elementos iterableslista", rango , etc
    # se deja tabulacion o 4 espacios seguido de las instrucciones
for contador in range (1,5): #siempre se cuenta el 0 como valor 
    print("@")


suma=0
#primeer valor define el inicio segundo valor define el final tercer valor define la el numero de aumentos por salto
for numero in range(1,6):
     print(numero)
     suma += numero
print(suma)

#ejemplo 3 crear un programa que solicite un numero entero y a continuacion imprima la tabla d emultiplicar correspondiente

n1 =int(input("ingresa un numero de la tabla de multi´plicar"))
for i in range (0,11):
     print(f" {i} multiplicado x {n1} ==>", i*n1)