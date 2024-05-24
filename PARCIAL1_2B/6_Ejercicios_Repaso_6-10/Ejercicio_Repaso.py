#Crear un programa que clacule y obtenga el total a pagar por un producto determinado. 
#Se debera de solicitar el nombre o descrpcion del producto, codigo del producto cantidad del producto precio unitario del producto,
#el total a pagar incluye el iva y el descuento 
#si se compran de 1-5 productos =10% off
#6-10 15% ff
#>1020%

producto=str(input("ingresa el nombre o descrupcion del prodcuto"))
cantidad=int(input("-ingresa la cantidad del producto"))
precio=float(input("ingresa el precio del producto"))
total=float;
total=(cantidad*precio)*1.16
if cantidad<=5:
    total=(total*.90)
elif cantidad<=10:
    total=(total*.85)
elif cantidad>10:
    total=(total*.80)
print(f"El precio total por {cantidad} del producto{producto} con descuentos e iva aplicados es==> {total}")