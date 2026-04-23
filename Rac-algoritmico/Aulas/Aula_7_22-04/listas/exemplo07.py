"""
Listas Multidimoensinoais
Pegar dados de 5 pontos turísticos
"""
from pdb import post_mortem

pontos = []
for i in range(5):
    ponto = input("Digite o nome do ponto turístico: ")
    lat = float(input("Digite a latitude: "))
    lon = float(input("Digite a longitude: "))
    info = [ponto, lat, lon]
    pontos.append(info)
print(pontos)
pontos[0][0]