'''Criar um programa que lê as temperaturas médias de cada mês
do ano e as armazena em uma lista. Usar um outro vetor para
guardar e exibir, quando necessário, os nomes dos meses do ano.
Calcular a média anual de temperatura, e informar quais meses
ficaram acima desta média anual'''
temps_col = []
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro' 'dezembro' ]
while True:
    janeiro = float(input("Digite a temperatura média de mês de janeiro: "))
    temps_col += [janeiro]

    fevereiro = float(input("Digite a temperatura média de mês de fevereiro: "))
    temps_col += [fevereiro]

    março = float(input("Digite a temperatura média de mês de março: "))
    temps_col += [março]

    abril = float(input("Digite a temperatura média de mês de abril: "))
    temps_col += [abril]

    maio = float(input("Digite a temperatura média de mês de maio: "))
    temps_col += [maio]

    junho = float(input("Digite a temperatura média de mês de junho: "))
    temps_col += [junho]
    
    julho = float(input("Digite a temperatura média de mês de julho: "))
    temps_col += [julho]
    
    agosto = float(input("Digite a temperatura média de mês de agosto: "))
    temps_col += [agosto]
    
    setembro = float(input("Digite a temperatura média de mês de setembro: "))
    temps_col += [setembro]
    
    outubro = float(input("Digite a temperatura média de mês de outubro: "))
    temps_col += [outubro]
    
    novembro = float(input("Digite a temperatura média de mês de novembro: "))
    temps_col += [novembro]
    
    dezembro = float(input("Digite a temperatura média de mês de dezembro: "))
    temps_col += [dezembro]
    break
media = sum(temps_col) / 12
print(f"A média anual de temperatura é: {media}")
print(f"a média anual de temperatura é: {media}")
print("Os meses que ficaram acima da média anual de temperatura são:")
for i in range(12):
    if temps_col[i] > media:
        print(meses[i])
print("Os meses que ficaram abaixo da média anual de temperatura são:")
for i in range(12):
    if temps_col[i] < media:
        print(meses[i])