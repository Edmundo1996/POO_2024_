# 2.- 
# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for

lista1=[]
n1=True
while n1==True:
    ingreso=int(input("ingresa un numero"))
    if ingreso<120:
        lista1.append(ingreso)
    else:
        n1=False
lista1.sort()
print(lista1)