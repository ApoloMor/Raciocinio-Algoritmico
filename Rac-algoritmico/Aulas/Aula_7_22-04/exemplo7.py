'''
listas multidimencionais
pegar ldados de 5 pontos turisticos
'''
pontos = []
for i in range(2):
    ponto = input("Digite o nome do ponto: ")
    lat = float(input("Digite a latitude: "))
    lon = float(input("Digite a longitude: "))
    info = [[ponto], lat, lon]
    pontos.append(info)
print(pontos)
