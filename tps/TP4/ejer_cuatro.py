def calcular_descuento (precio):
    if precio>1000:
        pfinal=(1000*90)/100
        return pfinal
    else:
        return precio
    
print(calcular_descuento(10000))
print(calcular_descuento(888))
