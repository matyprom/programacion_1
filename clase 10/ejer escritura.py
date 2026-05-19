
nombres=input("pasame un nombre")

archivo=open("archivo nobres", "w")
for n in range(5) :
    archivo.write(nombres + "\n")
    nombres=input("pasame un nombre")
archivo.close()


# lista_nombres=[]
# archivo=open("archivo nobres", "w")
# for n in range(5):




# archivo.write("\n".join(lista_nombres))
# archivo.close()