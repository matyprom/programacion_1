def sumar(a,b):
    return a+b

def calcular_costo_envio(peso_gramo):
    if peso_gramo <= 0:
        raise ValueError("el peso debe ser mayor a 0")
    if peso_gramo <= 1000:
        return 2500
    if peso_gramo<=5000:
        return 4500
    return 7000