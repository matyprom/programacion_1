import sys
import os
# nombre_apellido= sys.argv[1]
# cantidad = int(sys.argv[2])

# for i in range(cantidad):
#     print(f"hola, {nombre_apellido}")

archivo=sys.argv[1]
if not os.path.exists(archivo):
    print ("no existe")

with open("archivo.txt", "r") as datos:
    contenido=datos.read()
print(contenido)
    


