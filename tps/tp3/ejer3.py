LA_LISTA = []
fin = False
usuario = " "
while fin == False:
    usuario=(input("pasame algo para agregar a la lista/ escribi fin: "))
    if usuario != "fin":
        LA_LISTA.append(usuario)
        
    else:
        fin=True  
print(LA_LISTA)
print("las lista tiene", len(LA_LISTA), "elementos")