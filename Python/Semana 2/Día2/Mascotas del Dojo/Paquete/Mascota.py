from Paquete.Ninja import Ninja

class Mascota(Ninja):
    def __init__(self,nombre, apellido, mascotas, premio, comida_mascota, name, tipo, golosinas, salud, energia, ruido):
        super().__init__(nombre, apellido, mascotas, premio, comida_mascota)
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia
        self.ruido = ruido 



    def dormir(self):
        self.energia += 25
        return self
    
    
    def comer(self):
        self.energia += 5
        self.salud += 10
        return self

    
    def jugar(self):
        self.salud += 5
        return self
    
    def emitir_sonido(self):
        print(self.sonido)


