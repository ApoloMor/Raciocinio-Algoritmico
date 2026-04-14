"""Solicitar ao usuário duas datas e calcular a quantidade de dias entre elas (levar em
consideração os anos bissextos)"""
print("Digite a primeira data:")
dia = int(input("Dia: ").zfill(2))
mes = int(input("Mês: ").zfill(2))
ano = int(input("Ano: \n"))
print("Digite a segunda data:")
dia2 = int(input("Dia: ").zfill(2))
mes2 = int(input("Mês: ").zfill(2))
ano2 = int(input("Ano: \n"))
dias1 = 0
for a in range(0, ano):
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        dias1 += 366
    else:
        dias1 += 365
for m in range(1, mes):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        dias1 += 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        dias1 += 30
    elif m == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            dias1 += 29
        else:
            dias1 += 28
dias1 += dia
dias2 = 0
for a in range(0, ano2):
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        dias2 += 366
    else:
        dias2 += 365
for m in range(1, mes2):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        dias2 += 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        dias2 += 30
    elif m == 2:
        if (ano2 % 4 == 0 and ano2 % 100 != 0) or (ano2 % 400 == 0):
            dias2 += 29
        else:
            dias2 += 28
dias2 += dia2
if dias1 >= dias2:
    print(f"A quantidade de dias entre as datas é: {dias1 - dias2}")
else:
    print(f"Erro")