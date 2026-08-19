import json

producto={
    "nombre":"pepsi",
    "precio":950,
    "stok":9,
    "tamano":"chico"
}

with open("producto.json", "w") as archivo:
    json.dump(producto, archivo)

