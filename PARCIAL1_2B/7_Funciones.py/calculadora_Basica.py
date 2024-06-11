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
    return(result)

print("seleccione una opcion segun desea PRESIONANDO EL NUMERO O ESCRIBIENDO LA OPERACION A REALIZAR \n SUMA '1' o 'SUMA' \n RESTA '2' o 'RESTA'\n MULTIPLICACION '3' o MULTIPLICACION\n divicion '4' o 'DIVISION' \n 5 PARA SALIR ")

opcion =True
while opcion:
    opc=input("ingresa la opcion segun la operacion")
    if opc=="5":
        opcion=False
        print("adios")
    else:
        sol_Datos()
        operaciones(n1,n2,opc)
        resultado=operaciones(n1,n2,opc)
        print(resultado)