'''
solicitar uma frase ao usuario , e exibir  a quantidade de vogais total e individual
1 letra a = a A à À á Á â Â
'''
soma_a = 0
soma_e = 0
soma_i = 0
soma_o = 0
soma_u = 0
frase = str(input("digite uma frase:"))
for letra in frase:
    if letra in "aAàÀáÁâÂãÃ":
        soma_a +=1
    if letra in "eEéÉêÊ":
        soma_e +=1
    if letra in "iIíÍîÎ":
        soma_i +=1
    if letra in "oOõÕóÓôÔ":
        soma_o +=1
    if letra in "uUùÙúÚûÛ":
        soma_u +=1
total = soma_a + soma_e + soma_i + soma_o + soma_u
print(f"o total de vogais é {total},\n tendo:\n{soma_a} letras a\n{soma_e} letras e\n{soma_i} letras i\n{soma_o} letras o\n{soma_u} letras u")