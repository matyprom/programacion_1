archivo=open("temperaturas.txt", "r")
temp={}
archivo_bien=[]
for lineas in archivo:
    partes = lineas.strip().split(";")
    archivo_bien.append(partes)
    ciudades=partes[0]
    temperaturas=partes[1]
    if ciudades not in temp:
        temp[ciudades]=[]
    temp[ciudades].append(temperaturas)
print(archivo_bien)
print(temp)
archivo.close()
