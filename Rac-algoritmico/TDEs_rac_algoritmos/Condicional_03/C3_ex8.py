dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
hora = int(input("Hora: "))
minuto = int(input("Minuto: "))
segundo = int(input("Segundo: "))

tipo = input("O que deseja adicionar? (segundo/minuto/hora/dia): ").lower()
qtd = int(input("Quantidade: "))

if tipo == "segundo":
    segundo += qtd
    if segundo >= 60:
        minuto += segundo // 60
        segundo = segundo % 60

    if minuto >= 60:
        hora += minuto // 60
        minuto = minuto % 60

    if hora >= 24:
        dia += hora // 24
        hora = hora % 24

if mes in [1,3,5,7,8,10,12]:
    dias_mes = 31
elif mes in [4,6,9,11]:
    dias_mes = 30
elif mes == 2: # verificar bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        dias_mes = 29
    else:
        dias_mes = 28
if dia > dias_mes:
    dia = 1
    mes += 1

if mes > 12:
    mes = 1
    ano += 1

print(f"{dia:02}/{mes:02}/{ano} {hora:02}:{minuto:02}:{segundo:02}")