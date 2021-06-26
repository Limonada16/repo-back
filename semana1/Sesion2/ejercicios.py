#CADENA PALINDROMA
def palindromo (texto):
    if texto == texto[::-1]:
        print ("Palindromo")
    else:
        print ("No es")

# CAMBIAR CODIGO ADN
def contra (texto):
    cadeNew = ""
    codigo = {"T" : "A", "A" : "T", "C": "G", "G" : "C" }
    for le in texto :
        cadeNew += codigo[f'{le}']
    return cadeNew

print(contra("TACG"))
# print (palindromo("abba"))