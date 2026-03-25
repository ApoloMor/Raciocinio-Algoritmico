'''Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) e calcule a
seguinte expressão:
D= R+S/2 ---- R= (a+b)**2 --- S = (b+c)**2
'''

A = int(input("Digite o valor de A:"))
B = int(input("Digite o valor de B:"))
C = int(input("Digite o valor de C:"))
R = (A + B) ** 2
S = (B + C) ** 2
D = (R + S) / 2
print (f"D é igual a: {D:.2f}")