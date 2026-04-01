LA_LISTA = []
fin = False
usuario = " "
while usuario!="fin" and len(LA_LISTA)<5:
    usuario=(input("pasame algo para agregar a la lista/ escribi fin: "))
    if usuario != "fin":
        LA_LISTA.append(usuario)
    
print(LA_LISTA)
print("las lista tiene", len(LA_LISTA), "elementos")