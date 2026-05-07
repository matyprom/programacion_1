# mi_primer_conjunto= {1,2,3,3,4}
# print(type(mi_primer_conjunto))
# print(len(mi_primer_conjunto))
# print(mi_primer_conjunto)

#--------------------------------------------------

# nombres={"ana", "pedro", "juana"}
# nombres.add("kaká")
# print(nombres)

# nombres.remove("juana")
# print(nombres)

# print("ana" in nombres)

# lista_nombres=["ana","ana", "marco", "kaká"]
# print(set(lista_nombres))

#----------------inion interseccion y diferencia---------------------------------------------------------------

a={1, 2, 3}
b={9, 2, 4}

print("conjunto a", a)
print("conjunto b: ", b)
print("union: ", a|b)
print("interseccion: ", a&b)
print("deferencia: ", a-b)