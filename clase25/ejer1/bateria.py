def clasificar_nivel_bateria(porcentaje):
    if porcentaje >=0 or porcentaje>=20:
        return "baja"
    if porcentaje >=21 or porcentaje>=80:
        return "media"
    if porcentaje >=81 or porcentaje>=100:
        return "alta"
    raise ValueError("el porcentaje debe estar entre 0 y 100")