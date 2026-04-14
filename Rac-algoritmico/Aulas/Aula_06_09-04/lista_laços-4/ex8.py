'''Elaborar um programa que receba um número em binário, e mostre o seu valor em
decimal'''
decimal = 0
potencia = 0
binario = str(input("Digite um numero em binário: ")) 
invertido = ""
for i in binario:
    invertido = i + invertido
for bit in invertido:
    if bit == '1':
        decimal += 2**potencia
    potencia += 1
print("O número em decimal é:", decimal)