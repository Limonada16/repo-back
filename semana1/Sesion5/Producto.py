class Product:
    def __init__(self, costo):
        self.__costo = costo
        self.__precio * 1.57

    def precio_final(self, descuento):
        return self.__precio * (1-descuento)

play5 = Product(3000)
print(play5.precio_final)