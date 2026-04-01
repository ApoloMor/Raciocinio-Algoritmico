"""Criar um jogo de par ou ímpar, onde dois jogadores entram com seu palpite (par ou
ímpar) e seus valores de 1 a 5. Tomar por base os nomes: Jogador 1 e Jogador 2. Caso
um dos valores esteja fora dos parâmetros informados, mostrar uma mensagem
informando que esta rodada não valeu. Caso contrário, informa qual jogador ganhou esta
rodada"""
par = input("Jogador 1, escolha par ou ímpar: ")
valor1 = int(input("Jogador 1, escolha um valor de 1 a 5: "))
valor2 = int(input("Jogador 2, escolha um valor de 1 a 5: "))
if (valor1 < 1 or valor1 > 5) or (valor2 < 1 or valor2 > 5):
    print("Esta rodada não valeu. Valores fora dos parâmetros.")
else:
    soma = valor1 + valor2
    if (soma % 2 == 0 and par == "par") or (soma % 2 != 0 and par == "ímpar"):
        print("Jogador 1 ganhou esta rodada!")
    else:
        print("Jogador 2 ganhou esta rodada!")