ciudades = []
fechas = []
registros = [
    ("2026-04-07", "Bariloche", 18),
    ("2026-04-07", "Viedma", 31),
    ("2026-04-07", "El Bolson", 24),
    ("2026-04-14", "Bariloche", 20),
    ("2026-04-14", "Viedma", 29),
    ("2026-04-14", "El Bolson", 22),
    ("2026-04-21", "Bariloche", 17),
    ("2026-04-21", "Viedma", 27),
    ("2026-04-21", "El Bolson", 19)
]
promedio_ciudad={}
for fecha, ciudad, temp in registros:
    if ciudad not in promedio_ciudad:
        promedio_ciudad[ciudad]=[]
    promedio_ciudad[ciudad].append(temp)
    ciudades.append(ciudad)
    fechas.append(fecha)
for ciudad in promedio_ciudad:
    tem=promedio_ciudad[ciudad]
    promedio_ciudad[ciudad]= sum(tem)/len(tem)
print(set(ciudades))
print(set(fechas))
print(promedio_ciudad)