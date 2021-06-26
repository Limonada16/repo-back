class Product:
    precio = 0
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return self.nombre

    def __lt__(self, other):
        

    def __eq__(self, other):
        return self.precio == other.precio

class Cart:
    products = []
    
    def add_product(self,producto):
        self.products.append(producto)

    @property

    def total(self):
        total = 0
        for producto in self.products:
            total += producto.precio
        return total

iphone = Product(nombre="iPhone12", precio=6000)
macbook = Product(nombre="MacBook", precio=8000)

cart = Cart()
cart.add_product(iphone)
cart.add_product(macbook)
cart.add_product(iphone)

print(cart.total)