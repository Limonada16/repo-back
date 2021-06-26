lista = [1,3,4,19,21,11]

def half(x):
    return x/2

isadult = lambda x: x>18

mapa = map(half, lista)



print(list(mapa))
print(list(filter(lambda x: x>18, lista)))
