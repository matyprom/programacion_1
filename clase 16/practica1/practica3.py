import json

with open("producto.json", "r") as archivo:
    datos=json.load(archivo)

datos["nombre"] = "pepsi"

archivo=open("nuevo_producto.json", "w")
json.dump(datos, archivo)
archivo.close()