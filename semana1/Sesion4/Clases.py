#CREACIÓN DE LA CLASE
class Empleado:
    numero_ventas = 0

    #INICIALIZADOR DE LA CLASE
    def __init__ (self, nombre, apellido, salario, dni):
        self.nombre =  nombre
        self.apellido = apellido
        self.salario = salario
        self.dni = dni
    #METODO VENDER
    def vender(self):
        self.numero_ventas += 1
        print ("Hice una venta")
    #METODO REPORTAR
    def reportar(self):
        print(f"vendí: {self.numero_ventas}")
#INSTANCIAR UN OBJETO CON SUS
juan = Empleado("Alonso", "Conde", 2000, "71791966") 
jhon = Empleado("Jhon", "Gutierrez", 3000, "71791967") 

#LLAMAR A LOS METODOS DEL OBJETO CREADO
print(juan.salario)
juan.vender()
juan.reportar()
jhon.reportar()