import json

with open("datohorario.txt", "r") as datoshorario:
    datos = json.load(datoshorario)
    print(datos)
