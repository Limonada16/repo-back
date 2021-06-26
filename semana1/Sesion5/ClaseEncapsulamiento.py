class Empleado:
    __salario = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario

    def calcular_salario(self):
        return self.__salario

    def pagar(self):
        monto = calcular_salario()
        print(f"{monto}pagado" )


jhon = Empleado(salario=3000, nombre="Jhon Rambo")

print(jhon.nombre)
print(jhon.calcular_salario())
print(jhon._Empleado__salario)