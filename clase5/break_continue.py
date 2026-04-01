salir = True
i=0
while salir:
    print(f"estoy al principio de la interacion: {i}")
    i +=1
    if input("ir a la proxima interaccion? si/no") == "si":
        continue #si se cumple el if vuelve al inicio de whilw
    print(f"estoy al final de la interacion: {i-1}")
    if input("deseas salir ")=="si":
        break #si se cumple el if sale del while
    print(f"estoy al final de la interacion: {i-1}")
print("chau")