numeros = [-1, 1, -2, -3, 7, 10]
numero_negativos=0
numero_positivos=0
suma=0
for i in numeros:
    if i>0:
        numero_positivos+=1
    else:
        numero_negativos+=1
    suma+=i
print("suma total: ", suma)
print("numero negativos: ", numero_negativos)
print("numeros positivos", numero_positivos)