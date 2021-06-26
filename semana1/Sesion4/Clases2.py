class Perro:
    nombre = "perro"

    def __init__ (self, nombre):
        self.nombre = nombre

    def cambiarNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def ladrar(self):
        print("woof")

Fido = Perro(nombre="Fido")
Firulais = Perro(nombre="Firulais")

print(Fido.nombre)
Fido.ladrar()
Firulais.ladrar()
Fido.cambiarNombre("Bobbie")
print(Fido.nombre)