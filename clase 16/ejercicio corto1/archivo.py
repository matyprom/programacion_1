import json

with open("ejercicio corto\\guardia_house.json", "r") as archivo:
    datos=json.load(archivo)

# for pacientes in (datos["pacientes"]):
#     print (pacientes)
print(datos["guardia"])