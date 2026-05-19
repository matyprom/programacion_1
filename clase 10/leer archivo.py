
idx=0
archivo=open("nombres.txt", "r")

nombres = archivo.readlines()
archivo.close()
print(nombres)

for nombre in nombres:
    print(idx, nombre.strip())
    idx+=1

for idx, nombre in enumerate(nombres):
    j=0