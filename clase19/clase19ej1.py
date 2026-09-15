from datetime import datetime, timedelta
import time

# ahora = datetime.now()

# print(datetime.now().year)
# print(type(ahora))

# time.sleep(3)
# print(datetime.now().second)

# fechayhora=datetime.strptime("02092020 1745", "%d%m%Y  %H%M")

# print(fechayhora)
#----------------------------------------------------------------------
# fechas = [
#     "21-08-2026 18:45:20",
#     "2026/08/21 07:30",
#     "21.08.26"
# ]

# formatos=[
#     "%d-%m-%Y %H:%M%S",
#     "%Y/%m/%d %H:%M",
#     "%d.%m.%y"
# ]

# fechayhora1=datetime.strptime(fechas[0], "%d-%m-%Y %H:%M:%S")
# fechayhora2=datetime.strptime(fechas[1], "%Y/%m/%d %H:%M")
# fechayhora3=datetime.strptime(fechas[2], "%d.%m.%y")

# print(datetime.strptime(fechas[0], "%d-%m-%Y %H:%M:%S"))
# print(datetime.strptime(fechas[1], "%Y/%m/%d %H:%M"))
# print(datetime.strptime(fechas[2], "%d.%m.%y"))
#-------------------------------------------------------------------------
# fecha="2026-09-15T18:25:30"

# formatofecha=datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S")
# print(formatofecha)
# print(formatofecha.strftime("%Y/%m/%d %H.%M.%S"))
#------------------------------------------------------------------
# fecha_1 = datetime.strptime("01/12/2026 08:15", "%d/%m/%Y %H:%M")
# fecha_2 = datetime.strptime("01/09/2026 10:30", "%d/%m/%Y %H:%M")

# if fecha_1 < fecha_2:
#     print("La primera fecha ocurre antes")
# elif fecha_1 > fecha_2:
#     print("La segunda fecha ocurre antes")
# else:
#     print("Las fechas son iguales")
# -----------------------------------------------------------------------------


fecha = datetime(2026, 9, 2, 17, 30)
vencimiento = fecha + timedelta(minutes=365)

print(vencimiento)