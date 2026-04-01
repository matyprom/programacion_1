documento=bool(input("tenes documento")=="s")
edad=int(input("que edad tenes?"))

if edad>=18 and documento == True:
    print("entra pa")
else:
    print("no entras pa")