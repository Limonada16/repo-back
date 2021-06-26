class Estudiante:

    def __init__(self, nombre):
        self.nombre = nombre
        self.__nota = []

    def set__notas(self, nombre, nota):
        if len(self.__nota > 3):
            print("Todas las notas han sido registradas")
        else:    
            self.__nota.append(nota)

    def promedio(self):
        sum = 0 
        cant = 0
        for n in self.__notas:
            sum += n
            cant += 1

        return sum / cant

estudiante1 = Estudiante("Jaimito")
estudiante1.set__notas(10)
estudiante1.set__notas(15)
estudiante1.set__notas(8)

print(estudiante1.promedio)


