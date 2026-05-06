def precio(producto):
    if producto=="martillo":
        return 3000
    elif producto=="clavos":
        return 500
    elif producto=="destor":
        return 500
    else:
        return 0
    
suma=0
productos=input("pasame un producto").lower()
while productos!="fin":
    suma+=precio(productos)
    productos=input("pasame un producto o fin").lower()

print(suma)