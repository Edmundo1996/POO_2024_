print("calculadora de IMC ingrese sus datos a continuacion ")
n2=0
n1=1
while n1==1:
    n2+=1
    peso=float(input("ingresa tu peso en kg ==>  "))
    estatura=float(input("ingresa tu estatura en metros==>  "))
    IMC=(peso/(estatura*estatura))
    if IMC>30.0:
        print("obesidad")
    elif IMC>25.0 and IMC<29.9:
        print("peso superior al normal")
    elif IMC>18.5 and IMC<24.9:
        print("normal")
    else:
        print("peso inferior al normal")
    print("si quiere agregar otros datos presione 1")
print(f"has registrado {n2} usarios")
#.