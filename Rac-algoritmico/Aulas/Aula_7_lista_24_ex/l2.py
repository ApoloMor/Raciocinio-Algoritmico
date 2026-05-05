''' Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa'''
numerosR = []
for i in range(10):
    num = float(input("Digite um número real: "))
    numerosR += [num]
numerosR.reverse()
print(numerosR)