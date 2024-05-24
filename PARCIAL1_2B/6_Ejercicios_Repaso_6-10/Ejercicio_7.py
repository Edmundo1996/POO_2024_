#Mostrar si el numero es par o impar
n1=int
while n1!=0:
    n1=int(input("ingresa un numero para saber si es impar y presiona 0 para salir"+ "\n"))
    if n1%2>0:
        print(f"El numero {n1} es impar")
    else:
        print(f"el numero {n1} es par")