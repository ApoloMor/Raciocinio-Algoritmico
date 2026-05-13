"""Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre-a
expressa em anos, meses e dias."""
idade_dias = int(input("Digite a sua idade total em dias:"))
anos = idade_dias / 365
resto_dias = idade_dias % 365
meses = resto_dias / 30
dias = resto_dias % 30
print(f"A idade expressa é: {anos} ano(s), {meses} mês(es) e {dias} dia(s).")