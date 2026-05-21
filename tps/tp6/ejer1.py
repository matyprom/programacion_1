ciudades = set()
fechas = set()
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
registros= set(registros)

for registros in registros:
    ciudad = registros[1]
    varfechas= registros[0]
    ciudades.add(ciudad)
    fechas.add(varfechas)


print(fechas)
print(ciudades)

#uh ni idea estoy re perdido