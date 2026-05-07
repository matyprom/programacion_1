# producto={
#     "nombre": "papa",
#     "precio": 60,
#     "stok": 5
# }

# producto["precio"]*=1.1

# producto["stok"]-=1
# print(producto)
# print(f"producto: {producto["nombre"]} - precio actualizado : {producto["precio"]} - stok: {producto["stok"]}")


#-------------------------------------------------------------------------------------------------------------------------
cuenta={
    "ususario": "Matias",
    "email": "mat@gmail.com",
    "activo": True
}

print(cuenta["email"])
cuenta["activo"]= False

cuenta["ultimo_login"]="ayer"
print(cuenta)