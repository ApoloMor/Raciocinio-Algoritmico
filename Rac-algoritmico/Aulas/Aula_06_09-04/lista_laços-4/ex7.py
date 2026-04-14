"""Elaborar um programa que solicita várias palavras ao usuário, sendo que o critério de
parada é digitar uma palavra vazia. Contar e exibir quantas letras A existem neste
conjunto de palavras."""
contador = 0
palavra = " "
while palavra != "":
    palavra = str(input("Digite uma palavra: (Enter para concluir)"))
    for l in palavra:
        if l in "aAáÁãÃâÂ":
            contador += 1
print(contador)