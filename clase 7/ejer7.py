numeros = [4, 9, 1, 9, 3]

def num_mayor(lista):
    mayor=[]
    contador=0
    for i in lista:
        if lista[i]>lista[i-1]:
            mayor=i

num_mayor(numeros)
print(num_mayor())
