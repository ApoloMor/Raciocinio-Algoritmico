"""Elaborar um programa que receba o nome completo do usuário, e imprima apenas o
primeiro e último nome."""
nome_full = input("Digite seu nome completo: ")
first = ""
last = ""
temp = ""
for l in nome_full:
    if l != " ":
        temp += l
    else:
        if first == "":
            first = temp
        temp = ""
# depois do loop o temp guarda o último nome
last = temp
print(first + " " + last)