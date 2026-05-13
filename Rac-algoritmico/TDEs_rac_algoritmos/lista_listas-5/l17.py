'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será
determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco
distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O
programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme
o exemplo abaixo:
Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m'''
atletas = []
media = 0
numeracao = ['Primeiro Salto: ', 'Segundo Salto: ', 'Terceiro Salto: ', 'Quarto Salto: ', 'Quinto Salto: ']
while True:
    atleta = input("Nome do atleta: (Enter para finalizar)")
    if atleta == "":
        break
    saltos = []
    for i in range(5):
        distancia = float(input(f"{numeracao[i]}"))
        saltos.append(distancia)
    media = sum(saltos) / 5
    atletas.append([atleta, saltos, media])
for atleta in atletas:
    nome = atleta[0]
    saltos = atleta[1]
    media = atleta[2]
    print(f"Atleta: {nome}")
    print("Saltos:", end=" ")
    for i in range(len(saltos)):
        if i < len(saltos) - 1:
            print(saltos[i], end=" - ")
        else:
            print(saltos[i])
    print(f"Média dos saltos: {media:.1f} m\n")

