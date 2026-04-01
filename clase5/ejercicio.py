def pedrir_comida():
    comida =""
    while comida =="":
        comida=input("que queres")
    return comida

def obtenes_presio(comida):
    pedrir_comida()
    menu=["pizza"
          "hambuerguesa"
          "empanadas"]            
    return menu
pedrir_comida()
print(obtenes_presio())
    

