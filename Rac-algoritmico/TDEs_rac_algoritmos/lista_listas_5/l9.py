'''Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
elementos do vetor'''
numeros = []
quadrados = []
for n in range(1,11):
    numero = int(input(f'Digite o {n}° número inteiro: '))
    numeros.append(numero)
for i in numeros:
    quadrados.append(i**2)
print(sum(quadrados))