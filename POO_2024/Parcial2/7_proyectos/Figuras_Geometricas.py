<<<<<<< HEAD
class Figuras:
    def __init__(self):
        self.x = 0  
        self.y = 0  
        self.visible = True 

    def esta_visible(self):
      print(self.visible)

    def mostrar(self):
      print(f"valor x de la figura igual: {self.x} y valor y de la figura igual: {self.y}")

    def ocultar(self):
       self.visible=False

    def movement(self, x1, y1):
       self.x=x1
       self.y=y1
       print(f"la figura se encuentra en el valor{self.x} en en su valor de x y en {self.y} en su valor de y")
    def calcular_area(self):
       return(0.0)
    
class Rectangulo(Figuras):
    def __init__(self, alto, ancho): 
        self.alto = alto
        self.ancho = ancho
    
    def calcular_area(self):
        return self.alto * self.ancho
    
class Circulo(Figuras):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return 3.14159 * self.radio ** 2
    
    rectagulo1=Rectangulo(Figuras)
    
=======
class Figuras:
    def __init__(self):
        self.x = 0  
        self.y = 0  
        self.visible = True 

    def esta_visible(self):
      print(self.visible)

    def mostrar(self):
      print(f"valor x de la figura igual: {self.x} y valor y de la figura igual: {self.y}")

    def ocultar(self):
       self.visible=False

    def movement(self, x1, y1):
       self.x=x1
       self.y=y1
       print(f"la figura se encuentra en el valor{self.x} en en su valor de x y en {self.y} en su valor de y")
    def calcular_area(self):
       return(0.0)
    
class Rectangulo(Figuras):
    def __init__(self, alto, ancho): 
        self.alto = alto
        self.ancho = ancho
    
    def calcular_area(self):
        return self.alto * self.ancho
    
class Circulo(Figuras):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return 3.14159 * self.radio ** 2
    
    rectagulo1=Rectangulo(Figuras)
    
>>>>>>> 9d31cefd29013294c0a24990ad8ed6fb1841eb20
