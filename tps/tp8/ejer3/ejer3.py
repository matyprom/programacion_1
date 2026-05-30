#Pida al usuario el nombre de 4 alumnos.
# Valide que el nombre no esté vacío.
# Guarde los nombres válidos en una lista.
# Escriba los nombres en un archivo llamado alumnos.txt, un nombre por línea.
# Cierre el archivo.
lista_alumnos=[]
for alumnos in range(5):
    alumno=input("decime tu nombre")
    if alumno != "":
        lista_alumnos.append(alumno)
    else:
        alumno2=input("el nombre esta vacio, pasame un nombre valido")
        lista_alumnos.append(alumno2)
archivo=open("alumnos.txt","w")
for alumnos in lista_alumnos:
    archivo.write(alumnos + "\n")

archivo.close()


