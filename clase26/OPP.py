class Televisor:
    def __init__(self, ubicacion, canal, volumen):
        self.ubicacion = ubicacion
        self.canal = canal
        self.volumen = volumen
        print("se creo la clase televisor")
    def volumen_porcentaje(self):
        return self.volumen * 10
    def cambiar_canal(self, nuevo_canal):
        self.canal = nuevo_canal

sala = Televisor ("sala", 4, 3)
cocina= Televisor("Cocina", 12, 7)

# # print(vars(sala))
# # print(vars(cocina))

# print(sala.volumen)

# sala.volumen = 5

# print (sala.volumen)

print(sala.volumen_porcentaje())
print(cocina.volumen_porcentaje())

sala.cambiar_canal(9)

print(sala.canal)