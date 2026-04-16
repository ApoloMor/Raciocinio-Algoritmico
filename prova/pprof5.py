#entrada »» aabcc   saida »» a2b1c2
txt = input("Digite a string: ")
r = ""
ch = ""
cont =0
for c in txt:
    if c!= ch:
        if cont > 0:
            r += f"{c}{cont}"
        ch = c
        cont += 1
    else:
        cont += 1