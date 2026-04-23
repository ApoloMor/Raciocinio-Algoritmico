"""
Imposto de Renda
"""
faixas = [1903.98, 2826.65, 3751.05, 4664.68]
taxas = [0.075, 0.15, 0.225, 0.275]
dep = 189.59
salario = float(input("Qual o seu salário? "))
n_dep = int(input("Qual o número de dependentes? "))
pensao = float(input("Qual o valor de pensão? "))
outras = float(input("Qual o valor de outras deduções? "))
base = salario - (n_dep * dep + pensao + outras)
ir = 0
for i in range(3):
    if base > faixas[i]:
        if base < faixas[i+1]:
            ir += (base - faixas[i]) * taxas[i]
        else:
            ir += (faixas[i+1] - faixas[i]) * taxas[i]
if base > faixas[3]:
    ir += (base - faixas[3]) * taxas[3]
print(ir)