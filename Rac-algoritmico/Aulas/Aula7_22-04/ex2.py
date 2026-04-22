"""
- rendimento mensal;
- número de dependentes;
- valor da pensão alimentícia;
- outras deduções.
base de cálculo = rendimento – [(dedução por dependente * número de dependentes) + valor da pensão alimentícia + outras deduções]
imposto = (faixa 1, se base de cálculo <= faixa 1), + ..., +
(faixa 4, se base de cálculo <= faixa 4) + (faixa 5, se base de cálculo
> faixa 4)"""
faixa = [1903.98, 2826.65, 3751.05, 4664.68]
aliq = [0.075, 0.15]