#forma normal


# cuadrados=[]
# for x in range(5):
#     cuadrados.append(x**2)

# print(cuadrados)
#----------------------------------------------------------------
#forma con comprension lista
cuadrados = [x**2 for x in range(5)]
print(cuadrados)

#----------------------------------------------------------------------
#forma con comprension diccionario

cuadrados={x:x**2 for x in range(5)}
print(cuadrados)

#
#forma con compresion 
cuadrados={x**2 for x in range(5)}+0


