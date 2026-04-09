"""Criar um programa que solicita ao usuário 10 números, contando
quantos são pares e quantos são ímpares. Informar ao final estas
informações."""
sum = 0
for i in range(10):
    nm = int(input("digite o numero:"))
    sum += nm
print(f"A soma dos numeros é:{sum}")
