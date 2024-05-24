promedio = 0
n2 = 0
n1 = "yes"

while n1 == "yes":
    n2 += 1
    nombre = input("Ingresa el nombre del alumno ==> : ")
    carrera = input("Ingresa la carrera: ")
    print("Ingresa las calificaciones de tus 3 parciales ==> : ")
    for i in range(1, 4):
        calificacion = float(input(f"Ingrese la calificación {i}: "))
        promedio += calificacion
        promediofin = float(input("Ingresa la calificación de tu proyecto final: "))
    promedio1 = promedio / 3
    total = (promedio + promediofin) / 2
    print(f"El alumno {nombre} de la carrera de {carrera} tiene un promedio de {total}")
    if total < 80:
        print(f"El alumno {nombre} sacó un promedio de {total} y presentara examen extraordinario")
    else:
        print(f"felicidades paso conn una calificacion de {total}")
    n1 = input("¿Quieres agregar otro alumno? (yes/no): ")
print(f"Total de alumnos ingresados: {n2}")
      