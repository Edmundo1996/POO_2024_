#Mostrar todos los numeros que ingrese el usario entre 2
n1=int(input("ingresa un numero entre el que quieres dividir==>" +"\n"))
n2=int(input("ingresa hasta que numero quieres hacer las diviciones==> "+"\n"))
i=0
while i<n2:
    i+=1
    print(f"la divicion del numero {n1} entre {i} ==> ", i/n1)