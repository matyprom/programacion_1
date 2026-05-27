codigo=input("escribi el codigo con este formato [PROG-101]")

gion=codigo.count("-")
codigo_separado=codigo.split("-")
codigo_num=codigo_separado[1].strip()
codigo_let=codigo_separado[0].strip()
print(len(codigo_let))
print(len(codigo_num))

if codigo_num.isnumeric() and codigo_let.isalpha()and gion==1:
    codigo_final = codigo_let.upper() + "-" + codigo_num
    print(f"codigo valido: {codigo_final}")
else:
    print("codigo invalido")