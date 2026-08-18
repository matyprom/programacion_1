# Consignas
# Antes de empezar a escribir código, desarrollá una explicación completa de cómo resolverías el problema. Tomate el tiempo para pensar la estrategia, los pasos, las estructuras de datos y las decisiones lógicas. Escribí ese análisis al comienzo del archivo, antes de la implementación.
###recorreria la lista con un for, y 

##
# Mostrar promedio de cada estudiante.
# Clasificar cada estudiante en:
# Promociona si promedio >= 8 y asistencias >= 8
# Regulariza si promedio >= 4 y asistencias >= 6
# Recursa en otro caso
# Mostrar cuántos estudiantes hay en cada categoría.
# Mostrar la comisión con mejor promedio general.
# Generar un set con nombres de estudiantes en riesgo (Recursa).
estudiantes = [
    {"nombre": "Ana", "notas": [7, 8, 6], "asistencias": 9, "comision": "C1"},
    {"nombre": "Luis", "notas": [4, 5, 3], "asistencias": 6, "comision": "C1"},
    {"nombre": "Mora", "notas": [9, 8, 10], "asistencias": 10, "comision": "C2"},
    {"nombre": "Pedro", "notas": [2, 4, 3], "asistencias": 7, "comision": "C2"}
]
promociona=0
regulariza=0
recursa=0
recursan=[]
prom_c1=[]
prom_c2=[]

for estudiante in estudiantes:
    promedio=sum(estudiante["notas"])/len("notas")
    print(f"el promedio de {estudiante["nombre"]} es {promedio}")
    if promedio >= 8 and estudiante["asistencias"] >=8:
        print(f"{estudiante["nombre"] } promociona")
        promociona+=1
    elif promedio >= 4 and estudiante["asistencias"] >=6:
        print(f"{estudiante["nombre"] } regulariza, rinde el final")
        regulariza+=1
    else:
        print(f"{estudiante["nombre"] } recursa")
        recursa+=1
        recursan.append(estudiante["nombre"])
    if estudiante["comision"]=="C1":
        prom_c1.append(promedio)
    elif estudiante["comision"]=="C2":
        prom_c2.append(promedio)

print(f"hay {promociona} que promocionan, {regulariza} que regurarizan y {recursa} que recursan")

promedio_general_c1=sum(prom_c1)/len(prom_c1)
promedio_general_c2=sum(prom_c2)/len(prom_c2)
if promedio_general_c1<promedio_general_c2:
    print("c2 tiene mejor promedio")
else:
    print("c1 tiene mejor promedio")
set(recursan)
print("los estudiantes que en riesgo de recurar son ", recursan)

