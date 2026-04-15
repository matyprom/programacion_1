import funciones as fun
pedido_final=[]
preciofinal=0

while True:
    pedido = fun.pedido()
    preciofinal = preciofinal + fun.precio(pedido)
    print(preciofinal)
    pedido_final.append(fun.comida(pedido))
    print("antes de entrar")
    salir=fun.salir()
    if salir==True:
        break
print("el total a pagar es: ", preciofinal)
print("su pedido final es: ", pedido_final)