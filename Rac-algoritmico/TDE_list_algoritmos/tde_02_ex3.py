"""
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e
mostre-a expressa apenas em dias."""

idade_anos = int(input("Digite sua idade em anos:"))
idade_meses = int(input("Digite sua idade em meses:"))
idade_dias = int(input("Digite sua idade em dias:"))
# Considerando 1 ano = 365 dias e 1 mês = 30 dias
total_dias = (idade_anos * 365) + (idade_meses * 30) + idade_dias

print(f"Sua idade em dias é:{total_dias}")