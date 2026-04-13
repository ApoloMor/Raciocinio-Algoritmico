""""
- rendimento mensal;
- número de dependentes;
- valor da pensão alimentícia;
- outras deduções.
 base de cálculo = rendimento – [(dedução por dependente *
número de dependentes) + valor da pensão alimentícia + outras
deduções]
"""
while True:
    rendimento = float(input("Digite seu rendimento total: "))
    pensao = float(input("Digite quanto paga de pensão, se não digite 0:"))
    dependentes = int(input("quantos dependetes possui: "))
    if dependentes >= 0:
        calculo_dependentes = 189.59 * dependentes
    else:
        calculo_dependentes = 0
    outras_deducoes = float(input("Digite outras deduções (ou 0): "))

    aliquota1 = 0.075
    aliquota2 = 0.15
    aliquota3 = 0.225
    aliquota4 = 0.275

    faixa1 = 1903.98
    faixa2 = 2826.65
    faixa3 = 3751.05
    faixa4 = 4664.68

    calculo_rendimento = (rendimento - (calculo_dependentes + pensao + outras_deducoes))
    if calculo_rendimento < 0:
        calculo_rendimento = 0
    #Diferenças
    diferenca_faixa2 = (calculo_rendimento - faixa1)
    diferenca_faixa3 = (calculo_rendimento - faixa2)
    diferenca_faixa4 = (calculo_rendimento - faixa3)
    diferenca_faixa5 = (calculo_rendimento - faixa4)

    #Faixas completas
    faixa2_cheia = (faixa2 - faixa1) * aliquota1
    faixa3_cheia = (faixa3 - faixa2) * aliquota2
    faixa4_cheia = (faixa4 - faixa3) * aliquota3

    imposto = 0

    if calculo_rendimento <= faixa1: #Calculo dentro da faixa 1
        print("Você não paga imposto de renda.")

    elif calculo_rendimento <= faixa2: #Calculo dentro da faixa 2
        imposto = diferenca_faixa2 * aliquota1
        print(f"Você deve pagar {imposto:.2f}, se enquadra na faixa 2, com uma taxa de 7.5%")

    elif calculo_rendimento <= faixa3: #Calculo dentro da faixa 3
        imposto = diferenca_faixa3 * aliquota2 + faixa2_cheia
        print(f"Você deve pagar {imposto:.2f}, se enquadra na faixa 3, com uma taxa de 15%")

    elif calculo_rendimento <= faixa4: #Calculo dentro da faixa 4
        imposto = diferenca_faixa4 * aliquota3 + faixa3_cheia + faixa2_cheia
        print(f"Você deve pagar {imposto:.2f}, se enquadra na faixa 4, com uma taxa de 22.5%")

    elif calculo_rendimento > faixa4: #calculo acima da faixa 4
        imposto = diferenca_faixa5 * aliquota4 + faixa4_cheia + faixa3_cheia + faixa2_cheia
        print(f"Você deve pagar {imposto:.2f}, está acima da faixa 4, com uma taxa de 27.5%")

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != "s":
        break

"""" imposto = (faixa 1, se base de cálculo <= faixa 1), + ..., +
(faixa 4, se base de cálculo <= faixa 4) + (faixa 5, se base de cálculo
> faixa 4)"""



