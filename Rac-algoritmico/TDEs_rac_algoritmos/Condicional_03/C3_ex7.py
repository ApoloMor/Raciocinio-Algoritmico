""" Implemente um programa que solicite o dia, mês e ano (com 4 dígitos) de nascimento
de uma pessoa, e pergunte em qual formato deve exibir a data, como segue:
Código de Exibição de Data
• 1 – Data simples. Ex.: 10/08/1990;
• 2 – Data abreviada. Ex.: 10/ago/1990;
• 3 – Data completa. Ex.: 10 de agosto de 1990."""
dia = input("Dia: ").zfill(2)
mes = input("Mês: ").zfill(2)
ano = input("Ano: ")

formato = input("Formato (1, 2 ou 3): ")

# conversão do mês
match mes: #match é uma função que cumpre o mesmo objetivo de if/elif, match > valor a ser comparado, case> comparação em si.
    case "01":
        abrev = "jan"
        completo = "janeiro"
    case "02":
        abrev = "fev"
        completo = "fevereiro"
    case "03":
        abrev = "mar"
        completo = "março"
    case "04":
        abrev = "abr"
        completo = "abril"
    case "05":
        abrev = "mai"
        completo = "maio"
    case "06":
        abrev = "jun"
        completo = "junho"
    case "07":
        abrev = "jul"
        completo = "julho"
    case "08":
        abrev = "ago"
        completo = "agosto"
    case "09":
        abrev = "set"
        completo = "setembro"
    case "10":
        abrev = "out"
        completo = "outubro"
    case "11":
        abrev = "nov"
        completo = "novembro"
    case "12":
        abrev = "dez"
        completo = "dezembro"
    case _:
        print("Mês inválido")
        exit()

# saída conforme formato
if formato == "1":
    print(f"{dia}/{mes}/{ano}")
elif formato == "2":
    print(f"{dia}/{abrev}/{ano}")
elif formato == "3":
    print(f"{dia} de {completo} de {ano}")
else:
    print("Formato inválido")
