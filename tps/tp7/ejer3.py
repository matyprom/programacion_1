nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombres_normalizados=[]
cont=0
for i in nombres:
    nombre_bien=nombres[cont].strip().capitalize()
    nombres_normalizados.append(nombre_bien)
    cont+=1

print(nombres_normalizados)