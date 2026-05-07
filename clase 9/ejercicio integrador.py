alumnos = [
    {
        "nombre":"joaquin",
        "notas":[8,9,7],
        "materias":{"programacion", "matematica"}
    },
    {
        "nombre":"juan",
        "notas":[8,9,7],
        "materias":{"programacion", ""}
    },
    {
        "nombre":"kaká",
        "notas":[3,9,7],
        "materias":{"programacion", "ingles"}
    }
    
]

for alumnos in alumnos:
    print(alumnos["nombre"])
for alumnos in alumnos:
    suma=0
    catidad=0
    for notas in alumnos["notas"]:
        suma+=notas
        cantidad+=1
    print(suma, cantidad)
