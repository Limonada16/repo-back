#ABRIR Y LEER ARCHIVO POR LINEA
f = open("texto.txt")
print(f.readline())

#CONVERTIR ARHIVO A STRING
with archivo as reader: 
    for line in reader:
        print (line)