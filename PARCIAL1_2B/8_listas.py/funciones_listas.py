paises=[
    "mexico",
    "brazil",
    "japon"
]
numeros =[
    23,
    24,
    34,
    12,
    56,
    0.100
]
texto=[
    "hola",
    True,
    23,
    3.141516
]
# ORDENAR UNA LISTA SE UTILIZA .SORT()
print(paises)
paises.sort()
print(paises)
numeros.sort()
print(numeros) 

# AÑADIR ELEMENTOS 

paises.insert(len(texto),"True") #INSERT REQUIERE 2 ARGUMENTOS LA POCICION Y LO QUE SE DESEA AGREGAR 
print(paises)

texto.append(True) #AGREGA UN ELEMENTO AL FINAL DE LA LISTA
print(texto)

# ELIMINAR ELEMENTOS
numeros.remove(23) #REMOVE ACEPTA UN ARGUMENTO QUE ES EL ELEMNTO A ELIMINAR SI NO SE ENCUENTRA MARCARA EXEPTION
print(numeros)
numeros.pop(0)
numeros.reverse()
print(numeros)


# buscar un dato dentro de una lista

respuesta="brazil" in paises
print(respuesta)

# cuantas veces aparece un valor dentro de una lista

print(numeros)
numeros.append(24)
contador=numeros.count(24)
print(f"el numero 23 se contro {contador}")



# unir listas
print(paises)
paises.extend(numeros)
print(paises)
