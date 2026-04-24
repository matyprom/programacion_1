numeros = [-1, 1, -2, -3, 7, 10]
numero_negativos=[]
numero_positivos=[]
suma=0
for i in numeros:
    if i>0:
        numero_positivos.append(i)
    else:
        numero_negativos.append(i)
    suma+=i
print("suma total: ", suma)
print("numero negativos: ", numero_negativos)
print("numeros positivos", numero_positivos)