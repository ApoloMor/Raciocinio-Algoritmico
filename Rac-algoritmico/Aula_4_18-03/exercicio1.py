""""
- rendimento mensal;
- número de dependentes;
- valor da pensão alimentícia;
- outras deduções.
 base de cálculo = rendimento – [(dedução por dependente *
número de dependentes) + valor da pensão alimentícia + outras
deduções]
"""


salario = float(input("Digite seu salario: "))
outras_deducoes = float(input("Digite quanto paga de outras deduções, se não recebe digite 0:"))
pensao = float(input("Digite quanto paga de pensão, se não digite 0:"))
calculo_dependentes = 0
dependentes = int(input("quantos dependetes possui: "))
    if dependentes > 0:
        calculo_dependentes = 189,59 * dependentes

aliquota1 = 0.075
aliquota2 = 0.15
aliquota3 = 0.225
aliquota4 = 0.275

faixa1 = 1.903.98
faixa2 = 2.826.65
faixa3 = 3.751.05
faixa4 = 4.664.68

imposto = 0

calculo1 = salario - (calculo_dependentes + pensao + outras_deducoes)
    if calculo1 <= faixa1:
        imposto = 0
    elif calculo1 > faixa1 and calculo1 < faixa2:
        imposto = (calculo1 - faixa1) * aliquota1



"""" imposto = (faixa 1, se base de cálculo <= faixa 1), + ..., +
(faixa 4, se base de cálculo <= faixa 4) + (faixa 5, se base de cálculo
> faixa 4)"""




