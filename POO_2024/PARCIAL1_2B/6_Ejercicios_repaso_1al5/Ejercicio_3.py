#Escribir un programa que muestre los cuadrados de los primeros 60 numeros

n1=0
n2=0
print("ciclo while")
while n1<=60:
    n1+=1
    n2=n1*n1
    print(n2)
print("")
print("ciclo for\n")
for i in range (61):
    print(i*i)