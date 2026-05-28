# Interpretando consignas
## Verificaciones
Se pide verificar que un dato es un número?
```python
if dato.isnumeric():
```
Se pide verificar que tiene N cantidad de caracteres?
```python
if len(dato) == N
```

Se pide verificar que no sea un dato vacío?
RESPUESTA:
```python
if len(dato)==0:

if dato=="":
```
Se pide verificar que un elemento exista más de N veces?
RESPUESTA:
```python
if dato.count(";")==3:

```
Si tenemos que verificar que un texto contenga otro texto?
RESPUESTA:
```python
dato="aguante boca"
if "boca" in dato:

dato=["aguante boca"]
if "boca" in dato:

dato={"boca": {....}}
if "boca" in dato:

# funsiona para todo :)

```
### Repeticiones
Tenemos una lista de 25 datos, hay que verificar que todos sean números. ¿Qué hacemos?
RESPUESTA:
```python
datos=[1,2,3,4,...,25]
for dato in datos:
    if dato.isnumeric()
```
Hay que pedirle 5 nombres al usuario. ¿Que hacemos?
RESPUESTA:
```python
datos=[]
for idx in range(5):
    datos.append(input(f"pasame el nombre{idx}"))
```
Tenemos que pedir datos al usuario hasta que digan FIN. ¿Que usamos?
RESPUESTA:
```python

```
#### Archivos
Hay que leer un archivo:
RESPUESTA:
```python
f=open("archivo.txt", "r")
contenid=f.read()
contenido_lista=f.readline()
```
Hay que escribir un archivo:
RESPUESTA:
```python
f=open("archivo.txt", "w")#borra lo que habia en el archivo para volver a escribir
escribir=f.write("aguante bocaaa")
f.close()

```
¿Hay que cerrar un archivo?
RESPUESTA:
```python
archivo.close()
```
Tenemos que solicitarle al usuario nombre, apellido y año de nacimiento ¿Que hacemos?

```python
♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !"#$%&'())*+,-./01523456789:;<=>?@AEDEFGHIJKLM
```

Si tenemos que crear una estructura que tiene el nombre de producto como clave, dentro tenemos que tener precio, stock y tipo de producto. Usar la estructura más semántica posible.