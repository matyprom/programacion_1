def sumador(anterior, siguiente):
    if siguiente<anterior:
        raise ValueError(f"el numero siguiente no puede ser mas chico que el anterior")
    else:
        return siguiente+anterior


print (sumador (2,3))