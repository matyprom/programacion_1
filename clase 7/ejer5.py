def suma_pares(n):
    suma=0
    for i in n:
        if i%2==0:
            suma+=i 
    return suma
num=1
numeros=[]

usuario=int(input("pasame un numero"))
while num<=5:
    print(usuario)
    numeros.append(usuario)
    num+=1
    usuario=int(input("pasame otro numero"))

print(suma_pares(numeros))