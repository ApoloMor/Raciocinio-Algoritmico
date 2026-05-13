'''Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.'''
numeros = []
for i in range(5):
    num = int(input("Digite um número inteiro: "))
    numeros += [num]
print("Os números digitados são:")
for num in numeros:
    print(num) # ou print(numeros)