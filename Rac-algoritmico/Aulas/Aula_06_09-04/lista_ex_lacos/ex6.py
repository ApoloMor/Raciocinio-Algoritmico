"""Elaborar um programa que receba o nome completo do usuário, e imprima apenas o
primeiro e último nome."""
nome_full = input("Digite seu nome completo: ")
first = ""
last = ""
encontrei = False
for l in nome_full:
    if l == " ":
        encontrei = True
    if encontrei == False:
        first += l
    else:
        last += l
print (first + last)
        
        