"""
Criar um programa que recebe um texto digitado pelo usuário e
o imprime apenas com consoantes, removendo as vogais. Obs.:
desconsiderar letras maiúsculas e acentos.
"""
texto = input("Digite um texto:")
txt1 = ""
for i in texto:
    if i not in "aeiou":
        txt1 += i
print(i)