alumnos = [
    {"nombre": "paula","nota":8},
    {"nombre": "juan", "nota":3},
    {"nombre": "pablo", "nota":6}]

alumnos.append(
    {"nombre":"jhon", "nota":2}
)

for alumnos in alumnos:
    if alumnos["nota"]>=4:
        print(alumnos["nombre"], "aprobó")
    else:
        print(alumnos["nombre"], "desaprobo")