'''
1. Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer no
plano, P(x1,y1) e P(x2,y2), escreva a distância entre eles. A fórmula que efetua tal cálculo
d = raizde{(x2-x1)² + (y2-y1)²}
é:
'''

import math
x1 = int(input("Digite o valor de x1:"))
x2 = int(input("Digite o valor de x2:"))
y1 = int(input("Digite o valor de y1:"))
y2 = int(input("Digite o valor de y2:"))
d = ((x2-x1)**2 + (y2-y1)**2)**0.5
print ("O resultado é {d:.2f}")
