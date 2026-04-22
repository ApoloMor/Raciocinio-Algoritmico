"""
elaborar um codigo que permita o usurio realizar saques de 10 a 600
e retornar quantas notas de 1, 5, 10, 50, 100
"""
notas = [100, 50, 10, 5, 1]
n_notas = []
saq = int(input("Digite o valor de saque entre R$10 e R$600: "))
for nota in notas:
    n = saq // nota
    saq %= nota
    n_notas.append(n)
print(n_notas)