suma=0
numeros_negativos=0
numeros_positivos=0
num=[]

us=int(input("pasame un numero"))
while us!=0:
    num.append(us)
    us=int(input("pasame un numero"))

for i in num:
    if i>0:
        numeros_positivos+=1
    if i<0:
        numeros_negativos+=1
    suma+=i
print(suma, numeros_negativos, numeros_positivos)