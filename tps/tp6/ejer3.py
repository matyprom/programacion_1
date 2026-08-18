# Mostrar todos los títulos publicados después de 2010.
# Obtener un set con los géneros disponibles.
# Crear un diccionario donde la clave sea el género y el valor la cantidad de libros de ese género.
# Mostrar qué género tiene más libros.
# Mostrar los géneros sin repetirse.
desp_2010=[]
generos_disp=set()
generos={}
libros = [
    ("El Principito", "Antoine de Saint-Exupéry", 1943, "Novela"),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela"),
    ("Breves respuestas a las grandes preguntas", "Stephen Hawking", 2018, "Ciencia"),
    ("Sapiens", "Yuval Noah Harari", 2011, "Historia"),
    ("Física para la ciencia y la tecnología", "Serway", 2010, "Ciencia")
]
for titulo, autor, anio, genero in libros:
    if anio >= 2010:
        desp_2010.append(titulo)
    generos_disp.add(genero)
    if genero not in generos:
        generos[genero]=[]
    generos[genero].append(titulo)
    # print(f"{genero}: {len(titulo)} libros")
for genero, titulos in generos.items():
    print(f"{genero}: {len(titulos)} libros")

print(generos)
print(desp_2010)
print("los generos disponibles son: ", generos_disp)

