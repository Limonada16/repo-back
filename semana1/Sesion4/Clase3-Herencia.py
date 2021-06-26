class Animal:

    nombre = "animal"

    def __init__ (self, nombre):
        self.nombre = nombre

    def dormir(self):
        print("ZZZ")

class Dog(Animal): 

    def ladrar(self):
        print("Woof")

class Cat(Animal):

    def maullar(self):
        print("Miau")

fido = Dog(nombre="Fido")
print(fido.nombre)
fido.ladrar()
fido.dormir()

pelusa = Cat("Pelusa")
print(pelusa.nombre)
pelusa.maullar()
pelusa.dormir()