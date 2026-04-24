# def cantidad (nro_usuario):
#     cant=0
#     for i in nro_usuario:
#         cant+=1
#     return cant


# nro_usuario=[]

# usuario=int(input("escribi un numero"))

# while usuario!=0:
#     nro_usuario.append(usuario)
#     print(nro_usuario)
#     usuario=int(input("escribi un numero"))
# print("adivinaste el numero")
# print(nro_usuario)
# print(cantidad(nro_usuario))

nums=[10, -1,2,3,5,7,6,-7,8,-10]
par=[]
numeros=[]

for i in range(len(nums)):
    n=nums[i]%2
    numeros.append(n)
    if nums[i]%2==0:
        par.append(nums[i])
print (par)
print(numeros)
