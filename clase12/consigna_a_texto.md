De las siguientes consignas responder:

¿Cuales son los datos de entrada?
¿Qué resultado debe salir?
¿Qué estructuras necesito?
¿Qué validación mínima haría?
¿Qué caso puede romper el programa?

EJ1: Un sensor registra eventos con este formato:

"PUERTA_A;ABIERTA;18:03"
"PUERTA_B;CERRADA;18:04"
"PUERTA_A;ABIERTA;18:05"

Se quiere contar cuántas veces aparece cada puerta.

# respuesta 1:

1_ (puerta, estado, hora)
2_ puesta N : aparece n veces
3_ 
- guardo todos los datos en una lista
- normalizo los datos
- verifico si el formato es correcto
- corto los datos por ";"
- gaurdo el primer dato en otra lista 
- 

