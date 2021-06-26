class Spy:
    nombre = "unknown"
    def __set__(self, obj, val):
        print("Estan actualizando nombre a" + val)
        self.nombre = val

espia = Spy()
espia.nombre = "James Bond"
