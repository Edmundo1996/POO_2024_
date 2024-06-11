
# crear una lista
lista = (23,24)
print(lista)

#recorrer lista con ciclo for 
# el indice en una lista siempre empieza en 0

for i in lista:
    print(i)

# recorrer lista con ciclo while
i=0
while i<=  len(lista)-1:
    i+=1
    print(i)

# crear una lista de 4 palabras, solicitar una palabra y buscar la conicidencia en la lista e indicar si la encontro y en que pocicion
encontrado=True
palabras =("hola", "2024", "bye", "UTD")
palabra_buscar =input("ingresa la palabra a buscar")

for i in palabras:
    if palabra_buscar == i:
        print(f"encontre la palabra {palabra_buscar} esta en la pocicion: {palabras.index(i)}")
        encontrado=False
if encontrado==True:
    print("no la encontre")
i=0
while i <=len(palabras):
    if palabra_buscar == palabras[i]:
        print(f"encontre la palabra {palabra_buscar} esta en la pocicion: {palabras.index(i)}")
        encontrado=False
    i+=1
if encontrado==False:
    print("no la encontre")


# agregar y eliminar elemento
n1 = (23 , 24)
print(n1)
# agregar elemento
n1.append(100)
print(n1)


agenda =[
"Carlos", 6182177656,
"Leon", 6181573516,
"Karin",6187655479,
"Pedro",6184653515,
]

