class Mamals:
    def swim(self):
        print("Swimming as a mamal...")


class Fish:
    def swim(self):
        print("Swimming")


class Dolphin(Fish, Mamals): 
    pass

class Monkey(Mamals):
    pass

print(Dolphin.__mro__)

# chita = Monkey()
# flipper = Dolphin()

# chita.swim()
# flipper.swim()
