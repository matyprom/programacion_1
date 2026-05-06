def suma_pares(lista):
    numeros_pares=0
    for i in lista:
        if i%2==0:
            numeros_pares+=i
    return numeros_pares
numeros=[2,4,5,7,9]
print(suma_pares(numeros))