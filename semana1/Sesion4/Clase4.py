class Seat: 
    color = "negro"

class Car:
    asientos = [Seat(), Seat()]

ferrari = Car()
ferrari.asientos[0].color = "rojo"

print(ferrari.asientos[0].color)
print(ferrari.asientos[1].color)
