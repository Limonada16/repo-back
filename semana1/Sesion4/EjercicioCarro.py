class Vehiculo:
    def __init__ (self, puertas, llantas, todoterreno):
        self.puertas = puertas
        self.llantas = llantas
        self.todoterreno = todoterreno
    
class Auto(Vehiculo):
    pass
class Camioneta(Vehiculo):
    pass
class Moto(Vehiculo):
    pass

Toyota = Auto(2,4,False)
Hyundai = Camioneta(4,4,False)
Kawasaki = Moto(0,4,True)
