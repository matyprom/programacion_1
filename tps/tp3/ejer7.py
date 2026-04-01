opcion=""
total=0
comida=["pizza", "empanadas", "hamburguesas"]
pedido=[]
pizza=0
hamburguesa=0
empanadas=0
print("seleccionar la comida")
while opcion!="terminar":
    opcion=input("escribi que queres wacho o ingesa terminar para finalizar pedido ").lower()
    # if opcion=="pizza"or"empanadas"or"hamburguesa":
    if opcion=="pizza":
        total+=25
        pedido.append(opcion)
        pizza+=1
        print("perfecto tomamos tu pedido")
    elif opcion=="empanadas":
        total+=40
        pedido.append(opcion)
        empanadas+=1
        print("perfecto tomamos tu pedido")
    elif opcion=="hamburguesa":
        total+=30
        pedido.append(opcion)
        hamburguesa+=1
        print("perfecto tomamos tu pedido")
    elif opcion=="terminar":
        print("cerrando pedido..")
    else:
        print("ERROR..")
print("tu pedido fue ", pedido)
print(pizza, " - pizzas")
print(hamburguesa, " - hamburguesas")
print(empanadas, " - empanadas")
print("dale graciass, el total es", total)