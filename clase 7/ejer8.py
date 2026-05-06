def numero(lista):
    menor=[]
    cont=0
    n_menor=lista[0]
    for i in lista:
        if i<n_menor:
            n_menor=i
    for i in lista:
        if i==n_menor:
            cont+=1
    menor.append(n_menor)
    menor.append(cont)
    return menor

numeros=[-4, -9, 1, -9, 3]

print (numero(numeros))