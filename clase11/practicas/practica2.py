usuarios=[
    "ana,programacion",
    "juan,matematica",
    "lucia,fisica"
]
nombres=[]
materia=[]
for usuario in usuarios:
    lineas=usuario.split(",")
    nombres.append(lineas[0])
    materia.append(lineas[1])
    print(lineas)
    print(nombres)

