D1 = int(input("Digite o 1° digito de seu CPF:"))
D2 = int(input("Digite o 2° digito de seu CPF:"))
D3 = int(input("Digite o 3° digito de seu CPF:"))
D4 = int(input("Digite o 4° digito de seu CPF:"))
D5 = int(input("Digite o 5° digito de seu CPF:"))
D6 = int(input("Digite o 6° digito de seu CPF:"))
D7 = int(input("Digite o 7° digito de seu CPF:"))
D8 = int(input("Digite o 8° digito de seu CPF:"))
D9 = int(input("Digite o 9° digito de seu CPF:"))
D10 = int(input("Digite o 10° digito de seu CPF:"))
D11 = int(input("Digite o 11° digito de seu CPF:"))

#validação prévia:
if D1 == D2 == D3 == D4 == D5 == D6 == D7 == D8 == D9 == D10 == D11:
    print("CPF INVÁLIDO!")

#validando o décimo digito:
soma = D1 *10 + D2 * 9 + D3 * 8 + D4 * 7 + D5 * 6 + D6 * 5 + D7 * 4 + D8 * 3 + D9 * 2
md = (soma * 10) % 11

if md == 10:
    md = 0

if md != D10:
    print("CPF INVÁLIDO!")
else:
    print("50% validado...")

    #validando o décimo-pimeiro digito:
    soma2 = D1 * 11 + D2 * 10 + D3 * 9 + D4 * 8 + D5 * 7 + D6 * 6 + D7 * 5 + D8 * 4 + D9 * 3 + D10 * 2
    md2 = (soma2 * 10) % 11

    if md2 == 10:
        md2 = 0

    if md2 == D11:
        print("CPF válidado com sucesso!")
    else:
        print("CPF INVÁLIDO!")