class Libro:
    def __init__(self, titulo, autor, cant_pag):
        self.titulo = titulo
        self.autor = autor
        self.cant_pag = cant_pag
    def Libro_extenso(self):
        if self.cant_pag>50:
            return True
        return False
    def ficha(self):
        return (self.titulo, self.autor)

libro1= Libro("boca", "yo", 25)
libro2= Libro("river", "juan", 89)

# print(libro1.titulo, libro1.cant_pag)
# print(libro2.titulo, libro2.cant_pag)

# libro1.cant_pag = 99

# print(libro1.cant_pag)

print(f"libro y autor {libro1.ficha()} el libro es extenso? {libro1.Libro_extenso()}")
print(f"libro y autor {libro2.ficha()} el libro es extenso? {libro2.Libro_extenso()}")
