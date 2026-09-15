producto_y_precio = input("psame el producto y el precio separado por un ; :")
try:
    datos=producto_y_precio.split(";")
except ValueError:
    print("producto y precio inavalido")
    exit(2)
try:
    precio=float(datos[1])
    
except IndexError:
    print("se ingreso un numero invalido")
    exit(1)

producto=datos[0]
print(f"{producto} cuesta ${precio}")