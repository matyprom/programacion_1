# mi_primer_diccionario={
#     "clave_1": "valor_1",
#     "clave_2": "valor_2"
# }
# print(mi_primer_diccionario)
# print(type(mi_primer_diccionario))
#---------------------------------------------------------------------------------------

# alumno_tupla= ("paula", "perez", 8)
# print(alumno_tupla[2])

# alumno_dict={
#     "nombre": "paula",
#     "apellido": "perez",
#     "nota":8
# }

# print(alumno_dict["nombre"])

#----------------------------------------------------------------------------------------
# persona={
#     "nombre":"martin",
#     "edad": 20
# }
# #imprime el nombre
# print(persona["nombre"])
# #cambia la edad
# persona["edad"]=21
# #agrega ciudad
# persona["ciudad"]="bariloche"
# #imprime si ciudad esta en el diccionario
# print("ciudad" in persona)
# #guarda solo las keys
# keys=persona.keys()
# #guarda solo los values
# values=persona.values()

# print(keys)
# print(values)
# print(persona)

#--------------------------------------------------------------------------------------------------

persona={
    "nombre":"martin",
    "edad": 20,
    "ciudad": "bariloche"

}

for clave in persona:
    print(clave, persona[clave])