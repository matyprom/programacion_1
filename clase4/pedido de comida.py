opcion=""
total=0
comida=["pizza", "empanadas", "hamburguesas"]
print("seleccionar la comida")
while opcion!="terminar":
    opcion=input("escribi que queres wacho o ingesa terminar para finalizar pedido ").lower()
    if opcion=="pizza"or"empanadas"or"hamburguesas":
        if opcion=="pizza":
            total+=25
            print("perfecto tomamos tu pedido, el total es {total}")
        elif opcion=="empanadas":
            total+=40
            print("perfecto tomamos tu pedido, el total es {total}")
        elif opcion=="hamburguesas":
            total+=30
            print("perfecto tomamos tu pedido, el total es {total}")
    elif opcion=="terminar":
        print("cerrando pedido..")
    else:
        print(f"no tenemos {opcion}")
print("dale graciass, el total es {total}")