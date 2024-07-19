# 3.- 

# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas

lista=[]
n1=len(lista)
n2=True
while n2==True:
    agregar=input("ingresa algo lo que sea")
    lista.append(agregar)
    print("quieres agregar otro archivo presiona 1 para 'si' \n 2 para 'no'")
    n3=int(input())
    if n3!=1:
        n2=False
for i in lista:
    print(i.upper())