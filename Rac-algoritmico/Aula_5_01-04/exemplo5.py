#pegar o ultimo nome de um nome completo
nome = input("digite seu nome completo:")
parcial = ""
encontrei = False
for letra in nome:
    if letra != " ":
        if encontrei:
            parcial = ""
            encontrei = False
        parcial += letra
    else:
        encontrei = True
print(parcial)