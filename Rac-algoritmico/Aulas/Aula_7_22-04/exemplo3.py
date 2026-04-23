"""
Validar as entradas de um codigo usando funções
Somar 2 numeros
"""
import utils as u

num1 = u.get_int_num("Digite o primeiro numero: ")
num2 = u.get_int_num("Digite o segundo numero: ")
soma = u.somar(num1, num2)
print("A soma dos numeros é: ", soma)