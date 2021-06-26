
class Pet:
    def __init__(self,nombre):
        self.nombre = nombre
    def alimentar(self):
        print("alimentación generica")

class Dog(Pet):
    def alimentar(self):
       print("Dar croquetas")

class Cat(Pet):
    def alimentar(self):
        print("Dar enlatado")

class Turtle(Pet):
    pass

mascotas = [
    Dog(nombre="Fido"),
    Cat(nombre="Pelusa"),
    Turtle(nombre="Veloz")
    ]
for mascota in mascotas:
    mascota.alimentar()