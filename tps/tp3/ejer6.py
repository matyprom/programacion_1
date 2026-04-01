lista=["futbol", "basquet", "tenis", "boxeo"]
posicion=0
usuario=input("decime un deporte: ")
while posicion < len(lista):
    if usuario == lista[posicion]:
       print("ese esta") 
       print("esta en la posicion", len(lista[posicion]))
    posicion+=1
    # print (posicion)




# while usuario in lista:     
#     print("Esta")
#     print(len(lista[posicion]))
#     usuario=input("decime un deporte: ")
# print("No esta")
