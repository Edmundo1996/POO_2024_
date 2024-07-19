# crear una lista de 4 palabras, solicitar una palabra y buscar la conicidencia en la lista e indicar si la encontro y en que pocicion
encontrado=True
palabras = ("hola", "2024", "bye", "UTD")
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