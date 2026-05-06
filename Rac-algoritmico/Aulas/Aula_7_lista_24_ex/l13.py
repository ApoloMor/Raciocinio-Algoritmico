'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 - Janeiro, 2 - Fevereiro, . . . )'''
temps_col = []
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro' ]
while True:
    mes = float(input(F"Digite a temperatura média de mês de {meses[len(temps_col)]}: "))
    temps_col += [mes]
    if len(temps_col) == 12:
        break
media = sum(temps_col) / 12
print(f"a média anual de temperatura é: {media:.2f}")
n=0
print("Os meses que ficaram acima da média anual de temperatura são:")
for i in range(12):
    if temps_col[i] > media:
        n+=1
        print(n,"-", meses[i]) # ou mostra o numero do mês (EX: abril >> 04) com i + 1 no lugar de n