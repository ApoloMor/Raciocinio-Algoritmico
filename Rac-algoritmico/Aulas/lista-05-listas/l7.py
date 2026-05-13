'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números'''
numeros = []
for i in range(1,6):
    num = int(input(f"Digite o {i} número:"))
    numeros.append(num)
soma = sum(numeros)
multiplic =  numeros [0] * numeros[1] * numeros[2] * numeros[3] * numeros [4]
print(numeros, soma, multiplic)