#Pedir calificacion de 15 alumnos y sacar el promedio.
n1=0
n2=0
n3=0
while n1<15:
    n1+=1
    n2=float(input(f"ingresa la calificacion {n1} " "\n"))
    n3=n3+n2
print(f"El promedio es==> ", (n3/15))