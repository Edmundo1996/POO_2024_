def sol_Datos():
    global n1,n2,opc
    print("Saludos Esta es una calculadora basica ingresa 2 numeros a contunuacion ......\n")
    n1=float(input("ingrese el priemr numero porfavor  \n"))
    n2 = float(input("ingrese el segundo numero porfarvor \n"))
    

def operaciones (num1,num2,opc):
    if opc=="1":
        suma=num1+num2
        result=suma
    elif opc=="2":
        resta=num1-num2
        result=resta
    elif opc=="3":
        multi=num1*num2
        result=multi
    elif opc=="4":
        divi=num1/num2
        result=divi
    elif opc=="5":
        potencia=num1 ** num2
        result=potencia
    elif opc=="6":       
        result=num1**.5
    return(result)


   
print("""seleccione una opcion segun desea PRESIONANDO EL NUMERO O ESCRIBIENDO LA OPERACION A REALIZAR 
SUMA '1' o 'SUMA' 
RESTA '2' o 'RESTA'
MULTIPLICACION '3' o MULTIPLICACION
divicion '4' o 'DIVISION' 
5 elevar a la potencia
sacar raiz presione 6
salir presione 7""")

opcion =True
while opcion:
    opc=input("ingresa la opcion segun la operacion")
    if opc=="7":
        opcion=False
        print("adios")
    elif opc=="6":
        n1=float(input("ingrese el numero a sacar la raiz"))
        resultado=operaciones(n1,0,opc)
        print(resultado)

    else:
        sol_Datos()
        operaciones(n1,n2,opc)
        resultado=operaciones(n1,n2,opc)
        print(resultado)
        #.