class Ninja:
    def __init__(self, nombre, apellido, mascotas, premio, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascotas = mascotas
        self.premio = premio
        self.comida_mascota = comida_mascota

    def alimentar_mascotas(self):
        for mascota in self.mascotas:
            print(f"{self.nombre} está alimentando a {mascota.nombre}.")
            mascota.comer()

    def pasear_mascotas(self):
        for mascota in self.mascotas:
            mascota.jugar()

    def bañar_mascotas(self):
        for mascota in self.mascotas:
            mascota.baño()


class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def jugar(self):
        print(f"{self.nombre} está jugando.")

    def baño(self):
        print(f"{self.nombre} está tomando un baño.")


mascota1 = Mascota("Rosi", "perro")
mascota2 = Mascota("Luna", "gato")

ninja1 = Ninja("Lorena", "Ferreira", [mascota1, mascota2], "galletas", "Croquetas")

ninja1.alimentar_mascotas()
