rango = list(range(1, 1000))

str_range = []

for i in rango:
    str_range.append(str(i))


output = open("texto.txt", "w")
output.writelines(rango)