clave_almacenada="1234"
uso_clave_token=bool(input("usas clave token?")=="s")

if uso_clave_token==False:
    clave_ingresada=input("pasame la contraseña")
    if clave_almacenada == clave_ingresada:
        print("acceso con clave")
    elif uso_clave_token:
        print("acceso permitido")
    else:
        print("acceso denegado")

