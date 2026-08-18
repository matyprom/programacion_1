mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]

ubicacion={}
conjunto=set()
for tipo, valor, ubi in mediciones:
        if ubi not in ubicacion:
            ubicacion[ubi]=[]
        ubicacion[ubi].append((tipo, valor))
        conjunto.add(tipo)
print(ubicacion)
print(conjunto)

