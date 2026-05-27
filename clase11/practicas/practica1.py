lineas=[
    " AnA ;8;7;9",
    " JuAn ;3;5;4",
    " LucIA ;10;9;10"
]
datos_limpios=[]
for linea in lineas:
    datos=linea.split(";")
    print(datos)
    nombre = datos[0]
    nombres_lindos=nombre.strip().capitalize()
    print(nombres_lindos)


# tlineas="".join(lineas).strip(" ").split(" ")
# print(tlineas)