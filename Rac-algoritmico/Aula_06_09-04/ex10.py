"""Criar um Programa que simule um caixa eletrônico. O programa
deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. A saber:
a. Notas disponíveis: 1, 5, 10, 50 e 100 reais;
b. Valor mínimo de saque: R$ 10,00 reais;
c. Valor máximo de saque: R$ 600,00 reais.
"""
while True:
    try:
        saque = int(input("Digite o valor do saque (10 -- 600): "))
    except ValueError:
        print("Insira um valor válido!!!")
        continue
    if 10 <= saque <= 600:
        resto = saque
        n100 = resto // 100
        resto = resto % 100
        n50 = resto // 50
        resto = resto % 50
        n10 = resto // 10
        resto = resto % 10
        n5 = resto // 5
        resto = resto % 5
        n1 = resto
    if n100 > 0:
        print(f"Você usou {n100} nota(s) de 100")
    if n50 > 0:
        print(f"Você usou {n50} nota(s) de 50")
    if n10 > 0:
        print(f"Você usou {n10} nota(s) de 10")
    if n5 > 0:
        print(f"Você usou {n5} nota(s) de 5")
    if n1 > 0:
        print(f"Você usou {n1} nota(s) de 1")
    agn = input("Deseja fazer outro saque?(s/n)").lower()
    if agn == "n":
        break