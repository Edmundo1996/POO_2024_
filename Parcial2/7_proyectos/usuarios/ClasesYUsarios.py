class Usuarios:
    def __init__(self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel

    def info_usuario(self):
        print(f"Nombre: {self.nombre}\nDirección: {self.direccion}\nTeléfono: {self.tel}")


class Cliente(Usuarios):
    def __init__(self, nombre, direccion, tel, numero_de_cliente):
        super().__init__(nombre, direccion, tel)
        self.numero_de_cliente = numero_de_cliente

    def info_usuario(self):
        super().info_usuario()
        print(f"Número de cliente: {self.numero_de_cliente}")


class Empleado:
    def __init__(self, salario, num_empleado, tipo):
        self.salario = salario
        self.num_empleado = num_empleado
        self.tipo = tipo
    def info_usuario(self):
        super().Empleados()
        print(f"Número: {self.num_empleado}")
        
cliente1 = Cliente("Ana Torres Guzman", "Col centro 1500 nte", 6182177656, 1234)
cliente1.info_usuario()

Emplead1=Empleado("Daniel Fuentes Loera",1200.90,123,"A")