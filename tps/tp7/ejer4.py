edad_usuario=input("pasame tu edad")

edad_pulida=edad_usuario.strip()
print(type(edad_pulida))
if edad_pulida.isnumeric():
    edad=int(edad_pulida)
    if edad<120 and edad>0:
        print(f"Edad registrada: {edad}")
    else:
        print("edad invalida")
else:
    print("edad invalida")
