from Paquete.Ninja import Ninja
from Paquete.Mascota import Mascota

class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def jugar(self):
        print(f"{self.nombre} está jugando.")

    def baño(self):
        print(f"{self.nombre} está tomando un baño.")


class Perro(Mascota):
    def __init__(self, nombre):
        super().__init__(nombre)

    def ladrar(self):
        print("¡Guau! ¡Guau!")


class Gato(Mascota):
    def __init__(self, nombre):
        super().__init__(nombre)

    def maullar(self):
        print("¡Miau! ¡Miau!")



perro1 = Perro("Rex")
gato1 = Gato("Luna")


perro1.comer()
perro1.jugar()
perro1.ladrar()

gato1.comer()
gato1.jugar()
gato1.maullar()