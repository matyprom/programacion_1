# def saludar():
#     print("que onda")

# saludar()

#---------------------------------------------------------------------------------------------------
# def saludar(nombre):
#     print(f"que onda {nombre}😊")

# saludar("juan")
#---------------------------------------------------------------------------------------------------
# def saludar(nombre1, nombre2):
#     print(f"que onda {nombre1} y {nombre2}😊")

# saludar("juan", "pedrro")

#---------------------------------------------------------------------------------------------------
# def saludar(nombre1="juan", nombre2="PANCHO"):
#     print(f"hola {nombre1} y {nombre2}")
# saludar ()

# saludar( nombre1="pedro", nombre2="pedro" )
#---------------------------------------------------------------------------------------------------
# def saludar(nombre):
#     return f"hola {nombre}"#devuelve eso
# saludar("juan")
#---------------------------------------------------------------------------------------------------
# def mayor(edad):
#     if edad >=18:
#         return True
#     else:
#         return False
# print (mayor(12))
#---------------------------------------------------------------------------------------------------
def trae_documento():
    return input("trae documento si/no") == "si"

def edad():
    return int(input("ingresa tu edad"))

def puede_pasar(documento, edad):
    return documento==True and edad >=18

documento = trae_documento()
edad= edad()

if puede_pasar(documento, edad):
    print("ouede pasar")
else:
    print("no pasa")
