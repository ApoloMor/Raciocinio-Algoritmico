'''Criar um programa que cadastre locais históricos do mundo com
suas coordenadas fazendo uso de tuplas com parâmetros
nomeados. Dica: usar a função namedtuple()'''
from collections import namedtuple
Local = namedtuple('Local', ['nome', 'cordX', 'cordY'] )
pontos = []
while True:
    nomeP = input('Nome do ponto: ')
    cordx = input('insira a coordenada x: ')
    cordy = input('insira a coordenada y: ')
    ponto = Local(nomeP, cordx, cordy)
    pontos.append(ponto)
    continuar = input("Deseja cadastrar outro ponto? (s/n): ").lower()
    if continuar != 's':
        break
print(pontos)