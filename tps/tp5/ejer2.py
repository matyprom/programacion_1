numeros = (4, 7, 2, 9, 7)
print(numeros[0])
print(numeros[-1])
contador=0
for x in numeros:
    if x ==7:
        contador+=1
print("hay ",contador, " numeros 7")
print("el largo de la tupla es: ", len(numeros))

