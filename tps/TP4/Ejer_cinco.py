def obtener_estado (nota):
    if nota>=8:
        return "promociona"
    elif nota<8 and nota>=6:
        return "aprueba"
    elif nota < 6:
        return "desaprueba"
    
print(obtener_estado(9))
print(obtener_estado(7))
print(obtener_estado(3))