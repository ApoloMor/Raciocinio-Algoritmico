#calcular a idade de uma pessoa com o seu ano de nascimento
import datetime

ano_nasc = int(input("Digite seu ano de nascimento:"))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc
resp = input("você já fez aniversário este ano? (s/n)")
""""if resp == "s":
    idade = ano_atual - ano_nasc
else:
    idade = ano_atual - ano_nasc -1
print("A sua idade é:", idade)
"""
if resp == "n": #idade = idade - 1
        idade -= 1
print("A sua idade é:", idade)