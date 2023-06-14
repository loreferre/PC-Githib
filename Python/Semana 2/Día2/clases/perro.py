from clases.animal import Animal

class Perro(Animal):
    def __init__ (self, nombre, dueño, raza, color):
        super().__init__(nombre, dueño)
        self.raza = raza
        self.color = color
    
    def imprime_info_perro(self):
        super().imprime_info()
        print(f"Raza {self.raza}")
        print(f"Color: {self.color}")