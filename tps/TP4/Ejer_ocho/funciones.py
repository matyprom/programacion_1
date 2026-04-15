def pedido():
    usuario=input("que queres[pizza-hamburguesa-milanesa]")
    return usuario

def precio(comida):
    if comida=="pizza":
        return 25
    elif comida=="hamburguesa":
        return 15
    elif comida=="milanesa":
        return 20
    else:
        return 0
    
def salir():
    print("ya entre")
    salida = input("joya, para salir escribe [listo]")
    return salida=="listo"

def comida(comida):
    if comida=="pizza":
        return "pizza"
    elif comida=="hamburguesa":
        return "hamburguesa"
    elif comida=="milanesa":
        return "milanesa"
    
    
