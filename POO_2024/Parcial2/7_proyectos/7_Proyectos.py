<<<<<<< HEAD
class Figuras:
    def calcular_area(self):
        pass

class Rectangulo(Figuras):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def get_largo(self):
        return self.largo
    
    def set_largo(self, valor):
        self.largo = valor
    
    def get_ancho(self):
        return self.ancho
    
    def set_ancho(self, valor):
        self.ancho = valor

    def calcular_area(self):
        return self.largo * self.ancho

class Triangulo(Figuras):
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    
    def get_altura(self):
        return self.altura
    
    def set_altura(self, valor):
        self.altura = valor
    
    def get_base(self):
        return self.base
    
    def set_base(self, valor):
        self.base = valor

    def calcular_area(self):
        return (self.altura * self.base) / 2

class Circulo(Figuras):
    def __init__(self, radio):
        self.radio = radio
    
    def get_radio(self):
        return self.radio
    
    def set_radio(self, valor):
        self.radio = valor

    def calcular_area(self):
        import math
        return math.pi * (self.radio ** 2)
=======
class Figuras:
    def calcular_area(self):
        pass

class Rectangulo(Figuras):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def get_largo(self):
        return self.largo
    
    def set_largo(self, valor):
        self.largo = valor
    
    def get_ancho(self):
        return self.ancho
    
    def set_ancho(self, valor):
        self.ancho = valor

    def calcular_area(self):
        return self.largo * self.ancho

class Triangulo(Figuras):
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    
    def get_altura(self):
        return self.altura
    
    def set_altura(self, valor):
        self.altura = valor
    
    def get_base(self):
        return self.base
    
    def set_base(self, valor):
        self.base = valor

    def calcular_area(self):
        return (self.altura * self.base) / 2

class Circulo(Figuras):
    def __init__(self, radio):
        self.radio = radio
    
    def get_radio(self):
        return self.radio
    
    def set_radio(self, valor):
        self.radio = valor

    def calcular_area(self):
        import math
        return math.pi * (self.radio ** 2)
>>>>>>> 9d31cefd29013294c0a24990ad8ed6fb1841eb20
