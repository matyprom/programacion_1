archivo=input("pasame el archivo")
posicion=int(input("pasame la posicion de la palabra"))

try:
    with open(archivo, "r") as frases:
      lineas=frases.read()
      print(lineas[posicion])
except FileNotFoundError:
   print("no existe el archivo")

#hice cualquiera                                                                               