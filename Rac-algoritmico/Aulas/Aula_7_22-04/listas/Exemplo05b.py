"""
Elaborar um código que permite fazer um saque entre 10 e 600
reais em um caixa eletrônico, e mostra quantas notas de
1, 5, 10, 50 e 100 serão entregues.
"""
saque = 120
notas = [100, 50, 10, 5, 1]
for i in range(len(notas)):
    n = saque // notas[i]
    saque %= notas[i]
    notas[i] = n
print(notas)