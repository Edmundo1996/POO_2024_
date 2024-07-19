#Mostrar todas las tablas de multiplicar con su titulo 
i=0
n1=0
while i<11:
    print(f"tabla de multiplicar del {i}")
    for n1 in range(10):
        print(f"{n1} x {i} =", i*n1)
        n1+=1
    i+=1