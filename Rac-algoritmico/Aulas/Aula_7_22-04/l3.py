'''Criar um programa que lê as temperaturas médias de cada mês
do ano e as armazena em uma lista. Usar um outro vetor para
guardar e exibir, quando necessário, os nomes dos meses do ano.
Calcular a média anual de temperatura, e informar quais meses
ficaram acima desta média anual'''
temps_col = []
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro' ]
while True:
    mes = float(input(F"Digite a temperatura média de mês de {meses[len(temps_col)]}: "))
    temps_col += [mes]
    if len(temps_col) == 12:
        break
media = sum(temps_col) / 12
print(f"a média anual de temperatura é: {media:.2f}")
print("Os meses que ficaram acima da média anual de temperatura são:")
for i in range(12):
    if temps_col[i] > media:
        print(meses[i])
print("Os meses que ficaram abaixo da média anual de temperatura são:")
for i in range(12):
    if temps_col[i] < media:
        print(meses[i])