limite = 0
pontos1 = 0
pontos2 = 0
i = int(input("escolha quantos pontos devem ser feitos para vencer: "))
while pontos1 < limite and pontos2 < limite:
    palpite1 = str(input("escolha pedra, papel ou tesoura(R,P,S): ")).upper()
    palpite2 = str(input("escolha pedra, papel ou tesoura(R,P,S): ")).upper()
    if palpite1 == palpite2:
        print("Empate!")
    elif palpite1 == "R" and palpite2 == "S":
        print("Jogador 1 ganhou!")
        pontos1 += 1

    elif palpite1 == "S" and palpite2 == "P":
        print("Jogador 1 ganhou!")
        pontos1 += 1

    elif palpite1 == "P" and palpite2 == "R":
        print("Jogador 1 ganhou!")
        pontos1 += 1

    elif palpite2 == "R" and palpite1 == "S":
        print("Jogador 2 ganhou!")
        pontos2 += 1

    elif palpite2 == "S" and palpite1 == "P":
        print("Jogador 2 ganhou!")
        pontos2 += 1

    elif palpite2 == "P" and palpite1 == "R":
        print("Jogador 2 ganhou!")
        pontos2 += 1

    else:
        print("Entrada inválida!")

    print(f"Placar: Jogador 1 = {pontos1} | Jogador 2 = {pontos2}")

# vencedor final
if pontos1 == i:
    print("🏆 Jogador 1 venceu o jogo!")
else:
    print("🏆 Jogador 2 venceu o jogo!")