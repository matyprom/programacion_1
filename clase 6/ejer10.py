lista=[]
us=input("pasame productos").lower()

while us!="fin":
    print(us)
    lista.append(us)
    us=input("pasme productos o fin").lower()

print(len(lista))
print(lista[0])
print(lista[-1])