'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor
PAR e os números IMPARES no vetor impar. Imprima os três vetores'''
total = []
par = []
impar =[]
for i in range (1,21):
    temp = int(input(f"Digite o {i} número: "))
    total += [temp]
    if temp % 2 == 0:
        par.append([temp])
    else:
        impar.append([temp])
print(f"Os numeros digitados foram: {total}\nOs pares são: {par}\nOs ímpares são: {impar}")