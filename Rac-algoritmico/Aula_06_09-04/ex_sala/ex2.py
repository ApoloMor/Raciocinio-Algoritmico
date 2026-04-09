"""
Criar um programa que pede ao usuário 5 números, e informa
qual é o menor e qual é o maior deles.
"""
num = int (input("Digite um número:"))
maior = num
menor = num
for i in range(4):
    num = int(input("Digite um número:"))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(maior, menor)