producto = {"nombre": "Mouse", "precio": 12500, "stock": 6}

for clave in producto:
    print(clave)

for valor in producto.values():
    print(valor)

for clave, valor in producto.items():
    print(clave, valor)