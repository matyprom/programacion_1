x=[10, -1, 2, 3, 5, 7, 6, -7, 8, -10]
maximo=0
minimo=0
for i in x:
    if maximo<i:
        maximo=i
    if minimo>i:
        minimo=i
print (maximo, minimo)